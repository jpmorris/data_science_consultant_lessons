# %% [markdown]
# ## GenAI Products in AWS
# - Sagemaker Bedrock - Managed service, higher-level, less-control
# - Sagemaker Jumpstart - Lower-level, more control, more flexibility 

# %% [markdown]
# ## Big question that we always should ask:
# ### Should we even do this?
# There is a tendency to take the most avant-garde technology and apply it to 
# an organization. Our data may not be robust enough, the technology not advanced
# enough, or the organization not ready enough. 
#
#
# Fine-tuned (therefor not a general model) LLMs cant currently (if ever) outperform a 
# other 
# %% [markdown]
# ## Some use Cases for in-house GenAI for a federal oversight agency
# Naive, but desirable prompts:
# - 'Where is fraud happening in my agency?' - Fraud signal is too weak to 
# - 'What are the common connections between two auditees?' -
# - 'How many findings of an audit were there for type X' - 
# detect fraud so easily, 
# By ingesting audit data: 
# - Generating summaries
# - Generating reports from audit data
# - Generating responses to common inquiries
#
#  

# %%
# # Steps to fine-tune a LLM with custom data for an organization
# 1. Obtain pre-trained model
# 1. Prepare custom data for fine-tuning
#   - Fine-tuning data is blocks of text
# 1. Test the model
