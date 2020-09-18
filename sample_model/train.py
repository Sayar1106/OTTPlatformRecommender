import model_dispatcher
import click
import joblib
import pandas as pd 
import os
from sklearn import metrics
from utils.split_data import split_data
from utils.scaler import Scaler
import config

# TODO(Sayar) This is currently boilerplate. Have to discuss with Leo how to read the data into the model.
@click.command()
@click.option("--model", type=str, help="Enter the model")
@click.option("--neighbors", type=int, help="Number of neighbors")
def run(model, neighbors):
    file = None
    SEED = None
    df = pd.read_csv(config.MODEL_INPUT, usecols=["acousticness", "danceability", 
                                    "energy", "instrumentalness", 
                                    "liveness", "loudness", "speechiness", 
                                    "tempo", "valence", "popularity"])

    X_train, X_valid, _, _ = split_data(df.values, df.values[:,-1])
    scaler = Scaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)

    X_valid = scaler.transform(X_valid)

    model = model_dispatcher.models[model](n_neighbors=neighbors)

    model.fit(X=X_train)

    joblib.dump(model, os.path.join(config.MODEL_OUTPUT, f"knn_.bin"))


if __name__ == "__main__":
    run()

    

    
