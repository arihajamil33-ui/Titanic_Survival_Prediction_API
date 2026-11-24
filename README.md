# Titanic Survival Prediction API

A Machine Learning project that predicts whether a passenger would survive the Titanic disaster based on passenger information.

## Live API

**API URL:** https://titanic-survival-prediction-api.onrender.com

**Swagger Documentation:** https://titanic-survival-prediction-api.onrender.com/docs

## Project Overview

This project uses a trained Machine Learning model to predict Titanic passenger survival.

The model is integrated with FastAPI to provide predictions through a REST API.

## Technologies Used

- Python
- Machine Learning
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- Docker
- Render
- GitHub

## Project Files

- `app.py` – FastAPI application
- `titanic_pipeline.pkl` – Trained Machine Learning pipeline
- `requirements.txt` – Project dependencies
- `Dockerfile` – Docker configuration

## API Endpoints

- `GET /` – Checks whether the API is running.
- `POST /predict` – Predicts passenger survival.
- `GET /docs` – Opens interactive API documentation.

## Run Locally

1. Clone the repository:

   `git clone https://github.com/arihajamil33-ui/Titanic_Survival_Prediction_API.git`

2. Open the project folder:

   `cd Titanic_Survival_Prediction_API`

3. Install dependencies:

   `pip install -r requirements.txt`

4. Run the API:

   `uvicorn app:app --reload`

5. Open the documentation:

   `http://127.0.0.1:8000/docs`

## Deployment

The API is deployed on Render using Docker.

## Project Purpose

This project demonstrates how a Machine Learning model can be integrated with FastAPI and deployed as a live web service.

## Author

Machine Learning Project – Titanic Survival Prediction API
