import string
from pandas import DataFrame
from sqlalchemy import create_engine
from kedro.config import ConfigLoader
import os

# Load database configuration
config_loader = ConfigLoader(conf_source=os.path.abspath("conf"))
db_params = config_loader.get("db.yml")

def save_to_db(df: DataFrame, table_name: string): 
    # Database connection details
    user = db_params['db']['user']
    password = db_params['db']['password']
    host = db_params['db']['host']
    port = db_params['db']['port']
    dbname = db_params['db']['dbname']

    # Create the SQLAlchemy engine
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")

    # Write the DataFrame to the database
    df.to_sql(table_name, engine, if_exists='replace', index=False)

    print(f"CSV data successfully loaded into the '{table_name}' table.")