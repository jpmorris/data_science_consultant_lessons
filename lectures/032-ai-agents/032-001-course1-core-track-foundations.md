# LLM Engineering: Core Track Foundations
**Udemy Course — 8 Weeks, 5 Days Each**

Source: `udemy_transcript_6100015.txt`

---

## Table of Contents

- [Week 1: Foundations — APIs, Prompting, and First Applications](#week-1-foundations--apis-prompting-and-first-applications)
- [Week 2: Open-Source Models and Local Inference](#week-2-open-source-models-and-local-inference)
- [Week 3: Multi-Modal LLMs and Production-Grade APIs](#week-3-multi-modal-llms-and-production-grade-apis)
- [Week 4: Building LLM Pipelines and UI Frontends](#week-4-building-llm-pipelines-and-ui-frontends)
- [Week 5: Retrieval-Augmented Generation (RAG)](#week-5-retrieval-augmented-generation-rag)
- [Week 6: Fine-Tuning a Frontier Model](#week-6-fine-tuning-a-frontier-model)
- [Week 7: Fine-Tuning an Open-Source Model with QLoRA](#week-7-fine-tuning-an-open-source-model-with-qlora)
- [Week 8: Building Autonomous Multi-Agent Systems](#week-8-building-autonomous-multi-agent-systems)

---

## Week 1: Foundations — APIs, Prompting, and First Applications

### Day 1: Course Introduction + OpenAI API Setup

**Learning Objectives:**
- Understand the scope of LLM engineering vs. data science
- Set up OpenAI API key and make first API call
- Understand model tiers (GPT-4o vs. GPT-4o-mini vs. o1) and cost tradeoffs
- Identify the difference between completion and chat completion APIs

**LLM Concepts Covered:**
- **What is an LLM engineer?**: Someone who builds production applications using LLMs as components — not training from scratch, but engineering systems that leverage foundation models. Distinct from ML researchers who train models and from data scientists who do analytics.
- **Chat completion API format**: The modern OpenAI API uses a messages list: `[{role: "system", content: ...}, {role: "user", content: ...}]`. The model generates the next assistant turn. This format supports multi-turn conversations natively.
- **System prompt**: The first message with `role: "system"`. Sets the overall context, persona, and constraints for the model. Users don't see this — it's the developer's instruction layer. Critical for controlling model behavior in production.
- **Model tiers**: GPT-4o is the flagship (expensive, capable); GPT-4o-mini is much cheaper with acceptable quality for many tasks; o1/o1-mini are reasoning models that "think" before answering (very expensive, best for complex multi-step reasoning). Rule: use the cheapest model that gets the job done.
- **Temperature**: A sampling parameter (0-2) controlling randomness. Temperature=0: near-deterministic (pick highest-probability token each time). Temperature=1: default sampling. Temperature=2: very random/creative. For factual tasks: low temperature. For creative tasks: higher temperature.

**Project:** Build a simple question-answering assistant using the OpenAI API.

---

### Day 2: Prompt Engineering Fundamentals

**Learning Objectives:**
- Write effective zero-shot, one-shot, and few-shot prompts
- Apply chain-of-thought prompting to improve reasoning
- Understand token counting and context window limits
- Use the `tiktoken` library to count tokens before sending requests

**LLM Concepts Covered:**
- **Zero-shot prompting**: Asking the model to perform a task with no examples. "Classify this review as positive or negative: [review]". Works for tasks well-represented in training data.
- **Few-shot prompting**: Providing 2-10 examples before the actual query. Dramatically improves performance on niche tasks or unusual output formats. The model infers the pattern from examples and applies it to the new input.
- **Chain-of-thought (CoT)**: Prompting the model to show its reasoning: "Think step by step before answering." Improves accuracy on math, logic, and multi-step reasoning. Why it works: generating intermediate reasoning tokens forces the model to allocate compute to the problem before committing to an answer.
- **Context window**: The maximum number of tokens an LLM can process in a single call (input + output combined). GPT-4o: 128K tokens. Exceeding this truncates your input (usually the beginning). Critical for RAG and long-document tasks.
- **Token vs. word**: A token is roughly 0.75 words in English (more for code, less for other languages). `tiktoken` library lets you count tokens before sending — essential for estimating cost and avoiding context overflow.
- **Prompt injection**: A security concern: if user input is concatenated into a system prompt, a malicious user could write instructions that override the system prompt. Mitigation: sanitize user input, use structured formats, keep user input separate from instructions.

**Project:** Prompt engineering playground — test different prompting strategies on a classification task, measure accuracy.

---

### Day 3: The OpenAI Ecosystem — Models, Embeddings, and Moderation

**Learning Objectives:**
- Use the Embeddings API to convert text to vectors
- Understand cosine similarity for semantic search
- Use the Moderation API to detect harmful content
- Build a simple semantic search system

**LLM Concepts Covered:**
- **Embeddings**: Dense vector representations of text. Similar texts have similar vectors (high cosine similarity). OpenAI `text-embedding-3-small` produces 1536-dimensional vectors. Use cases: semantic search, clustering, classification, RAG.
- **Cosine similarity**: The standard similarity metric for embeddings. Measures the angle between two vectors (not their magnitude). Ranges from -1 (opposite) to 1 (identical). For normalized embeddings, equivalent to dot product.
- **Why embeddings beat keyword search**: Keywords only match exact words. Embeddings capture semantic meaning — "automobile" and "car" will have similar embeddings even though they share no characters.
- **Moderation API**: OpenAI's dedicated endpoint for content safety. Returns scores for categories: hate, harassment, sexual, violence, self-harm. Free to use. Should be applied to user inputs in production applications that accept free text.
- **Embedding dimensionality tradeoff**: Higher-dimensional embeddings (e.g., 3072 vs. 1536) capture more nuance but cost more storage and compute. For most applications, 1536 is sufficient.

**Project:** Semantic document search — embed a corpus of documents, embed a query, return the top-k most similar documents.

---

### Day 4: Anthropic Claude and the Multi-Model Landscape

**Learning Objectives:**
- Make API calls to Claude (Anthropic) using the same pattern as OpenAI
- Compare capabilities of GPT-4o vs. Claude Sonnet vs. Gemini Pro
- Use LiteLLM to write model-agnostic code
- Understand why using multiple model providers is a production best practice

**LLM Concepts Covered:**
- **Anthropic Claude API**: Similar to OpenAI but with a separate `system` parameter rather than embedding system in the messages list. `anthropic.messages.create(model=..., system=..., messages=[...])`. Claude 3.5 Sonnet is the leading model for code and reasoning as of course recording.
- **Model-agnostic code with LiteLLM**: LiteLLM provides a unified interface to 100+ LLMs (OpenAI, Anthropic, Gemini, Groq, Ollama, etc.) with a single `completion()` call. Change the model string, not the code. Essential for multi-model experiments and vendor-agnostic production systems.
- **Why use multiple providers**: Redundancy (if OpenAI goes down), cost optimization (route simple queries to cheap models), performance optimization (some models excel at specific tasks), latency (different providers have different response times).
- **Prompt caching (Anthropic)**: If you send the same long prefix (e.g., a long system prompt or document) in multiple calls, Anthropic caches it and charges only for the first call. Dramatic cost reduction for applications with large, repeated context.

**Project:** Multi-model comparison tool — send the same prompt to GPT-4o, Claude, and Gemini, display responses side-by-side.

---

### Day 5: Building a Production-Quality Summarization Tool

**Learning Objectives:**
- Handle API errors, rate limits, and retries
- Stream responses for better UX
- Build a Jupyter notebook-based pipeline
- Estimate and control API costs

**LLM Concepts Covered:**
- **Streaming**: Instead of waiting for the full response, receive tokens as they're generated. OpenAI: `stream=True` returns a generator of chunks. Dramatically improves perceived latency for long responses. Essential for chat interfaces.
- **Rate limits**: APIs impose limits on requests/minute (RPM) and tokens/minute (TPM). Exceeding them returns 429 errors. Mitigation: exponential backoff retry, request batching, parallel requests within limits.
- **Exponential backoff**: When a rate limit (429) or transient error occurs, wait 2^n seconds before retrying (1s, 2s, 4s, 8s...). Add jitter (random offset) to avoid thundering herd when many clients retry simultaneously.
- **Cost estimation**: Before running a pipeline at scale, calculate: input tokens × input_cost_per_token + output tokens × output_cost_per_token. Use tiktoken to count tokens. Multiply by number of documents. Build cost-awareness into every LLM workflow.
- **Structured logging**: In production, log every LLM call: model, input_tokens, output_tokens, latency, cost, request_id. Enables debugging, cost tracking, and performance monitoring.

**Project:** Automated article summarizer — takes a list of URLs, fetches content, summarizes with GPT-4o-mini, streams output, tracks cost.

---

## Week 2: Open-Source Models and Local Inference

### Day 1: HuggingFace Transformers — Running Models Locally

**Learning Objectives:**
- Load and run a text generation model locally using HuggingFace `transformers`
- Understand the `pipeline` abstraction vs. raw model+tokenizer usage
- Run inference on CPU vs. GPU
- Understand why local models matter (cost, privacy, latency)

**LLM Concepts Covered:**
- **HuggingFace Hub**: Repository of 500K+ open-source models, datasets, and demos. Models are downloaded to local cache on first use. The primary source for open-source LLMs.
- **`transformers` Pipeline API**: High-level abstraction: `pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2")`. Handles tokenization, batching, decoding. Good for quick experiments. Raw model+tokenizer gives more control.
- **Model loading**: `AutoModelForCausalLM.from_pretrained(model_name)` + `AutoTokenizer.from_pretrained(model_name)`. Downloads weights to `~/.cache/huggingface`. First download can be several GB.
- **CPU vs. GPU inference**: On CPU: 7B model takes 30-120 seconds per response. On GPU (T4): 2-5 seconds. On GPU (A100): <1 second. GPU is essential for usable local inference. `model.to("cuda")` moves model to GPU.
- **Why local models**: (1) No API cost — run unlimited inferences for free after setup. (2) Privacy — data never leaves your machine. (3) Latency — no network round-trip. (4) Customization — fine-tuning, quantization, hardware-specific optimization. (5) Avoiding vendor lock-in.
- **Open weights vs. open source**: Open weights = model weights are public, but training code/data may not be. True open source = weights + code + data. Llama 3, Mistral: open weights. Most models on HuggingFace Hub are open weights.

**Project:** Local chatbot with Mistral 7B running entirely on your machine.

---

### Day 2: Quantization — Running Bigger Models on Consumer Hardware

**Learning Objectives:**
- Explain why quantization enables larger models on limited hardware
- Load 4-bit and 8-bit quantized models with `bitsandbytes`
- Measure quality-vs-size tradeoffs of quantization
- Run a 13B model on a single consumer GPU

**LLM Concepts Covered:**
- **Quantization**: Reducing the precision of model weights from 32-bit float (FP32) to lower precision (FP16, INT8, INT4). A 7B model at FP32 = 28GB VRAM. At FP16 = 14GB. At INT8 = 7GB. At INT4 = ~3.5GB. Makes models runnable on consumer hardware.
- **Quality tradeoff**: INT4 quantization loses some precision but the quality degradation is surprisingly small for most tasks (benchmarks show <5% performance drop vs. FP16). The model's knowledge is distributed across billions of parameters — losing a bit of precision in each is tolerable.
- **bitsandbytes**: HuggingFace library for quantization. `load_in_8bit=True` or `load_in_4bit=True` in `from_pretrained()`. Also supports QLoRA training (4-bit base + 16-bit adapters).
- **GGUF / llama.cpp**: Alternative quantization format (used by Ollama). More CPU-friendly. `Q4_K_M` is a common quantization level — 4-bit with mixed precision. Enables running 7B models on laptops with no GPU.
- **VRAM requirements rule of thumb**: Parameters (billions) × precision (bytes) = VRAM needed. 7B × 2 bytes (FP16) = 14GB. 7B × 0.5 bytes (INT4) = 3.5GB. Plus ~20% overhead for activations and KV cache.

**Project:** Compare Mistral 7B at FP16 vs. INT8 vs. INT4 on quality and speed.

---

### Day 3: Ollama — Local Inference Made Simple

**Learning Objectives:**
- Install and use Ollama to run LLMs locally
- Make API calls to Ollama using the OpenAI-compatible endpoint
- Run Llama 3, Phi-3, and Gemma locally with Ollama
- Understand the tradeoffs between Ollama and HuggingFace Transformers

**LLM Concepts Covered:**
- **Ollama**: A tool that packages local model inference into a simple CLI and HTTP server. `ollama pull llama3` downloads and configures the model. `ollama run llama3` starts a chat. Exposes an OpenAI-compatible API on `localhost:11434` — works with any OpenAI SDK client by changing the `base_url`.
- **Modelfile**: Ollama's configuration file for custom models. Define system prompt, temperature, context window. `FROM llama3` + custom parameters. Allows creating persistent customized local model endpoints.
- **Use case**: Ollama excels for quick local experiments and integrating local models into applications via the OpenAI-compatible API. HuggingFace Transformers gives more programmatic control (custom training, batching, modifications).
- **Small/fast models**: Phi-3 mini (3.8B), Gemma 2B — useful for fast local inference on CPU. Not as capable as 7B models but much faster. Good for low-latency applications or devices without GPU.

**Project:** Switch a Week 1 project from the OpenAI API to a local Ollama model with a one-line change.

---

### Day 4: Evaluating Open-Source Models — Benchmarks and Leaderboards

**Learning Objectives:**
- Navigate the Open LLM Leaderboard on HuggingFace
- Understand MMLU, HumanEval, HellaSwag, and other standard benchmarks
- Explain why benchmark performance doesn't always translate to real-world performance
- Build a simple custom evaluation framework

**LLM Concepts Covered:**
- **Open LLM Leaderboard**: HuggingFace's ranking of open-source models on standardized benchmarks. Key benchmarks: MMLU (knowledge across 57 subjects), HumanEval (code generation), HellaSwag (commonsense reasoning), ARC (grade-school science), TruthfulQA (avoiding false statements).
- **MMLU (Massive Multitask Language Understanding)**: 57 subjects from elementary math to professional law. Multiple-choice questions. Model picks A/B/C/D. Scores ~25% for random guessing, humans ~89%, GPT-4o ~87%, Llama 3 70B ~82%.
- **HumanEval**: 164 Python programming problems. Code is actually executed against test cases — measures functional correctness, not just syntactic plausibility. Pass@k metric: probability that at least 1 of k samples passes all tests.
- **Benchmark contamination**: If the benchmark test set was included in training data, the model's scores are inflated. Difficult to detect. A reason to distrust leaderboard numbers for newer models.
- **Task-specific evaluation matters more**: A model ranked 10th overall might be best for your specific task. Always evaluate on your own task distribution, not just trust leaderboard ranks.

**Project:** Build a mini evaluation harness — test 3 local models on 20 custom questions, compare accuracy.

---

### Day 5: Integrating Hugging Face into Pipelines + Inference API

**Learning Objectives:**
- Use HuggingFace's serverless Inference API (pay-per-use hosted inference)
- Understand the HuggingFace `datasets` library for data loading
- Build a pipeline that uses both cloud and local models based on task complexity
- Understand model cards and responsible AI metadata

**LLM Concepts Covered:**
- **HuggingFace Inference API**: Serverless hosted inference for models on the Hub. Send HTTP requests, get predictions. No GPU setup required. More expensive than running locally but cheaper than OpenAI for many models. `InferenceClient` Python SDK.
- **HuggingFace Datasets**: Library for loading and manipulating datasets from the Hub. `load_dataset("squad")` downloads and caches the dataset. Streaming mode for datasets too large to fit in memory. Arrow format for efficient columnar access.
- **Model cards**: Documentation files for models on HuggingFace Hub. Contain: intended use, limitations, training data, evaluation results, carbon footprint, license. Essential for responsible AI — understanding what a model was trained for before deploying it.
- **Hybrid routing**: Route complex/high-stakes queries to expensive frontier models (OpenAI/Anthropic). Route simple/bulk queries to cheap local or HuggingFace-hosted models. Based on query classification or heuristics (length, keyword matching). Reduces cost while maintaining quality on critical tasks.

**Project:** Hybrid routing system — classifies incoming queries and routes to GPT-4o-mini vs. local Mistral based on estimated difficulty.

---

## Week 3: Multi-Modal LLMs and Production-Grade APIs

### Day 1: Vision LLMs — Analyzing Images with GPT-4o

**Learning Objectives:**
- Send images to GPT-4o using the vision API
- Understand the difference between image URL input and base64 encoded input
- Know the token cost of images (how images are "tokenized")
- Build an image analysis pipeline

**LLM Concepts Covered:**
- **Vision API format**: GPT-4o accepts images inline in the messages array. Content is a list: `[{"type": "text", "text": "..."}, {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,..."}}]`. Can mix text and images in the same message.
- **Image tokenization**: GPT-4o divides images into 512×512 tiles. Each tile costs 170 tokens. A 1024×1024 image = 4 tiles = 680 tokens. High-detail mode uses more tiles for better accuracy on detailed images. Low-detail mode: fixed 85 tokens regardless of size.
- **Base64 encoding**: Converting binary image data to a string of ASCII characters. Required when passing image data directly (not via URL). In Python: `base64.b64encode(image_bytes).decode()`.
- **What vision LLMs can do**: Image captioning, object detection (described in text), OCR (reading text in images), chart interpretation, document understanding, medical image analysis (with caveats), visual QA.
- **Current limitations**: Poor spatial reasoning ("is the red box to the left or right of the blue circle?" — often wrong), struggles with precise counting, hallucinations about image content, inconsistent fine-grained detail recognition.

**Project:** Automated image metadata generator — analyze product photos and generate descriptions for e-commerce.

---

### Day 2: Audio and Speech APIs — Whisper and TTS

**Learning Objectives:**
- Transcribe audio with OpenAI Whisper API
- Generate speech with the TTS API
- Understand how voice interfaces are built (speech-to-text → LLM → text-to-speech)
- Run Whisper locally for free transcription

**LLM Concepts Covered:**
- **Whisper**: OpenAI's open-source speech-to-text model. Available via API (`openai.audio.transcriptions.create()`) or locally via `whisper` Python package. Transcribes 57+ languages. The API supports `.mp3`, `.wav`, `.m4a`, etc.
- **TTS (Text-to-Speech)**: `openai.audio.speech.create(model="tts-1", voice="alloy", input=text)`. 6 voices. Streams audio bytes. `tts-1-hd` for higher quality. Cost: $15 per million characters.
- **Voice pipeline architecture**: Microphone → Whisper (STT) → LLM (response) → TTS → Speaker. With streaming: stream the LLM response, send chunks to TTS as they arrive, play audio before full response is generated. Reduces latency from 3-5 seconds to <1 second.
- **Local Whisper**: Running Whisper locally (no API cost, no data leaving machine). `small`, `medium`, `large` models with speed/accuracy tradeoff. CUDA required for real-time transcription of long audio.
- **Diarization**: Identifying who spoke which segment in multi-speaker audio. Not built into Whisper — requires separate models (pyannote, Assembly AI). Important for meeting transcription.

**Project:** Voice assistant — record audio, transcribe with Whisper, generate a response with GPT-4o, play back as TTS.

---

### Day 3: Structured Outputs — JSON Mode and Pydantic Integration

**Learning Objectives:**
- Use `response_format={"type": "json_object"}` for JSON mode
- Define Pydantic models and use OpenAI's structured output API
- Understand constrained decoding and why it guarantees valid output
- Build a data extraction pipeline using structured outputs

**LLM Concepts Covered:**
- **JSON mode**: `response_format={"type": "json_object"}` forces the model to produce valid JSON. Does not guarantee specific keys — just syntactic JSON validity. Good for simple cases.
- **Structured outputs (OpenAI)**: Pass a Pydantic model (or JSON Schema) via `response_format=YourPydanticModel`. The API guarantees output matches the schema exactly — correct field names, correct types, no missing required fields. Uses constrained decoding internally.
- **Constrained decoding**: During token sampling, a finite state machine (FSM) tracks which output tokens are valid at each position given the schema. Invalid tokens get zero probability. Guarantees the output always matches the schema without needing retry logic.
- **Pydantic models for LLM output**: Define the desired output structure as a Python class inheriting from `BaseModel`. Field names, types, and descriptions help the model understand what to generate. Descriptions are especially important — they appear in the JSON Schema sent to the model.
- **Use cases**: Information extraction (pull structured data from unstructured text), classification with metadata, tool call parameters, any application needing reliable machine-readable output from an LLM.

**Project:** Resume parser — extract structured data (name, skills, experience, education) from free-text resumes using structured outputs.

---

### Day 4: Function Calling and Tool Use

**Learning Objectives:**
- Define tools in the OpenAI tools format (JSON Schema)
- Implement a tool-use loop (call LLM, call tool, pass result back, repeat)
- Build a practical tool-using assistant (weather, calculator, web search)
- Understand the relationship between tool calling and agentic AI

**LLM Concepts Covered:**
- **Tool calling (function calling)**: Define functions as JSON Schema objects. Pass them to the model in `tools=[...]`. The model decides whether to call a tool, and if so, which one and with what arguments. You execute the function and return the result in a follow-up message with `role: "tool"`.
- **Tool call loop**: (1) Send user message + tools definition. (2) Model returns `tool_calls` (not a text response). (3) Execute each tool call. (4) Append `role: "tool"` messages with results. (5) Send back to model. (6) Model generates final response. Can repeat if model wants to call more tools.
- **Parallel tool calls**: A model can request multiple tool calls in a single response. Execute them in parallel, return all results. Reduces round trips.
- **Tool design**: Good tool names and descriptions are critical — the model uses them to decide when and how to call tools. Parameter descriptions tell the model what each argument means. Clear, specific descriptions → better tool selection.
- **Tool calling vs. structured outputs**: Structured outputs: you control the schema, model always returns data in that shape. Tool calling: model decides when to call a function and what to pass. Tool calling is for taking actions; structured outputs are for extracting data.
- **Foundation of agents**: Tool calling is the mechanism that enables autonomous agents. An LLM with access to tools can take actions in the world — run code, search the web, query databases, send emails — and observe results, enabling multi-step autonomous behavior.

**Project:** Research assistant with tool use — can search the web, calculate, and look up facts using tool calling.

---

### Day 5: Building Robust Production APIs — Error Handling, Logging, Testing

**Learning Objectives:**
- Implement comprehensive error handling for LLM API calls
- Write unit tests for LLM-powered functions using mocking
- Build a cost-tracking dashboard
- Design for observability: structured logs, request IDs, latency tracking

**LLM Concepts Covered:**
- **Error taxonomy**: Rate limit (429): back off and retry. Invalid request (400): fix the prompt/parameters. Authentication (401): check API key. Server error (5xx): retry with backoff. Context length (400 with specific message): reduce input size.
- **Testing LLM code**: LLMs are non-deterministic and expensive — don't call the real API in unit tests. Use `unittest.mock.patch` to replace the API call with a fixed response. Test the surrounding logic independently. Integration tests (real API calls) run separately, less frequently.
- **Observability**: Every LLM call should emit structured log lines with: timestamp, request_id, model, input_tokens, output_tokens, latency_ms, cost_usd, success/failure. Enables debugging production issues and tracking spend.
- **Retry strategies**: For rate limits: exponential backoff with jitter. For server errors: same. For timeout: reduce request size or increase timeout. For context length: truncate or summarize earlier conversation. Never retry on 400 (invalid request) — it will always fail.
- **Prompt versioning**: Track which prompt version produced which output in production. When you update a prompt, compare outputs on a held-out dataset before shipping. Treat prompts like code — version control them.

**Project:** Production-hardened summarization API with full error handling, logging, cost tracking, and test suite.

---

## Week 4: Building LLM Pipelines and UI Frontends

### Day 1: Gradio — Building AI Web UIs in Python

**Learning Objectives:**
- Build interactive web UIs with Gradio
- Create chatbot interfaces with `gr.ChatInterface`
- Add file upload, image, and audio components
- Deploy a Gradio app to HuggingFace Spaces

**LLM Concepts Covered:**
- **Gradio**: Python library for building ML demos and web apps. `gr.Interface` for simple input/output. `gr.ChatInterface` for chatbot UIs. `gr.Blocks` for custom layouts. Runs locally and deploys to HuggingFace Spaces with one command.
- **Streaming in Gradio**: `yield` partial responses from your function to stream tokens to the UI as they're generated. Gradio handles the incremental display automatically. Critical for chat UIs — users can start reading while the model is still generating.
- **State management in Gradio**: `gr.State()` stores session-specific state (e.g., conversation history) across multiple function calls without exposing it in the UI. Each user session gets its own state.
- **HuggingFace Spaces**: Free hosting for Gradio (and Streamlit) apps. CPU-based hosting is free; GPU hosting has a small cost. Public or private. The standard way to share ML demos with the world.

**Project:** Gradio chatbot frontend for a GPT-4o-powered assistant with streaming, conversation history, and system prompt configuration.

---

### Day 2: LangChain — Chains, Prompts, and Memory

**Learning Objectives:**
- Build LLM chains using LangChain's LCEL (LangChain Expression Language)
- Use `ChatPromptTemplate` for reusable prompt templates
- Implement conversation memory with `ConversationBufferMemory`
- Understand when LangChain adds value vs. when to use the raw API

**LLM Concepts Covered:**
- **LangChain**: A framework for building LLM-powered applications. Provides abstractions for: prompt templates, output parsers, chains, memory, retrieval, agents. Reduces boilerplate. But adds complexity and abstraction — often debated in the community.
- **LCEL (LangChain Expression Language)**: `prompt | llm | output_parser` — pipe-based composition of LangChain components. Each component is a Runnable. Supports streaming, batching, and async out of the box.
- **ChatPromptTemplate**: Parameterized prompt templates. Define a template once with placeholders, instantiate with specific values. Enables systematic prompt management across a codebase.
- **Conversation memory**: `ConversationBufferMemory` stores full conversation history and injects it into every subsequent prompt. `ConversationSummaryMemory` summarizes older turns to save tokens. `ConversationTokenBufferMemory` limits history by token count.
- **When to use LangChain**: RAG pipelines (LangChain has strong RAG abstractions), rapid prototyping, teams with LangChain experience. When not to use: simple API wrappers (overkill), when you need full control over API calls, when debugging is critical (LangChain abstractions can hide errors).

**Project:** Multi-turn QA assistant with LangChain, persistent conversation memory, and structured prompt templates.

---

### Day 3: Document Processing Pipelines

**Learning Objectives:**
- Load and process PDFs, Word docs, and HTML with LangChain document loaders
- Implement text splitting strategies (character, recursive, token-based)
- Understand the tradeoffs of different chunking strategies
- Build a pipeline that processes a directory of documents

**LLM Concepts Covered:**
- **Document loaders**: LangChain provides loaders for PDF (`PyPDFLoader`), Word (`Docx2txtLoader`), web pages (`WebBaseLoader`), CSV, PowerPoint, and more. Each returns a list of `Document` objects with `page_content` and `metadata`.
- **Text splitting**: Documents must be split into chunks before embedding (context window limits). `RecursiveCharacterTextSplitter` is the standard: splits on paragraph breaks, then sentence breaks, then word breaks, ensuring chunks stay under a token limit while preserving natural text boundaries.
- **Chunk size and overlap**: Chunk size (e.g., 1000 tokens) determines how much context each retrieval brings. Overlap (e.g., 100 tokens) ensures concepts that span chunk boundaries aren't lost. Larger chunks: more context but more noise. Smaller chunks: more precise but may lose context.
- **Chunking quality matters enormously**: A common RAG failure mode is documents being split mid-sentence or mid-concept, retrieving incoherent fragments. Debugging chunking is essential — print retrieved chunks before the LLM sees them.
- **Metadata preservation**: Each chunk should retain metadata: source file, page number, section header. This enables citation ("this answer came from document X, page Y") and filtering ("only search documents from Q3 2024").

**Project:** Automated document pipeline — ingest a folder of PDFs, split them, output structured chunks with metadata for a downstream vector store.

---

### Day 4: Vector Databases — Chroma and FAISS

**Learning Objectives:**
- Store and retrieve document embeddings using ChromaDB
- Compare in-memory FAISS vs. persistent ChromaDB
- Implement similarity search with metadata filtering
- Understand approximate nearest neighbor (ANN) algorithms

**LLM Concepts Covered:**
- **Vector database**: A database optimized for storing and querying high-dimensional embedding vectors. Core operation: given a query vector, find the k most similar vectors (nearest neighbor search). Used in RAG, semantic search, recommendation systems.
- **ChromaDB**: Open-source vector database with Python SDK. Can run in-memory (lost on restart) or persist to disk. Supports metadata filtering alongside vector search (e.g., "find similar documents, but only from source=legal"). HuggingFace-integrated.
- **FAISS (Facebook AI Similarity Search)**: In-memory vector search library. Extremely fast. Many index types: Flat (exact, slow, small datasets), IVF (approximate, fast, large datasets), HNSW (graph-based, very fast, good recall). No persistence without serialization.
- **Approximate nearest neighbor (ANN)**: Exact nearest neighbor search scales as O(n) — too slow for millions of vectors. ANN algorithms (HNSW, IVF) trade a small amount of recall for orders-of-magnitude speedup. HNSW: builds a hierarchical graph; search traverses the graph instead of checking every vector.
- **Metadata filtering**: A critical feature for production RAG. Pre-filter the vector space by metadata fields before similarity search. "Find the 10 most similar documents to this query where department=legal and date>2024-01-01." Dramatically reduces irrelevant retrievals.
- **Embedding model choice**: The embedding model determines the quality of the vector space. `text-embedding-3-small` (OpenAI, cheap, good). `text-embedding-3-large` (OpenAI, expensive, better). `BAAI/bge-large-en` (open-source, free to run locally, competitive quality).

**Project:** Document retrieval system — embed 1000 documents into ChromaDB, support semantic search with metadata filtering, expose as a Python API.

---

### Day 5: End-to-End Pipeline Integration

**Learning Objectives:**
- Connect document ingestion → embedding → vector store → retrieval → LLM generation
- Handle edge cases: no relevant documents found, ambiguous queries
- Build a simple evaluation loop to measure retrieval accuracy
- Package the pipeline as a reusable Python class

**LLM Concepts Covered:**
- **The full RAG pipeline**: (1) Ingest: load documents, split into chunks, embed chunks. (2) Query: embed user query, retrieve top-k chunks by cosine similarity. (3) Generate: inject retrieved chunks into the prompt, call LLM to generate answer. (4) Return: answer + source citations.
- **Handling no-result cases**: If retrieved chunks are irrelevant (similarity below threshold), don't force the LLM to answer — it will hallucinate. Return "I don't have information about this topic." Threshold tuning is important.
- **Top-k selection**: How many chunks to retrieve (k=3, 5, 10). More k → more context but more noise and higher token cost. Typical choice: k=4-6. Some frameworks use MMR (Maximum Marginal Relevance) to diversify retrieved chunks and reduce redundancy.
- **Citation**: Include source metadata (filename, page number, URL) in the generation prompt. Instruct the model to cite sources in its answer. Enables users to verify claims and builds trust.

**Project:** Complete document QA system packaged as a Python class with ingest, query, and evaluate methods.

---

## Week 5: Retrieval-Augmented Generation (RAG)

### Day 1: RAG Fundamentals

**Learning Objectives:**
- Articulate why RAG outperforms fine-tuning for dynamic knowledge
- Implement a complete naive RAG system from scratch
- Understand the "lost in the middle" problem
- Measure the difference between RAG and no-RAG on a factual QA task

**LLM Concepts Covered:**
- **Why RAG**: LLMs have a training cutoff and fixed knowledge. Updating knowledge via fine-tuning is expensive and slow. RAG retrieves relevant documents at inference time, giving the model access to current, specific, or private information without retraining.
- **Naive RAG**: Embed all documents, embed query, retrieve top-k by cosine similarity, concatenate chunks into prompt, generate answer. Simple, often effective, but has multiple failure modes.
- **The "lost in the middle" problem**: LLMs pay more attention to the beginning and end of a long context. Relevant information placed in the middle of a long retrieved context gets "lost." Mitigation: put the most relevant chunk first or last, use re-ranking.
- **RAG vs. fine-tuning decision rule**: RAG for dynamic/factual knowledge that changes over time. Fine-tuning for style, format, or reasoning patterns that are stable. Most real-world use cases need RAG, not fine-tuning.
- **Hallucination mitigation with RAG**: Grounding the LLM's answer in retrieved documents significantly reduces hallucination. The model is instructed: "Answer only using the provided documents. If the answer isn't in the documents, say you don't know."

**Project:** Naive RAG system over a corpus of technical documentation.

---

### Day 2: Embeddings Deep Dive

**Learning Objectives:**
- Compare embedding models (OpenAI, BAAI/bge, sentence-transformers)
- Visualize embedding clusters with UMAP/t-SNE
- Understand how embedding quality affects retrieval quality
- Implement a benchmark for embedding model comparison

**LLM Concepts Covered:**
- **Sentence transformers**: HuggingFace library for efficient sentence embeddings. Models like `all-MiniLM-L6-v2` (fast, small, good quality) and `BAAI/bge-large-en-v1.5` (larger, SOTA for retrieval). Free to run locally.
- **Bi-encoder vs. cross-encoder**: Bi-encoder (standard embedding model): embed query and documents independently, then compare with cosine similarity. Fast — embed documents once offline. Cross-encoder: process (query, document) pairs together — much more accurate but too slow for full corpus search. Use bi-encoder for retrieval, cross-encoder for re-ranking candidates.
- **MTEB (Massive Text Embedding Benchmark)**: The standard leaderboard for embedding model quality. Covers retrieval, classification, clustering, reranking tasks. Use MTEB scores to choose embedding models for RAG.
- **Embedding space visualization**: t-SNE or UMAP projects high-dimensional embeddings to 2D for visualization. Clusters of topically similar documents should appear nearby. Useful for validating that the embedding model captures the relevant semantic structure in your corpus.
- **Domain mismatch**: General-purpose embedding models may struggle on highly specialized domains (legal, medical, code). Domain-specific fine-tuned embedding models (or fine-tuning your own) can significantly improve retrieval quality.

**Project:** Embedding model comparison — benchmark 3 models on a custom retrieval task, visualize embedding clusters.

---

### Day 3: Complete RAG Pipeline

**Learning Objectives:**
- Build a full RAG system with conversation history
- Implement query rewriting for follow-up questions
- Debug chunking errors by inspecting retrieved chunks
- Deploy a RAG system as a Gradio UI

**LLM Concepts Covered:**
- **Conversation history in RAG**: Pass prior turns into the prompt so the retriever knows the user's context. Reformulate the user's latest question using prior history before embedding it (query rewriting). Without this, follow-up questions like "tell me more about that" fail because "that" has no embedding.
- **Query rewriting**: Use an LLM to rewrite the user's latest query as a standalone question incorporating relevant context from the conversation history. Example: "What are its performance characteristics?" → "What are the performance characteristics of the PostgreSQL database discussed earlier?" The rewritten query embeds much better.
- **Chunking bugs**: A common failure mode is documents being split mid-sentence or mid-concept, retrieving incoherent fragments. Debugging chunking is essential — print retrieved chunks before the LLM sees them.
- **RAG system prompt pattern**: "You are a helpful assistant. Use the following documents to answer the user's question. If the answer is not in the documents, say you don't know. Always cite which document you're drawing from. Documents: [RETRIEVED CHUNKS]"

**Project:** Knowledge worker assistant — RAG pipeline over a corpus of company documents, deployed as a Gradio UI with conversation history.

---

### Day 4: RAG Evaluation

**Learning Objectives:**
- Build a golden test dataset of question-answer pairs
- Compute MRR and nDCG for retrieval quality
- Use LLM-as-judge to evaluate answer quality
- Iterate on chunking and embedding model choice based on eval results

**LLM Concepts Covered:**
- **Why RAG evaluation is hard**: The "right answer" is often subjective. Standard NLP metrics (BLEU, ROUGE) don't capture semantic correctness. You need LLM-based or human evaluation for answer quality.
- **Retrieval metrics**:
  - **MRR (Mean Reciprocal Rank)**: For each query, finds the rank of the first correct document (1/rank). Averages across queries. Score of 1.0 = always retrieves correct doc first.
  - **nDCG (Normalized Discounted Cumulative Gain)**: Rewards finding correct documents early, penalizes them at lower ranks. Better than MRR when multiple relevant docs exist.
- **Golden dataset**: A hand-curated set of (question, ground-truth answer, ground-truth relevant chunks) triples. Used as the reference for both retrieval and generation evaluation.
- **LLM-as-judge**: Use a strong model (GPT-4o or Claude) to score the RAG system's answers against the golden answers. Prompt: "Given this ground truth answer and this generated answer, rate the generated answer 1-5 for correctness and completeness." More scalable than human evaluation.
- **Structured outputs with Pydantic**: Use Pydantic models + OpenAI's structured output mode to force LLM-as-judge to return `{"score": int, "reasoning": str}` — avoids parsing fragile free-text scores.
- **Iterating on RAG**: Eval scores guide which knobs to turn: chunk size, overlap, embedding model, top-k, re-ranking, query rewriting.

**Project:** RAG evaluation harness with golden dataset, MRR/nDCG retrieval metrics, and LLM-as-judge generation scoring.

---

### Day 5: Advanced RAG Techniques

**Learning Objectives:**
- Apply semantic chunking (split at topic boundaries using an LLM)
- Use query expansion to retrieve from multiple angles
- Apply cross-encoder re-ranking to improve retrieval precision
- Describe GraphRAG and when it outperforms dense retrieval

**LLM Concepts Covered:**
- **Semantic chunking**: Instead of splitting by character count, use an LLM or embedding similarity to detect topic shifts. Produces chunks that are semantically coherent. More expensive but significantly better retrieval quality for complex documents.
- **Query expansion**: Rewrite the user's query into 3-5 different phrasings (using an LLM), embed all variants, retrieve for each, and merge/deduplicate results. Addresses vocabulary mismatch: different phrasings → different retrieved chunks → more robust coverage.
- **Re-ranking with cross-encoders**: First-stage retrieval (vector search) is fast but approximate. A cross-encoder model takes (query, document) pairs and scores their relevance jointly — much more accurate than cosine similarity but too slow for full corpus search. Apply re-ranking to the top-k retrieved candidates. Models: `ms-marco-MiniLM-L-6-v2`, Cohere reranker API.
- **GraphRAG**: Builds a knowledge graph over the document corpus (entities + relationships). Enables queries requiring multi-hop reasoning ("what is the relationship between X and Y?") that dense retrieval struggles with. More complex to implement; best for highly connected factual domains.
- **Results**: Course showed improving MRR from 0.73 to 0.91 by combining semantic chunking + query expansion + re-ranking + better embedding model.

**Project:** Advanced RAG knowledge worker — beats the baseline RAG system significantly on held-out eval set.

---

## Week 6: Fine-Tuning a Frontier Model

### Day 1: Training Fundamentals + Dataset Curation

**Learning Objectives:**
- Distinguish pre-training, fine-tuning, and RLHF in the LLM training pipeline
- Understand generalization vs. overfitting in the context of LLMs
- Curate a dataset from HuggingFace for a specific fine-tuning task
- Understand why dataset quality matters more than quantity

**LLM Concepts Covered:**
- **Pre-training vs. fine-tuning**: Pre-training = training from scratch on billions of tokens to build a base model (done by frontier labs, costs $100M+). Fine-tuning = additional training on a smaller, task-specific dataset to specialize the model. Fine-tuning adjusts existing weights, doesn't learn entirely new capabilities.
- **Supervised Fine-Tuning (SFT)**: The most common fine-tuning approach. Provide (input, desired output) pairs. Train the model to maximize likelihood of the desired output given the input. For LLMs: (prompt, ideal response) pairs.
- **When fine-tuning beats RAG**: Fine-tuning is better when the task requires a specific style, format, or reasoning pattern that can't easily be provided via prompting. RAG is better when the knowledge is dynamic or domain-specific factual information. Rule of thumb: "Prompt engineering and RAG solve 80% of what people think needs fine-tuning."
- **Data curation**: The art of assembling high-quality training data. Filtering for quality (removing duplicates, outliers, bad examples), balancing distributions, ensuring diversity. For the Price Is Right project: Amazon product descriptions → price prediction. Curating from raw Amazon data on HuggingFace.
- **Dataset distribution analysis**: Understanding the statistical properties of your training data before training. Are prices normally distributed? Are there outliers? Weighted sampling to balance categories.

**Project:** "The Price Is Right" — predict the price of an Amazon product from its description. Serves as the capstone project across Weeks 6-8.

---

### Day 2: Data Preprocessing with LLMs + Batch Processing

**Learning Objectives:**
- Use an LLM to evaluate and clean training data (LLM-as-data-curator)
- Use Groq batch API for cheap high-throughput LLM calls (22K requests for under $1)
- Structure batch jobs with JSONL format
- Apply the five-step AI process framework to a business problem

**LLM Concepts Covered:**
- **LLMs for data preprocessing**: LLMs can assess whether a training example is well-formed, relevant, and high-quality. More nuanced than rule-based filtering. For Price Is Right: use an LLM to assess whether a product description contains enough information to reasonably estimate a price.
- **Groq batch mode**: Asynchronous batch processing API. Submit a JSONL file of requests, Groq processes them (potentially overnight), return results as JSONL. Dramatically cheaper than synchronous real-time calls. Used for large-scale dataset preprocessing where latency doesn't matter.
- **Five-step AI process**: (1) Define the business problem clearly. (2) Collect and curate data. (3) Establish baselines (simple models first). (4) Apply progressively more sophisticated models. (5) Evaluate against business metrics, not just ML metrics.

**Project:** Data preprocessing pipeline — use Groq batch API to quality-filter 100K Amazon product descriptions for training.

---

### Day 3: Baseline Models — Traditional ML

**Learning Objectives:**
- Implement random baseline, linear regression, and Random Forest/XGBoost on the price prediction task
- Use CountVectorizer for bag-of-words text features
- Understand why baselines are essential before reaching for expensive LLMs
- Measure error with appropriate metrics (MAE, % error)

**LLM Concepts Covered:**
- **Baseline philosophy**: Always build the simplest possible model first. If a linear regression beats an LLM fine-tuned for a week, you wasted the week. Baselines also tell you how hard the problem is and give you a performance floor.
- **Bag of words for text**: CountVectorizer converts product descriptions to sparse word-count vectors. Combined with linear regression: surprisingly effective. Establishes that the task is learnable from text without any LLM.

**Project:** Baseline model suite — random predictor, linear regression, Random Forest, and XGBoost on price prediction.

---

### Day 4: Neural Networks + Testing Frontier Models on Price Prediction

**Learning Objectives:**
- Build a feedforward neural network in PyTorch for price prediction
- Understand why neural networks require non-linearity
- Test GPT-4o-mini, Claude Opus, and Gemini 3 zero-shot on price prediction
- Compare ML model performance to frontier model zero-shot performance

**LLM Concepts Covered:**
- **Why frontier models struggle at price prediction zero-shot**: Price prediction requires memorizing a vast number of specific product prices — exactly the kind of factual memorization that LLMs don't do well. They can reason about relative prices but not exact ones without training.
- **Neural network for tabular/text data**: Embedding layer → dense layers → ReLU → output neuron. For text: embed the tokens, pool, then dense layers. Training with Adam optimizer, MSE loss.
- **Human baseline**: Asking actual humans to predict prices from descriptions. Establishes a realistic ceiling. Demonstrates that even humans can't perfectly price products from descriptions alone — sets expectation for what models can achieve.

**Project:** PyTorch neural network for price prediction + frontier model zero-shot comparison.

---

### Day 5: Fine-Tuning GPT-4o (Frontier Fine-Tuning)

**Learning Objectives:**
- Use OpenAI's fine-tuning API to train a custom GPT model
- Format training data as JSONL with the chat completion format
- Monitor fine-tuning runs via OpenAI's dashboard
- Understand why fine-tuning can make a model worse (forgetting, overfitting)
- Know when to use a deep custom NN instead of a fine-tuned frontier model

**LLM Concepts Covered:**
- **OpenAI fine-tuning API**: Submit a JSONL file where each line is a complete chat completion example `{messages: [{role, content}, ...]}`. OpenAI trains a private copy of the base model on your data. You get a custom model ID to call like any other model.
- **Catastrophic forgetting**: Fine-tuning on a narrow dataset can cause the model to "forget" its general capabilities. A fine-tuned model might be worse at price prediction than the base model if the training data isn't representative or the fine-tuning runs too long.
- **When fine-tuning fails**: Fine-tuning a frontier model on price prediction in this course *made the model worse*. The base model's strong priors about prices conflicted with the specific patterns in the training data. Lesson: fine-tuning is not always the right tool.
- **Deep NN as alternative**: A custom deep neural network (289M parameters, purpose-built for this task) significantly outperformed both the base frontier model and the fine-tuned frontier model. Task-specific architecture beats general fine-tuning when you have enough data.
- **Cross-entropy loss**: For LLMs generating a price (as text), the training loss is cross-entropy over the token probability distribution. A lower loss means the model more confidently predicts the correct price tokens.

**Project:** Fine-tuned GPT-4o-nano on price prediction + comparison against baseline models and the custom deep NN.

---

## Week 7: Fine-Tuning an Open-Source Model with QLoRA

### Day 1: LoRA and QLoRA — Parameter-Efficient Fine-Tuning

**Learning Objectives:**
- Explain why full fine-tuning of a 7B+ model is impractical on consumer hardware
- Describe LoRA's low-rank decomposition approach
- Understand QLoRA as LoRA + 4-bit quantization of the base model
- Calculate the number of trainable parameters added by LoRA

**LLM Concepts Covered:**
- **Why full fine-tuning is impractical**: A 7B model at 16-bit precision = 14GB for weights + gradients + optimizer states ≈ 60GB+ GPU VRAM during training. No consumer GPU can handle this. Even A100 (40GB) struggles with 13B models.
- **LoRA (Low-Rank Adaptation)**: Instead of updating all parameters, add small trainable weight matrices alongside each attention/FFN layer. If original weight matrix W is (d × d), LoRA adds W_A (d × r) and W_B (r × d) where r << d (typically r=8 or r=16). The effective update is W + W_A × W_B. Trains only W_A and W_B — a tiny fraction of total parameters. During inference, merge: W_new = W + W_A × W_B.
- **LoRA rank (r)**: The rank of the low-rank decomposition. r=8: ~0.1% of parameters trainable. r=64: more expressive but more memory. Lower r → less memory, less expressive. Higher r → more expressive, approaches full fine-tuning.
- **LoRA alpha (α)**: A scaling factor that controls the magnitude of the LoRA updates relative to the original weights. Typically set to 2× the rank. Effectively a learning rate for the LoRA component.
- **Target modules**: Which layers to apply LoRA to. Common choices: all attention projection matrices (Q, K, V, O), sometimes MLP layers too. More modules → more expressive but more memory.
- **QLoRA**: LoRA + 4-bit quantization of the base model weights during training. The base model is quantized to 4-bit (NF4 format) to save memory. Only the LoRA adapters are trained in 16-bit precision. Enables fine-tuning of 7B models on a single T4 GPU (15GB VRAM).
- **bitsandbytes**: HuggingFace library that implements quantization. `load_in_4bit=True` or `load_in_8bit=True` in `from_pretrained()`.
- **Parameter count example**: LLaMA 3.2 3B model: ~3 billion parameters. With LoRA r=16 on all attention layers: ~3-5 million trainable parameters. That's 0.1% of the model.

**Project:** QLoRA theory and setup — configure a QLoRA training environment on Google Colab.

---

### Day 2: Dataset Preparation for Fine-Tuning

**Learning Objectives:**
- Format data as prompt-completion pairs for SFT
- Handle token length limits during dataset preparation
- Understand the difference between fine-tuning a base model vs. an instruct model
- Use HuggingFace Datasets library for preprocessing

**LLM Concepts Covered:**
- **Fine-tuning data format**: Each example: a prompt (product description formatted as a user message) + completion (the price as the assistant's response). For open-source models, need to apply the model's chat template to convert this to token IDs with appropriate special tokens.
- **Base vs. instruct model for fine-tuning**: Fine-tuning a base model gives you more control (you define the conversation format from scratch). Fine-tuning an instruct model leverages its existing conversational capabilities. For this task: fine-tuning a base model is better because you want the model to simply output a number, not engage in conversation.
- **Token length considerations**: Training examples that exceed the model's max sequence length must be truncated or filtered. For price prediction: short prompts + short completions → most examples fit easily.
- **Data splitting**: Train/validation/test split. Validation set used for monitoring during training (loss curves). Test set held out for final evaluation. Shuffling essential to avoid ordering biases.

**Project:** Dataset preparation pipeline — format 800K Amazon examples as SFT pairs for LLaMA fine-tuning.

---

### Day 3: Fine-Tuning Hyperparameters and Weights & Biases

**Learning Objectives:**
- Configure QLoRA hyperparameters (rank, alpha, target modules, dropout)
- Set training hyperparameters (learning rate, batch size, warmup, epochs)
- Use Weights & Biases for experiment tracking and visualization
- Set up HuggingFace SFTTrainer for fine-tuning

**LLM Concepts Covered:**
- **Learning rate for fine-tuning**: Typically much lower than pre-training (e.g., 2e-4 to 1e-5). Too high → catastrophic forgetting or divergence. Too low → no learning. Warmup schedule: linearly increase LR for the first N steps, then decay.
- **Gradient accumulation**: When GPU memory limits batch size to 1-2, accumulate gradients over multiple forward passes before updating weights. Simulates a larger effective batch size.
- **Weights & Biases (W&B)**: Experiment tracking platform. Logs training/validation loss, learning rate, gradient norms, custom metrics in real time. Enables comparison of multiple runs. Essential for serious fine-tuning work. `wandb.init(project="price-prediction")` in training code.
- **SFTTrainer** (from TRL): HuggingFace's supervised fine-tuning trainer. Handles gradient accumulation, mixed precision, LoRA integration, W&B logging, checkpointing. Simplifies the training loop significantly.
- **Mixed precision training**: Compute forward/backward passes in 16-bit (faster, less memory), store weights in 32-bit (stable). `bf16=True` or `fp16=True` in TrainingArguments.
- **Checkpointing**: Save model weights periodically during training. Allows resuming interrupted runs and selecting the best checkpoint based on validation loss.

**Project:** Configure and launch a QLoRA training run on LLaMA 3.2, with W&B tracking.

---

### Day 4: Running the Fine-Tuning Run + Monitoring

**Learning Objectives:**
- Execute a complete QLoRA fine-tuning run on 800K data points
- Interpret training and validation loss curves
- Identify overfitting from diverging train/val curves
- Select the best model checkpoint using W&B

**LLM Concepts Covered:**
- **Training loss interpretation**: Should steadily decrease. If it plateaus early → learning rate too low or model has already learned the pattern. If it spikes → learning rate too high or bad data.
- **Overfitting detection**: Training loss continues decreasing but validation loss stops decreasing or increases. Solution: stop training earlier, use more data, add regularization (dropout in LoRA layers).
- **LoRA dropout**: Adding dropout to LoRA adapter layers to reduce overfitting. Regularizes the adapter without affecting the frozen base model.
- **Gradient norm tracking**: W&B logs gradient norms. Large norms → training instability. Gradient clipping (max_grad_norm=1.0) prevents explosions.
- **A100 vs T4**: The full 800K example training run requires an A100 (40GB VRAM). The T4 (15GB, free) can handle smaller runs. Cost: ~$2-4/hour for A100 on Colab. A full training run: several hours → $10-20 total.

**Project:** Full QLoRA training run on Google Colab A100, monitoring loss curves and gradient norms in W&B.

---

### Day 5: Results — Fine-Tuned LLaMA vs Frontier Models

**Learning Objectives:**
- Run inference on the fine-tuned QLoRA model
- Calculate cross-entropy loss as an LLM evaluation metric
- Compare fine-tuned LLaMA 3.2 performance against GPT-5.1, Claude, and other frontier models
- Understand why a fine-tuned small model can outperform frontier models on narrow tasks

**LLM Concepts Covered:**
- **Cross-entropy loss as evaluation**: For a model predicting a price (e.g., "$129.99"), each token in the price string is evaluated. The model's probability assigned to the correct token, averaged across all tokens and examples, gives the cross-entropy loss. Lower = better calibration.
- **The shocking result**: A fine-tuned LLaMA 3.2 (3B parameters, fine-tuned with QLoRA on the Amazon price dataset) **outperforms GPT-5.1, Claude 4.5, and all frontier models** on this specific task. Demonstrates the power of task-specific fine-tuning.
- **Why this happens**: Frontier models were never trained specifically to predict Amazon prices. The fine-tuned LLaMA was shown 800K examples of (product description → price) pairs. It has internalized the price patterns in this corpus in a way no frontier model can match without similar training.
- **Lesson for practitioners**: Identify a narrow, well-defined task with available training data → fine-tune a small open-source model → can outperform expensive frontier models while running cheaper and locally.

**Project:** Evaluation of fine-tuned LLaMA 3.2 vs. all baselines and frontier models on the held-out test set.

---

## Week 8: Building Autonomous Multi-Agent Systems

### Day 1: Agentic AI Architecture + Modal Serverless Deployment

**Learning Objectives:**
- Design a multi-agent architecture for a commercial problem
- Deploy Python functions as serverless cloud functions using Modal
- Store and retrieve model weights persistently in Modal's cloud storage
- Understand the difference between agent orchestrators and worker agents

**LLM Concepts Covered:**
- **Agentic AI (formal definition)**: A system with an LLM in a loop with access to tools. The LLM decides what to do next — call a tool, call another agent, or return an answer. Key properties: autonomy (the LLM controls the workflow), persistence (the loop continues until a goal is met), tool access (the LLM can take actions, not just generate text).
- **Agent architectures**: (1) Single agent with many tools. (2) Orchestrator agent that calls specialist worker agents. (3) Multi-agent pipeline where output of one agent feeds the next. (4) Hierarchical: manager agent orchestrates sub-managers orchestrating workers.
- **Modal**: A serverless Python platform. Decorate a function with `@app.function()` to deploy it to the cloud. Supports GPU instances, persistent volume storage, scheduled runs. The fine-tuned LLaMA model is deployed to Modal so it can be called remotely without running it locally.
- **Serverless**: Functions spin up on demand, you pay per second of execution. No always-on server cost. Ideal for agent tools that are called infrequently.

**Project:** Deploy the fine-tuned LLaMA model as a serverless Modal function with persistent weight storage.

---

### Day 2: Advanced RAG + Ensemble Models

**Learning Objectives:**
- Build RAG directly with ChromaDB (no LangChain dependency)
- Combine RAG + fine-tuned model + neural network in an ensemble
- Visualize embedding clusters with t-SNE to validate indexing quality
- Understand ensemble methods for LLM-based systems

**LLM Concepts Covered:**
- **Ensemble approach**: Combine predictions from multiple models — RAG-augmented GPT-4o, the fine-tuned LLaMA 3.2, and the deep neural network. Average or weighted average their predictions. Reduces variance and improves robustness. Classic ML technique applied to LLM systems.
- **RAG without LangChain**: Using ChromaDB directly (without LangChain wrapper). More code, more control. Shows that LangChain is a convenience layer, not a requirement.
- **t-SNE visualization of embeddings**: Projecting 1536-dimensional embedding vectors to 2D. Clusters of similar products should appear nearby. Validates that the embedding model is capturing meaningful semantic structure in the product data.

**Project:** Ensemble price predictor combining RAG + fine-tuned LLaMA + deep NN, with t-SNE embedding validation.

---

### Day 3: Structured Outputs + Scanning Agent

**Learning Objectives:**
- Define Pydantic models to enforce LLM output schemas
- Use OpenAI's structured outputs API (JSON Schema enforcement during inference)
- Build a deal scanner agent that identifies underpriced products
- Send push notifications when deals are found

**LLM Concepts Covered:**
- **Structured outputs**: A stronger version of `response_format={"type": "json_object"}`. You define a Pydantic model (Python class), and OpenAI converts it to a JSON Schema. At inference time, token sampling is constrained so the output always matches the schema exactly. No parsing failures, no missing fields.
- **Constrained decoding**: The mechanism behind structured outputs. During token sampling, a finite state machine tracks which tokens are valid at each position given the schema. Only schema-valid tokens are assigned non-zero probability. Guarantees valid structured output every time.
- **Agent as a scanner**: The deal scanner agent runs on a schedule (Modal cron), fetches new Amazon products, predicts their "fair price" using the ensemble, compares to listed price, and alerts via Pushover if the listed price is significantly below the predicted price. A fully autonomous agent loop.

**Project:** Autonomous deal scanner agent with push notifications, running on a Modal cron schedule.

---

### Day 4: Planning Agents and Multi-Agent Orchestration

**Learning Objectives:**
- Implement a planning agent that decomposes a task into sub-tasks using tool calling
- Build a multi-agent system with 34 LLM calls across GPT-5, Claude, and open-source models
- Understand the ReAct (Reason + Act) agent pattern
- Measure the full cost of a complex agentic workflow

**LLM Concepts Covered:**
- **Planning agents**: An LLM given a high-level goal and a set of tools. It plans a sequence of tool calls to achieve the goal. Uses chain-of-thought to reason about what to do next, calls a tool, observes the result, reasons about the next step. Continues until the goal is achieved.
- **ReAct pattern**: Reason → Act → Observe → Reason → Act… A loop where the agent alternates between reasoning (generating thoughts) and acting (calling tools). The reasoning tokens help the model stay on track and avoid dead ends.
- **Tool as LLM call**: Tools can themselves be LLM calls. The orchestrator calls a "specialist agent" tool, which is another LLM prompt optimized for a specific subtask. Enables hierarchical agent architectures.
- **34 LLM calls in one workflow**: The final Price Is Right platform combines: orchestrator agent (GPT-5) + RAG retriever + fine-tuned LLaMA (on Modal) + deep NN + frontier model comparisons (Claude, Gemini) + deal scanner + structured output parser. Total: 34 LLM calls per product evaluation.
- **Agentic loop cost management**: Agent loops can eat through API budgets rapidly. Importance of: (1) choosing the cheapest model sufficient for each subtask, (2) caching repeated retrieval calls, (3) monitoring spend per workflow run.

**Project:** Multi-agent orchestrator with ReAct planning, specialist sub-agents, and cost tracking.

---

### Day 5: Finalizing the Agentic Platform + Course Wrap-Up

**Learning Objectives:**
- Integrate all components into a Gradio UI for the Price Is Right agent
- Articulate the complete LLM engineering stack you've built
- Position yourself to keep learning: RAG improvements, new models, new agentic frameworks

**LLM Concepts Covered:**
- **The complete LLM engineer's toolkit**: APIs (OpenAI, Anthropic, Gemini, DeepSeek, Groq), local inference (Ollama, HuggingFace Transformers), UIs (Gradio, Streamlit), frameworks (LangChain, LiteLLM), vector stores (Chroma, FAISS), fine-tuning (QLoRA, SFTTrainer), experiment tracking (W&B), deployment (Modal), evaluation (MRR, nDCG, LLM-as-judge), agents (tool calling, planning, multi-agent).
- **The arc of the course**: Each week's techniques are inference-time scaling (prompt engineering, RAG) or training-time scaling (fine-tuning). Both tracks matter. The best systems combine them.

**Project:** Complete "Price Is Right" multi-agent system — end-to-end product price prediction platform combining RAG, fine-tuned LLaMA, deep NN, frontier models, structured outputs, deal scanning, push notifications, and a Gradio UI. Over 34 LLM calls per evaluation.

---

*End of outline. Total: 8 weeks, 5 days each, covering the full arc from first API call to autonomous multi-agent commercial system.*
