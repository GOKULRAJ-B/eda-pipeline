from ingestion.data_loader import load_dataset
from validation.data_validator import dataset_metadata, data_quality_check
from preprocessing.data_cleaner import clean_data
from storage.data_storage import save_clean_data
from reports.report_generator import generate_report
import os
import sys

def run_pipeline(file_path):
    df = load_dataset(file_path)

    # dataset_metadata(df)
    # data_quality_check(df)

    df_clean = clean_data(df)

    save_clean_data(df_clean, file_path)
    generate_report(df_clean, file_path)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        raise Exception("File path required")

    run_pipeline(file_path)