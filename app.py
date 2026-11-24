import joblib 
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel, Field

model = joblib.load("titanic_pipeline.pkl")    #load trained model

app = FastAPI(title="Titanic Survival Prediction API")


class Passenger(BaseModel):
    pclass: int = Field(ge=1, le=3)
    sex: str 
    age: float = Field(ge=0, le=100)
    sibsp: int = Field(ge=0, le=10)
    parch: int = Field(ge=0, le=10)
    fare: float = Field(ge=0)
    embarked: str 

@app.get("/")
def home():
    return {"message":"Titanic Survival Prediction API is running"}


@app.post("/predict")
def predict_survival(passenger: Passenger):


        data = pd.DataFrame([{
            "pclass":passenger.pclass,
            "sex":passenger.sex.lower(),
            "age":passenger.age,
            "sibsp":passenger.sibsp,
            "parch":passenger.parch,
            "fare":passenger.fare,
            "embarked":passenger.embarked.upper()
        }])


        prediction = int(model.predict(data)[0])
        probability = float(model.predict_proba(data)[0][1])

        return {"prediction": prediction,
                "result": "Survived" if prediction == 1 else "Did not survive",
                "survival_probability": round(probability,4)}




