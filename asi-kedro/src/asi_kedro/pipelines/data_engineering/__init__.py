"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.14
"""

from .pipeline import create_pipeline
from .nodes import split_data

__all__ = ["create_pipeline"]

__version__ = "0.1"
