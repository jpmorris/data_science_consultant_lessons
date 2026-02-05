# Modern LLM Architecture Code References

This document provides direct links to implementation code for modern architectural innovations in open-source LLMs.

## Official Model Implementations

### Llama (Meta)
**Repository**: https://github.com/meta-llama/llama3  
**Repository (Llama 2)**: https://github.com/meta-llama/llama

#### Key Files to Study:
1. **Main Model Architecture**
   - `llama/model.py` - Complete model implementation
   - Core components: RMSNorm, RoPE, SwiGLU, GQA

2. **RMSNorm Implementation**
   ```python
   # From llama/model.py
   class RMSNorm(torch.nn.Module):
       def __init__(self, dim: int, eps: float = 1e-6):
           super().__init__()
           self.eps = eps
           self.weight = nn.Parameter(torch.ones(dim))

       def _norm(self, x):
           return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)

       def forward(self, x):
           output = self._norm(x.float()).type_as(x)
           return output * self.weight
   ```

3. **RoPE (Rotary Position Embeddings)**
   ```python
   # From llama/model.py
   def precompute_freqs_cis(dim: int, end: int, theta: float = 10000.0):
       freqs = 1.0 / (theta ** (torch.arange(0, dim, 2)[: (dim // 2)].float() / dim))
       t = torch.arange(end, device=freqs.device)
       freqs = torch.outer(t, freqs).float()
       freqs_cis = torch.polar(torch.ones_like(freqs), freqs)  # complex64
       return freqs_cis

   def apply_rotary_emb(xq, xk, freqs_cis):
       xq_ = torch.view_as_complex(xq.float().reshape(*xq.shape[:-1], -1, 2))
       xk_ = torch.view_as_complex(xk.float().reshape(*xk.shape[:-1], -1, 2))
       freqs_cis = reshape_for_broadcast(freqs_cis, xq_)
       xq_out = torch.view_as_real(xq_ * freqs_cis).flatten(3)
       xk_out = torch.view_as_real(xk_ * freqs_cis).flatten(3)
       return xq_out.type_as(xq), xk_out.type_as(xk)
   ```

4. **Grouped Query Attention (GQA)**
   ```python
   # From llama/model.py - Attention class
   class Attention(nn.Module):
       def __init__(self, args: ModelArgs):
           super().__init__()
           self.n_kv_heads = args.n_heads if args.n_kv_heads is None else args.n_kv_heads
           self.n_local_heads = args.n_heads
           self.n_local_kv_heads = self.n_kv_heads
           self.n_rep = self.n_local_heads // self.n_local_kv_heads  # Repetition factor
           self.head_dim = args.dim // args.n_heads

           self.wq = Linear(args.dim, args.n_heads * self.head_dim, bias=False)
           self.wk = Linear(args.dim, self.n_kv_heads * self.head_dim, bias=False)
           self.wv = Linear(args.dim, self.n_kv_heads * self.head_dim, bias=False)
           self.wo = Linear(args.n_heads * self.head_dim, args.dim, bias=False)
   
       def forward(self, x, ...):
           bsz, seqlen, _ = x.shape
           xq, xk, xv = self.wq(x), self.wk(x), self.wv(x)
           
           # Reshape for multi-head attention
           xq = xq.view(bsz, seqlen, self.n_local_heads, self.head_dim)
           xk = xk.view(bsz, seqlen, self.n_local_kv_heads, self.head_dim)
           xv = xv.view(bsz, seqlen, self.n_local_kv_heads, self.head_dim)
           
           # Apply RoPE
           xq, xk = apply_rotary_emb(xq, xk, freqs_cis)
           
           # Repeat k/v heads if n_kv_heads < n_heads (GQA)
           xk = repeat_kv(xk, self.n_rep)
           xv = repeat_kv(xv, self.n_rep)
           # ... attention computation
   ```

5. **SwiGLU Activation**
   ```python
   # From llama/model.py - FeedForward class
   class FeedForward(nn.Module):
       def __init__(self, dim: int, hidden_dim: int, multiple_of: int, ffn_dim_multiplier: Optional[float]):
           super().__init__()
           hidden_dim = int(2 * hidden_dim / 3)
           if ffn_dim_multiplier is not None:
               hidden_dim = int(ffn_dim_multiplier * hidden_dim)
           hidden_dim = multiple_of * ((hidden_dim + multiple_of - 1) // multiple_of)

           self.w1 = Linear(dim, hidden_dim, bias=False)  # Gate projection
           self.w2 = Linear(hidden_dim, dim, bias=False)  # Down projection
           self.w3 = Linear(dim, hidden_dim, bias=False)  # Up projection

       def forward(self, x):
           return self.w2(F.silu(self.w1(x)) * self.w3(x))  # SwiGLU
   ```

---

## DeepSeek

**Repository**: https://github.com/deepseek-ai/DeepSeek-V2  
**Repository (V3)**: https://github.com/deepseek-ai/DeepSeek-V3

### Key Innovations to Study:

#### 1. Multi-Head Latent Attention (MLA)
**Location**: `modeling_deepseek.py`

```python
# Simplified MLA concept from DeepSeek-V2
class MultiHeadLatentAttention(nn.Module):
    """
    MLA compresses KV cache using low-rank decomposition:
    - Instead of storing full K, V matrices
    - Store compressed latent representation
    - Dramatically reduces memory (e.g., 5.7GB -> 0.8GB for 32K context)
    """
    def __init__(self, config):
        super().__init__()
        self.q_lora_rank = config.q_lora_rank  # e.g., 1536
        self.kv_lora_rank = config.kv_lora_rank  # e.g., 512
        self.qk_rope_head_dim = config.qk_rope_head_dim
        
        # Query compression
        self.q_a_proj = nn.Linear(hidden_size, q_lora_rank, bias=False)
        self.q_b_proj = nn.Linear(q_lora_rank, num_heads * head_dim, bias=False)
        
        # KV compression - this is the key innovation
        self.kv_a_proj_with_mqa = nn.Linear(
            hidden_size,
            kv_lora_rank + qk_rope_head_dim,  # Compressed representation
            bias=False
        )
        self.kv_b_proj = nn.Linear(
            kv_lora_rank,
            num_heads * (head_dim - qk_rope_head_dim),
            bias=False
        )
    
    def forward(self, hidden_states, ...):
        # Query: low-rank compression
        q = self.q_b_proj(self.q_a_proj(hidden_states))
        
        # KV: compressed latent representation
        compressed_kv = self.kv_a_proj_with_mqa(hidden_states)
        kv_latent, k_rope = compressed_kv.split([self.kv_lora_rank, self.qk_rope_head_dim], dim=-1)
        
        # Expand KV from latent
        k = self.kv_b_proj(kv_latent)
        v = self.kv_b_proj(kv_latent)  # Can share or use separate projection
        
        # Apply RoPE only to the rope dimension
        # ... attention computation with compressed KV cache
```

**Key Benefit**: For DeepSeek-V2 with 128 heads and 128 dim/head:
- Traditional: 128 * 128 * 2 (K+V) = 32,768 dims per token to cache
- MLA: 512 compressed dims per token (60x reduction!)

#### 2. Mixture of Experts (MoE) - DeepSeek Implementation
**Location**: `modeling_deepseek.py`

```python
# DeepSeek MoE with fine-grained experts
class DeepSeekMoE(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.num_experts = config.n_routed_experts  # e.g., 64 experts
        self.num_experts_per_tok = config.num_experts_per_tok  # e.g., 6 active
        self.num_shared_experts = config.n_shared_experts  # e.g., 2 always active
        
        # Router network
        self.gate = nn.Linear(config.hidden_size, config.n_routed_experts, bias=False)
        
        # Routed experts (sparse)
        self.experts = nn.ModuleList([
            DeepSeekMLP(config) for _ in range(self.num_experts)
        ])
        
        # Shared experts (always active)
        self.shared_experts = DeepSeekMLP(config, is_shared=True)
    
    def forward(self, hidden_states):
        batch_size, seq_len, hidden_dim = hidden_states.shape
        hidden_states = hidden_states.view(-1, hidden_dim)
        
        # Router logits - which experts to use?
        router_logits = self.gate(hidden_states)
        
        # Top-k routing with auxiliary loss for load balancing
        routing_weights, selected_experts = torch.topk(
            router_logits, self.num_experts_per_tok, dim=-1
        )
        routing_weights = F.softmax(routing_weights, dim=-1)
        
        # Compute routed expert outputs
        expert_outputs = torch.zeros_like(hidden_states)
        for i, expert in enumerate(self.experts):
            expert_mask = (selected_experts == i)
            if expert_mask.any():
                expert_input = hidden_states[expert_mask.any(dim=-1)]
                expert_output = expert(expert_input)
                # Weight by routing weights and accumulate
                expert_outputs[expert_mask.any(dim=-1)] += (
                    expert_output * routing_weights[expert_mask].unsqueeze(-1)
                )
        
        # Always compute shared experts
        shared_output = self.shared_experts(hidden_states)
        
        # Combine routed and shared
        final_output = expert_outputs + shared_output
        return final_output.view(batch_size, seq_len, hidden_dim)
```

**Load Balancing Loss**:
```python
def load_balancing_loss(router_logits, selected_experts, num_experts):
    """
    Encourages equal distribution of tokens across experts
    Prevents some experts from being overused/underused
    """
    # Count how many tokens go to each expert
    expert_usage = torch.zeros(num_experts, device=router_logits.device)
    for i in range(num_experts):
        expert_usage[i] = (selected_experts == i).float().sum()
    
    # Compute probability of selecting each expert
    router_probs = F.softmax(router_logits, dim=-1).mean(dim=0)
    
    # Loss: (usage_fraction) * (selection_probability) should be uniform
    num_tokens = router_logits.shape[0]
    expert_usage_fraction = expert_usage / num_tokens
    loss = (expert_usage_fraction * router_probs).sum() * num_experts
    return loss
```

#### 3. Multi-Token Prediction (DeepSeek-V3)
**Location**: Check V3 release - new training objective

```python
# Concept: predict multiple future tokens simultaneously
class MultiTokenPredictionHead(nn.Module):
    """
    Instead of predicting just next token:
    Given [t1, t2, t3], predict [t4, t5, t6, t7] simultaneously
    
    Benefits:
    - Better training signal
    - Learns longer-range dependencies
    - Can improve sample efficiency
    """
    def __init__(self, config, num_future_tokens=4):
        super().__init__()
        self.num_future_tokens = num_future_tokens
        
        # Separate prediction heads for each future position
        self.prediction_heads = nn.ModuleList([
            nn.Linear(config.hidden_size, config.vocab_size, bias=False)
            for _ in range(num_future_tokens)
        ])
    
    def forward(self, hidden_states, future_token_ids):
        """
        hidden_states: [batch, seq_len, hidden_dim]
        future_token_ids: [batch, seq_len, num_future_tokens] - ground truth
        """
        losses = []
        for i, head in enumerate(self.prediction_heads):
            logits = head(hidden_states)
            loss = F.cross_entropy(
                logits.view(-1, logits.size(-1)),
                future_token_ids[..., i].view(-1)
            )
            losses.append(loss)
        
        return sum(losses) / len(losses)
```

---

## Mixtral (Mistral AI)

**Repository**: https://github.com/mistralai/mistral-src  
**Hugging Face**: https://huggingface.co/mistralai/Mixtral-8x7B-v0.1

### Mixtral 8x7B MoE Implementation

```python
# From Mistral's implementation
class MixtralSparseMoeBlock(nn.Module):
    """
    8 experts, top-2 routing per token
    Simpler than DeepSeek but effective
    """
    def __init__(self, config):
        super().__init__()
        self.hidden_dim = config.hidden_size
        self.ffn_dim = config.intermediate_size
        self.num_experts = config.num_local_experts  # 8
        self.top_k = config.num_experts_per_tok  # 2

        # Gating network
        self.gate = nn.Linear(self.hidden_dim, self.num_experts, bias=False)
        
        # 8 expert networks
        self.experts = nn.ModuleList([
            MixtralBlockSparseFF(config) for _ in range(self.num_experts)
        ])

    def forward(self, hidden_states):
        batch_size, sequence_length, hidden_dim = hidden_states.shape
        hidden_states = hidden_states.view(-1, hidden_dim)
        
        # Router: select top-2 experts per token
        router_logits = self.gate(hidden_states)
        routing_weights = F.softmax(router_logits, dim=1, dtype=torch.float)
        routing_weights, selected_experts = torch.topk(routing_weights, self.top_k, dim=-1)
        routing_weights /= routing_weights.sum(dim=-1, keepdim=True)  # Renormalize
        
        # Dispatch to experts
        final_hidden_states = torch.zeros(
            (batch_size * sequence_length, hidden_dim),
            dtype=hidden_states.dtype,
            device=hidden_states.device
        )
        
        # Expert computation - batched for efficiency
        for expert_idx in range(self.num_experts):
            expert_layer = self.experts[expert_idx]
            idx, top_x = torch.where(selected_experts == expert_idx)
            
            if top_x.shape[0] == 0:
                continue
            
            # Forward through this expert for selected tokens
            current_hidden_states = hidden_states[idx]
            current_hidden_states = expert_layer(current_hidden_states)
            
            # Weight by routing weights
            current_hidden_states *= routing_weights[idx, top_x, None]
            final_hidden_states[idx] += current_hidden_states
        
        final_hidden_states = final_hidden_states.reshape(batch_size, sequence_length, hidden_dim)
        return final_hidden_states, router_logits
```

---

## Flash Attention

**Repository**: https://github.com/Dao-AILab/flash-attention

### Flash Attention 2 - Optimized Attention

```python
# Using Flash Attention in PyTorch
from flash_attn import flash_attn_qkvpacked_func, flash_attn_func

# Standard usage
def flash_attention_forward(q, k, v, causal=True):
    """
    q, k, v: [batch, seqlen, num_heads, head_dim]
    
    Flash Attention benefits:
    - O(N) memory instead of O(N²) for attention matrix
    - Faster on GPU due to IO-aware algorithm
    - Exact attention (not approximate)
    """
    output = flash_attn_func(q, k, v, causal=causal)
    return output

# In practice, integrated into model:
class FlashAttention(nn.Module):
    def forward(self, x, ...):
        # Project to Q, K, V
        q = self.q_proj(x)
        k = self.k_proj(x) 
        v = self.v_proj(x)
        
        # Reshape for multi-head
        q = q.view(bsz, seqlen, num_heads, head_dim)
        k = k.view(bsz, seqlen, num_heads, head_dim)
        v = v.view(bsz, seqlen, num_heads, head_dim)
        
        # Flash attention
        output = flash_attn_func(q, k, v, causal=True)
        
        return self.o_proj(output.view(bsz, seqlen, -1))
```

**How it works**:
- Standard attention materializes N×N attention matrix in memory
- Flash Attention computes attention in blocks using fast SRAM
- Reduces memory from O(N²) to O(N)
- 2-4x faster for long sequences

---

## Hugging Face Transformers - Study All Models

**Repository**: https://github.com/huggingface/transformers

Most models have reference implementations here:

### Quick Links to Model Code:

1. **Llama**: `src/transformers/models/llama/modeling_llama.py`
2. **Mistral**: `src/transformers/models/mistral/modeling_mistral.py`
3. **Mixtral**: `src/transformers/models/mixtral/modeling_mixtral.py`
4. **DeepSeek**: `src/transformers/models/deepseek/modeling_deepseek.py`
5. **Qwen**: `src/transformers/models/qwen2/modeling_qwen2.py`
6. **GPT-NeoX**: `src/transformers/models/gpt_neox/modeling_gpt_neox.py`

### Common Pattern to Study:

```python
# Most modern models follow this structure:
class ModernTransformerBlock(nn.Module):
    def __init__(self, config):
        super().__init__()
        # 1. Pre-norm (RMSNorm or LayerNorm)
        self.input_layernorm = RMSNorm(config.hidden_size)
        
        # 2. Attention (with GQA, Flash Attention, etc.)
        self.self_attn = Attention(config)
        
        # 3. Post-attention norm
        self.post_attention_layernorm = RMSNorm(config.hidden_size)
        
        # 4. FFN or MoE
        if config.use_moe:
            self.mlp = MoEBlock(config)
        else:
            self.mlp = FeedForward(config)  # SwiGLU
    
    def forward(self, hidden_states, ...):
        # Pre-norm + Attention + Residual
        residual = hidden_states
        hidden_states = self.input_layernorm(hidden_states)
        hidden_states = self.self_attn(hidden_states, ...)
        hidden_states = residual + hidden_states
        
        # Pre-norm + FFN/MoE + Residual
        residual = hidden_states
        hidden_states = self.post_attention_layernorm(hidden_states)
        hidden_states = self.mlp(hidden_states)
        hidden_states = residual + hidden_states
        
        return hidden_states
```

---

## Hands-On Tutorial: Build Your Own

**Repository**: https://github.com/karpathy/llama2.c
- Minimal Llama 2 implementation in pure C
- Great for understanding every detail

**Alternative**: https://github.com/karpathy/nanoGPT
- Minimal GPT implementation
- Good starting point before adding modern features

### Exercise: Implement Modern Features

Start with nanoGPT and progressively add:
1. Replace LayerNorm with RMSNorm
2. Add RoPE instead of learned positions
3. Replace GELU with SwiGLU
4. Implement GQA instead of MHA
5. Add Flash Attention
6. Implement simple MoE (2 experts)

---

## Quantization Code Examples

### GPTQ (Post-Training Quantization)
**Repository**: https://github.com/IST-DASLab/gptq

```python
from gptq import GPTQ

# Quantize model to 4-bit
quantizer = GPTQ(model)
quantizer.quantize(
    calibration_data,
    bits=4,  # 4-bit quantization
    group_size=128  # Group size for quantization
)
```

### AWQ (Activation-aware Weight Quantization)
**Repository**: https://github.com/mit-han-lab/llm-awq

```python
from awq import AutoAWQForCausalLM

# Load and quantize
model = AutoAWQForCausalLM.from_pretrained("meta-llama/Llama-2-7b")
model.quantize(
    tokenizer,
    quant_config={"w_bit": 4, "q_group_size": 128}
)
```

---

## Serving/Inference Frameworks

### vLLM - Paged Attention
**Repository**: https://github.com/vllm-project/vllm

```python
# Key innovation: PagedAttention - OS-style paging for KV cache
from vllm import LLM, SamplingParams

llm = LLM(model="meta-llama/Llama-2-7b-hf")
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

prompts = ["Hello, my name is", "The future of AI is"]
outputs = llm.generate(prompts, sampling_params)
```

**PagedAttention Concept**:
```python
# KV cache is split into blocks (pages)
# Can be non-contiguous in memory
# Enables:
# - Better memory utilization (23x more than HF)
# - Sequence sharing for beam search
# - Easy context swapping

class PagedAttention:
    """
    Instead of allocating max_seq_len * batch_size upfront:
    - Allocate blocks (pages) of KV cache dynamically
    - Share blocks across sequences (prefix sharing)
    - Swap blocks to CPU if needed
    """
    def __init__(self, block_size=16):
        self.block_size = block_size
        self.kv_cache_blocks = []  # List of allocated blocks
        self.block_tables = {}  # Maps seq_id -> list of block_ids
```

---

## Resources for Deep Dive

### Papers with Code
- All papers have code implementations linked
- https://paperswithcode.com/

### Model Cards
- Hugging Face model pages have architecture details
- Example: https://huggingface.co/meta-llama/Llama-2-7b

### Official Technical Reports
1. **Llama 2**: https://arxiv.org/abs/2307.09288
2. **DeepSeek-V2**: https://arxiv.org/abs/2405.04434
3. **Mixtral**: https://arxiv.org/abs/2401.04088

---

## Suggested Learning Path

1. **Start**: Study Llama 2 implementation (cleanest modern baseline)
   - Focus on: RMSNorm, RoPE, SwiGLU, GQA

2. **Optimize**: Integrate Flash Attention
   - Understand memory optimization

3. **Scale**: Study Mixtral MoE
   - Understand sparse computation

4. **Advanced**: Study DeepSeek MLA
   - Understand KV cache compression

5. **Deploy**: Study vLLM/TGI
   - Understand inference optimization

6. **Practice**: Implement each component from scratch
   - Start with blog posts/tutorials
   - Then study production code
   - Finally implement yourself

---

## Interactive Notebooks

### Google Colab Examples

1. **Llama from Scratch**: https://colab.research.google.com/github/facebookresearch/llama-recipes/
2. **Mixtral Fine-tuning**: Search "Mixtral Colab" on Hugging Face
3. **Flash Attention Benchmark**: Available in flash-attention repo

### Jupyter Notebooks in HF Repos

Many model repos include example notebooks:
- Training examples
- Inference examples  
- Fine-tuning examples

---

## Next Steps

1. **Clone the repos**: Start with Llama 3 and Mixtral
2. **Set up environment**: Install dependencies
3. **Run examples**: Get model working locally (or on Colab)
4. **Read the code**: Start with model.py files
5. **Modify**: Change hyperparameters, add logging, visualize
6. **Implement**: Build your own version from scratch

**Start Simple**: 
- Don't try to understand everything at once
- Focus on one component (e.g., RoPE) 
- Implement it in isolation
- Then integrate into larger model
