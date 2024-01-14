"""
This is a boilerplate pipeline 'model_retraining'
generated using Kedro 0.18.14
"""
import pandas as pd
from sdv.metadata import SingleTableMetadata
from sdv.single_table import GaussianCopulaSynthesizer
from autogluon.tabular import TabularPredictor
import os
from pathlib import Path

from sdv.evaluation.single_table import get_column_plot

def create_synth_data(og_data: pd.DataFrame):
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(og_data)
    
    synthesizer = GaussianCopulaSynthesizer(metadata)
    synthesizer.fit(og_data)

    synth_data = synthesizer.sample(num_rows=3000)
    concat_data = pd.concat([og_data, synth_data])
    return concat_data

def retrain_model(train_data: pd.DataFrame):
    predictor_path = get_predictor_path()
    predictor = TabularPredictor.load(predictor_path)
    predictor.fit(train_data)
    return predictor

def get_predictor_path():
    # Specify the base directory where AutoGluon models are stored
    # Assuming that the method is inside nodes.py in pipelines/model_retraining
    current_dir = Path(__file__).resolve().parent

    # Move up two levels to reach src directory
    src_dir = current_dir.parents[3]

    # Append AutogluonModels to the path
    autogluon_models_path = src_dir / "AutogluonModels"

    # Get a list of all directories (timestamps)
    all_directories = [d for d in autogluon_models_path.iterdir() if d.is_dir()]

    # Find the most recent directory based on timestamps
    latest_directory = max(all_directories, key=os.path.getmtime)

    print(latest_directory)

    return latest_directory
