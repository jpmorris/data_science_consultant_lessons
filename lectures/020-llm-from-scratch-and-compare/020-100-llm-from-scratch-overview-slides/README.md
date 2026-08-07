# LLM from Scratch Overview - PowerPoint Lecture

This directory contains a Quarto presentation on building LLMs from scratch

## Setup

### 1. Install Quarto CLI (Arch Linux)

```bash
yay -S quarto-cli-bin
```

### 2. Install Python dependencies

```bash
uv sync
```

### 3. Register the Jupyter kernel

This registers the project's uv venv as the kernel quarto uses to execute code cells.
Only needs to be done once per machine.

```bash
uv run python -m ipykernel install --user --name llm-slides --display-name "Python (LLM Slides)"
```

## Preview the Presentation

### Local machine

```bash
uv run quarto preview llm-from-scratch-overview-slides.qmd
```

### Remote machine (SSH)

Bind to all interfaces so the port is reachable from your laptop:

```bash
uv run quarto preview llm-from-scratch-overview-slides.qmd --host 0.0.0.0
```

Then open `http://<hostname>:<port>/` in your laptop's browser.

Or use SSH port forwarding to avoid exposing the port:

```bash
# Run on your laptop, then open http://localhost:5694/ in your browser
ssh -L 5694:localhost:5694 <user>@<hostname>
```

### Render to HTML

```bash
uv run quarto render llm-from-scratch-overview-slides.qmd
```

## Files

- `llm-from-scratch-overview-slides.qmd` - Main Quarto presentation file
- `images/` - Images used in the presentation
