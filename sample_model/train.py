import model_dispatcher
import click
import joblib
import pandas as pd 
import os
from sklearn import metrics
from utils import split_data
from utils.scaler import Scaler
import config

# TODO(Sayar) This is currently boilerplate. Have to discuss with Leo how to read the data into the model.
@click.command()
@click.option("--fold", type=int, help="Enter the fold")
@click.opton("--model", type=str, help="Enter the model")
def run(fold):
    file = None
    SEED = None
    df = pd.read_csv(file)

    X_train = df[df["kfold"] != fold].reset_index(drop=True).values
    scaler = Scaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)

    X_valid = df[df["kfold"] == fold].reset_index(drop=True).values
    X_valid = scaler.transform(X_valid)

    model = model_dispatcher.models[model]

    model.fit(X_train)

    joblib.dump(model, os.path.join(config.MODEL_OUTPUT, f"knn_{fold}.bin"))


if __name__ == "__main__":
    run()

    

    
