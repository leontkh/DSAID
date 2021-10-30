from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

default_args = {
    'owner': 'Leon Tan',
    'start_date': datetime.now(),
    'retries': 0,
    'depends_on_past': False,
    }


with DAG(
        'process_csv',
        default_args=default_args,
        description='Process csv file containing name and price',
        schedule_interval="1 1 * * *",
        ) as dag:

    def process_csv(ds, **kwargs):
        import glob
        import os
        import pandas as pd
        
        input_path = os.environ.get("CSV_INPUT_PATH")
        output_path = os.environ.get("CSV_OUTPUT_PATH")
        
        print(input_path)
        print(output_path)
        
        for file_name in glob.glob(input_path+'*.csv'):
            df = pd.read_csv(file_name, low_memory=False)

            # Delete any rows which do not have a name
            df = df.loc[~(df["name"]=="")]
            df.dropna(subset=["name"], inplace=True)

            # Removing titles, then split the name field into first_name, and last_name, dropping away any suffixes
            df[["first_name", "last_name", "drop"]] = (df['name'].str
                                                       .replace("Mr. ","",regex=True)
                                                       .replace("Mrs. ","",regex=True)
                                                       .replace("Ms. ","",regex=True)
                                                       .replace("Miss ","",regex=True)
                                                       .replace("Dr. ","",regex=True)
                                                       .str.split(" ", 2, expand=True)
                                                      )
            df.drop(columns=["drop"], inplace=True)

            # Remove any zeros prepended to the price field
            df["price"] = df["price"].astype("float64")

            # Create a new field named above_100, which is true if the price is strictly greater than 100
            df["above_100"] = df["price"].gt(100)

            # Saves a new file in output
            df.to_csv(f"{file_name.replace(input_path,output_path+'processed_')}")

            # Removes the file from input so that it doesnt run again on the same input
            os.remove(file_name)
        return "Completed without errors"
    
    process_csv = PythonOperator(
        task_id='process_csv_in_input_folder',
        python_callable=process_csv,
    )