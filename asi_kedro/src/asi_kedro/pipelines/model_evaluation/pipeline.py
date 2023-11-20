"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.18.14
"""
from kedro.pipeline import Pipeline, pipeline, node
from .nodes import evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=evaluate_model,
            inputs="random_forest_output",
            outputs="random_forest_evaluation_plot",
            name="random_forest_evaluation"
        ),
        node(
            func=evaluate_model,
            inputs="linear_regression_output",
            outputs="linear_regression_evaluation_plot",
            name="linear_regression_evaluation"
        )
    ])
