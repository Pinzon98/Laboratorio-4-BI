from typing import Optional
from fastapi import FastAPI
from DataModel import DataModel
from DataModelPunto2 import DataModelPunto2
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from typing import List

columns = ["Adult Mortality", "Alcohol", "Hepatitis B", "Measles", "BMI", "Polio", "Total expenditure", "HIV/AIDS", "GDP", "Population", "thinness 10-19 years", "Income composition of resources"]
ytest = ["Valor Esperado"]
app = FastAPI() 

@app.get("/")
def read_root():
   return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
def make_predictions(dataModel: DataModel):
    df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
    df.columns = dataModel.columns()
    df = df[columns]
    model = joblib.load("pipeline.joblib")
    result = model.predict(df)
    result = result[0]
    return result

@app.post("/predictionPunto2")
def make_predictionsPunto2(dataModelPunto2: List[DataModelPunto2]):
    y_test = []
    y_pred = []
    for i in dataModelPunto2:        
        df = pd.DataFrame(i.dict(), columns=i.dict().keys(), index=[0])
        df.columns = i.columns()
        dfPred = df[columns]
        valorEsp = df[ytest]
        valorEsp = valorEsp.to_dict()
        model = joblib.load("pipeline.joblib")
        result = model.predict(dfPred)
        result = result[0]
        y_test.append(valorEsp["Valor Esperado"][0])
        y_pred.append(result)
    return r2_score(y_test, y_pred)