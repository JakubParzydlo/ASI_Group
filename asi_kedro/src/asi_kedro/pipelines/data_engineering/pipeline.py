"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import knn_filling, avg_filling, iter_filling, drop_na, split_data, save_raw_data_to_db

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=save_raw_data_to_db,
            inputs="raw_data",
            outputs=None,
            name="save_raw_data_to_db_node"
        ),
        node(
            func=knn_filling,
            inputs="raw_data",
            outputs="filled_data_knn",
            name="node_fill_data_knn"
            ),
        node(
            func=avg_filling,
            inputs="raw_data",
            outputs="filled_data_avg",
            name="node_fill_data_avg"
            ),
        node(
            func=iter_filling,
            inputs="raw_data",
            outputs="filled_data_iter",
            name="node_fill_data_iter"
            ),
        node(
            func=drop_na,
            inputs="raw_data",
            outputs="filled_data_tidy",
            name="node_fill_data_tidy"
            ),
        node(
            func=split_data,
            inputs="filled_data_iter",
            outputs=["train_data", "test_data"],
            name="split_data_node"
        ),
        
        
    ])
