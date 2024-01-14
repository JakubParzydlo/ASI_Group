"""
This is a boilerplate pipeline 'model_retraining'
generated using Kedro 0.18.14
"""
import pandas as pd
from sdv.metadata import SingleTableMetadata
from sdv.single_table import GaussianCopulaSynthesizer

def create_synth_data(og_data: pd.DataFrame):
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(og_data)
    
    synthesizer = GaussianCopulaSynthesizer(metadata)
    synthesizer.fit(og_data)

    synth_data = synthesizer.sample(num_rows=3000)

    merged_data = pd.merge(og_data, synth_data)
    return merged_data



