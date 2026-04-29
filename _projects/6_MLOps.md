---
layout: page
title: "❤️ Heart Disease Predictor 💔"
description: A live heart disease prediction service — FastAPI backend deployed on Railway, called in real-time from this page via TypeScript.
img: assets/img/projects/MLOps.jpg
importance: 1
category: work
related_publications: false
---

## Live Demo

<div style="background: var(--global-bg-color); border: 1px solid var(--global-divider-color); border-radius: 8px; padding: 1.5rem; margin-bottom: 2rem;">
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
    <div>
      <label style="display:block; font-size:0.85rem; margin-bottom:0.25rem;">Age</label>
      <input id="age" type="number" value="55" min="1" max="120" style="width:100%; padding:0.4rem; border-radius:4px; border:1px solid var(--global-divider-color); background:var(--global-bg-color); color:var(--global-text-color);">
    </div>
    <div>
      <label style="display:block; font-size:0.85rem; margin-bottom:0.25rem;">Sex (0=F, 1=M)</label>
      <input id="sex" type="number" value="1" min="0" max="1" style="width:100%; padding:0.4rem; border-radius:4px; border:1px solid var(--global-divider-color); background:var(--global-bg-color); color:var(--global-text-color);">
    </div>
    <div>
      <label style="display:block; font-size:0.85rem; margin-bottom:0.25rem;">Chest Pain Type (0–3)</label>
      <input id="cp" type="number" value="1" min="0" max="3" style="width:100%; padding:0.4rem; border-radius:4px; border:1px solid var(--global-divider-color); background:var(--global-bg-color); color:var(--global-text-color);">
    </div>
    <div>
      <label style="display:block; font-size:0.85rem; margin-bottom:0.25rem;">Resting BP (mmHg)</label>
      <input id="trestbps" type="number" value="130" style="width:100%; padding:0.4rem; border-radius:4px; border:1px solid var(--global-divider-color); background:var(--global-bg-color); color:var(--global-text-color);">
    </div>
    <div>
      <label style="display:block; font-size:0.85rem; margin-bottom:0.25rem;">Cholesterol (mg/dl)</label>
      <input id="chol" type="number" value="250" style="width:100%; padding:0.4rem; border-radius:4px; border:1px solid var(--global-divider-color); background:var(--global-bg-color); color:var(--global-text-color);">
    </div>
    <div>
      <label style="display:block; font-size:0.85rem; margin-bottom:0.25rem;">Max Heart Rate</label>
      <input id="thalach" type="number" value="150" style="width:100%; padding:0.4rem; border-radius:4px; border:1px solid var(--global-divider-color); background:var(--global-bg-color); color:var(--global-text-color);">
    </div>
    <div>
      <label style="display:block; font-size:0.85rem; margin-bottom:0.25rem;">Exercise Angina (0=No, 1=Yes)</label>
      <input id="exang" type="number" value="0" min="0" max="1" style="width:100%; padding:0.4rem; border-radius:4px; border:1px solid var(--global-divider-color); background:var(--global-bg-color); color:var(--global-text-color);">
    </div>
  </div>
  <button id="heart-submit" style="margin-top:1rem; padding:0.5rem 1.5rem; border-radius:4px; border:none; background:#e74c3c; color:white; font-size:1rem; cursor:pointer;">Predict</button>
  <div id="heart-result"></div>
</div>

<script src="/assets/js/heart-predictor.js"></script>

## Overview

A heart disease risk prediction service — trained with scikit-learn, served via FastAPI, containerized with Docker, and deployed to the cloud. The live demo above runs against a real API endpoint hosted on Railway, called directly from this page using TypeScript.

The model takes 7 patient features and returns a binary prediction (high/low risk) along with a probability score.

## Architecture

This project is fully deployed end-to-end:

- The **FastAPI** backend runs in a Docker container on **Railway**, exposed as a public HTTPS endpoint
- This website calls the API via **TypeScript** (`fetch`) — no middleman, no mock data
- The frontend form is embedded directly in this page and sends real POST requests to the live service

## Stack

- **FastAPI** — REST API (`/predict` endpoint)
- **Docker** — containerized for reproducible deployment
- **Railway** — cloud hosting with automatic deploys from GitHub
- **scikit-learn** — logistic regression model trained on the Cleveland Heart Disease dataset
- **TypeScript** — frontend form compiled to JS, served via GitHub Pages
- **Python 3.12**

## Repository

The full code is available on [GitHub](https://github.com/AntonWangDTU/MLOps_HeartR).

## Running Locally
<div class="row justify-content-sm-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/HeartR.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
</div>

### With Docker (recommended)

1. Clone the repository:
```bash
git clone https://github.com/AntonWangDTU/MLOps_HeartR
cd MLOps_HeartR
```

2. Build the image:
```bash
docker build -t heart-predictor .
```

3. Run the container:
```bash
docker run -p 8000:8000 heart-predictor
```

4. Open [http://localhost:8000](http://localhost:8000) in your browser.

### Without Docker

Requires Python 3.12. Install dependencies with `uv` and run:

```bash
uv sync
uv run uvicorn src.mlops_ha.api:app --host 0.0.0.0 --port 8000
```
