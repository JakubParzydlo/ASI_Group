"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import lr_train_model, rt_train_model, rt_test_model, lr_test_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=lr_train_model,
            inputs="train_data",
            outputs="linear_regression_model",
            name="linear_regression_train"
            ),
        node(
            func=rt_train_model,
            inputs="train_data",
            outputs="random_forest_model",
            name="random_forest_model_train"
        ),
        node(
            func=lr_test_model,
            inputs=["linear_regression_model", "test_data"],
            outputs="linear_regression_output",
            name="linear_regression_model_test"
        ),
        node(
            func=rt_test_model,
            inputs=["random_forest_model", "test_data"],
            outputs="random_forest_output",
            name="random_forest_model_test"
        )
    ])
