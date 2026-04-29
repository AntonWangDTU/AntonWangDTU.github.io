---
layout: page
title: Heart Disease Predictor
description: A machine learning service for heart disease risk prediction, built with FastAPI and Docker.
img: assets/img/projects/MLOps.jpg
importance: 1
category: work
related_publications: false
---
<div class="row justify-content-sm-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/HeartR.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
</div>

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

A FastAPI application that predicts the risk of heart disease based on patient data, packaged in Docker for easy deployment anywhere.

## Features

Predictions are based on 7 key patient features:

- `age`, `sex`, `cp` (chest pain type), `trestbps` (resting blood pressure), `chol` (cholesterol), `thalach` (max heart rate), `exang` (exercise-induced angina)

The app returns both a prediction and a probability score, and includes a simple web interface for interactive use.

## Stack

- **FastAPI** — REST API and web interface
- **Docker** — containerization for portable deployment
- **scikit-learn** — model training
- **Python 3.12**

## Getting Started

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

4. Open your browser at [http://localhost:8000](http://localhost:8000) to use the web interface.

### Without Docker

Requires Python 3.12 installed locally. Install dependencies and run the app directly.

## Repository

The full code is available on [GitHub](https://github.com/AntonWangDTU/MLOps_project).

## How to use

1. **Insert your values** 

<div class="row justify-content-sm-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/HeartR1.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
</div>

2. **Press predict** 


<div class="row justify-content-sm-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/HeartR2.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
</div>


3. **View your patients risk of having heart disease** 


<div class="row justify-content-sm-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/HeartR3.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
</div>

