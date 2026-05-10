---
layout: page
title: IBIS Field Trial Tracker
description: A research data management dashboard for the IBIS project — tracking field experiments, ETL pipeline status, and data quality across international partners.
importance: 1
category: work
related_publications: false
---

<div style="margin-bottom: 1.5rem;">
  <a href="/ibis-tracker/" class="btn btn-primary" style="font-size:0.95rem;">
    🌱 Open Live Demo
  </a>
</div>

## Overview

A prototype data stewardship dashboard built for the [IBIS Project](https://www.bioengineering.dtu.dk/) (Initiative for Biotertilizer Innovation and Science) at DTU Bioengineering.

The IBIS project develops next-generation microbial biofertilizers through data-driven approaches across partners in Europe, Africa, and Asia. A key challenge is ensuring that experimental data from heterogeneous field sites can be captured, cleaned, and made analysis-ready in a traceable way.

This app demonstrates what a lightweight data steward tool could look like — covering experiment registration, ETL pipeline monitoring, and data quality reporting.

## Features

- **Partner pipeline status** — visual Extract → Transform → Load status per country partner (Denmark, Kenya, India, Brazil)
- **Data quality alerts** — surfaces real issues found during ETL: date format mismatches, decimal separator differences, unit conversions, duplicate rows, unknown strain codes
- **Experiment registry** — searchable and filterable table of all registered field trials
- **Yield comparison chart** — inoculated vs. control across partner sites
- **Log new experiment** — form for registering a new field trial into the system

## ETL pipeline

The data cleaning logic behind this dashboard is built and documented in the companion repo [`etl-learning`](https://github.com/AntonWangDTU/etl-learning), which works with realistic mock data from the Kenya and India partner sites:

- Kenya data: DD/MM/YYYY dates, plant height in mm instead of cm, duplicate rows, missing experiment IDs
- India data: comma as decimal separator, yield in t/ha instead of kg/ha, extra whitespace in headers
- Brazil data: unknown strain codes, missing strain assignments in control experiments

## Stack

- **Vanilla HTML/CSS/JS** — no framework, fully static, deployable on GitHub Pages
- **Chart.js** — yield comparison bar chart
- **SQLite (ibis.db)** — the ETL learning repo loads cleaned data into a local database

## Repository

ETL source code: [github.com/AntonWangDTU/etl-learning](https://github.com/AntonWangDTU/etl-learning)
