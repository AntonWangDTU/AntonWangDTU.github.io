---
layout: page
title: End-to-end MLOps Pipeline
description: A production-ready machine learning service built with MLflow, FastAPI, and Docker.
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

This project demonstrates an end-to-end machine learning pipeline with a focus on production readiness. The goal was to go beyond model training and build the infrastructure needed to track, serve, and deploy a machine learning model in a reproducible way.

The project uses heart disease risk prediction as the prediction task, but the architecture is designed to be dataset-agnostic.

## Stack

- **MLflow** — experiment tracking and model registry
- **FastAPI** — REST API for model serving
- **Docker + docker-compose** — containerization and orchestration
- **scikit-learn** — model training
- **Python 3.11**

## Architecture

The pipeline consists of two containerized services orchestrated with docker-compose:

1. An **MLflow tracking server** that logs experiment runs, parameters, metrics, and model artifacts to a persistent local volume
2. A **FastAPI application** that loads the production-stage model from the MLflow registry at startup and exposes a `/predict` endpoint

The entire stack can be started with a single command:

```bash
docker-compose up
```

## Usage

Once running, the `/predict` endpoint accepts a JSON payload and returns a prediction:

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"age": 55, "cholesterol": 240, "trestbps": 130, "thalach": 150}'
```

The MLflow UI is accessible at `localhost:5000` and shows all logged experiment runs.

## Repository

The full code is available on [GitHub](https://github.com/AntonWangDTU/MLOps_project).
