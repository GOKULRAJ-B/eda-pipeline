import pandas as pd

def dataset_metadata(df):

    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    datetime_cols = df.select_dtypes(include=['datetime64']).columns

    return numeric_cols, categorical_cols, datetime_cols


def data_quality_check(df):

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:", df.duplicated().sum())

    print("\nSummary Statistics")
    print(df.describe())