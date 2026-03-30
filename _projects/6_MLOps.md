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
        {% include figure.liquid loading="eager" path="assets/img/projects/MLOps.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
</div>

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
git clone git@github-anton:AntonWangDTU/MLOps_HeartR.git
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
