# AWS Data Science Services and SAP SO2

This is a review of some AWS Data Science Services which overlap with the SAP SO2 exam - AWS
Certified Solutions Architect - Professional.

Much of this material comes from Stephane Maarek's course on Udemy - Ultimate AWS Certified
Solutions ARchitect Associate 2025.

# Rekognition

![AWS Recognition](images/aws_rekognition.png)
![Recognition Modalities](images/rekognition_modalities.png)
![Rekognition - Content Moderation](images/rekognition_content_moderation.png)

# Transcribe

![AWS Transcribe](images/aws_transcribe.png)

- Google's version: Speech

# Polly

![AWS Polly](images/aws_polly.png) ![AWS Polly](images/aws_polly_lexicon_ssml.png)

- Google's version: Speech

# Translate

![AWS Translate](images/aws_translate.png)

# Lex+Connect

![AWS Lex+Connect](images/aws_lex_connect.png)

# Comprehend

![AWS Comprehend](images/aws_comprehend.png)
![AWS Comprehend Medical](images/aws_comprehend_medical.png)

# Sagemaker

![AWS Sagemaker](images/aws_sagemaker.png)

## Sagemaker sub-services

### Notebook Instances

### Studio

- Jupyterlab
- RStudio
- Canvas - no code ML ![Sagemaker Canvas](images/sagemaker_canvas.png)

  - 3 environments with flexibility/knowledge tradeoff - Canvas - no code - Sagemaker
    off-the-shelf/managed containers - Sagemaker custom containers
  - was 'AutoPilot'
  - under the 'Auto ML' link in studio

![Sagemaker Use Cases](images/sagemaker_use_cases.png)

- Code Editor - VS Code web-based editor
- MLFlow ![Sagemaker Mlflow](images/sagemaker_mlflow.png)

### Ground Truth

Ground Truth is a data labeling service that makes it easy to build highly accurate training
datasets for machine learning. You can use Ground Truth to create labeled training data for image,
text, and 3D point cloud data.

The service allows designing labeling ui, creating labeling workflows for internal employees or
hiring external workers directly through amazon like mechanical turk.

### "Experiments" in Studio

- AWS UI Abstraction in Studio for MLFlow.
  - Alternative tracker is Weights and Biases (wandb)

### Pipelines

### Models

- Create, Register, deploy, monitor, and manage models

![AWS Forecast](images/sagemaker_models.png)

### Jumpstart

![AWS Forecast](images/sagemaker_jumpstart.png)

# Forecast

![AWS Forecast](images/aws_forecast.png)

# Kendra

![AWS Kendra](images/aws_kendra.png)

# Personalize

![AWS Personalize](images/aws_personalize.png)

# Textrack

![AWS Textrack](images/aws_textract.png)

# Bedrock

- Fully managed
- Allows for (easier?) serverless deployment of ML models

![AWS Bedrock](images/aws_bedrock.png)

# Amazon Q

AI Assistant
