---
layout: page
title: Jobnet Scraper
description: Automated job scraper and LLM-based matcher for Jobnet.dk — scrapes postings by keyword and scores each one against your profile.
img: assets/img/projects/scraper_jobnet.png
importance: 2
category: work
related_publications: false
---

<div class="row justify-content-sm-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/scraper_jobnet.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
</div>

## Overview

Automated job scraper and LLM-based matcher for [Jobnet.dk](https://jobnet.dk). Scrapes postings by keyword, scores each one against your profile and example references, and saves a ranked report of the best matches.

## How it works

1. **Scrape** — Playwright fetches job postings from Jobnet.dk for each configured keyword, intercepting the XHR API responses to extract structured data.
2. **Evaluate** — Each job is sent to an LLM with your personal profile and example good postings as context. The model returns a match decision, a score (1–10), and a short reason.
3. **Report** — Matches above the minimum score threshold are ranked and saved to a dated markdown report.

## Stack

- **Playwright** — headless browser scraping with XHR interception
- **Claude / OpenAI / Ollama** — LLM backend for job matching
- **uv** — fast Python package management
- **Python 3.12**

## Usage

```bash
# Run with local Ollama model
uv run python src/pipeline.py

# Run with Claude, stricter score threshold
uv run python src/pipeline.py --llm anthropic --min-score 7

# Run with OpenAI, more results per keyword
uv run python src/pipeline.py --llm openai --max 40
```

| Option | Default | Description |
|---|---|---|
| `--llm` | `local` | Backend: `local` (Ollama), `anthropic`, or `openai` |
| `--model` | — | Override the default model for the chosen backend |
| `--max` | `20` | Max job postings scraped per keyword |
| `--min-score` | `6` | Minimum LLM score (1–10) to include in report |

## Keywords

Searches are driven by a configurable keyword list:

```python
KEYWORDS = [
    "Data science",
    "Machine Learning",
    "Bioinformatics",
    "Machine learning engineer",
]
```

## Repository

The full code is available on [GitHub](https://github.com/AntonWangDTU/jobnet_scraper).
