# The Great Data Scientist in the Age of AI — Slides

Quarto revealjs presentation covering what makes a great data scientist in the current AI landscape.

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

Only needs to be done once per machine.

```bash
uv run python -m ipykernel install --user --name ds-ai-industry-slides --display-name "Python (DS AI Industry Slides)"
```

## Preview the Presentation

### Local machine

```bash
uv run quarto preview great-ds-ai-industry-slides.qmd
```

### Remote machine (SSH)

```bash
uv run quarto preview great-ds-ai-industry-slides.qmd --host 0.0.0.0
```

Then open `http://<hostname>:<port>/` in your laptop's browser.

Or use SSH port forwarding:

```bash
# Run on your laptop, then open http://localhost:5694/ in your browser
ssh -L 5694:localhost:5694 <user>@<hostname>
```

### Render to HTML

```bash
uv run quarto render great-ds-ai-industry-slides.qmd
```

## Files

- `great-ds-ai-industry-slides.qmd` - Main Quarto presentation file
- `images/` - Images used in the presentation
