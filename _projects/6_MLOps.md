---
layout: page
title: End-to-end MLOps Pipeline
description: A production-ready machine learning service built with FastAPI and Docker.
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

This project demonstrates a production-ready machine learning pipeline for heart disease risk prediction. The goal was to go beyond model training and build the infrastructure needed to serve and deploy a model in a reproducible, containerized way.

The architecture is designed to be dataset-agnostic and can be adapted to other prediction tasks with minimal changes.

## Stack

- **FastAPI** — REST API for model serving and web interface
- **Docker** — containerization for portable, reproducible deployment
- **scikit-learn** — model training
- **Python 3.12**

## Architecture

The app exposes two interfaces:

1. A **web UI** at the root endpoint for interactive predictions via a browser form
2. A **`/predict` REST endpoint** that accepts a JSON payload and returns a prediction with probability

The entire service runs in a single Docker container and can be started with:
```bash
docker build -t heart-predictor .
docker run -p 8000:8000 heart-predictor
```

## Usage

Once running, the `/predict` endpoint accepts 7 patient features and returns a prediction:
```bash
curl -X POST http://localhost:8000/predict \
  -d "age=55&sex=1&cp=2&trestbps=130&chol=240&thalach=150&exang=0"
```

The web interface is accessible at `http://localhost:8000`.

## Repository

The full code is available on [GitHub](https://github.com/AntonWangDTU/MLOps_HeartR).
