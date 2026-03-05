import pandas as pd
import re
import string


# ---------- TEXT CLEANING FUNCTIONS ----------

def remove_html_tags(text):
    pattern = re.compile('<.*?>')
    return pattern.sub(' ', str(text))


def remove_url(text):
    pattern = re.compile(r'https?://\S+|www\.\S+')
    return pattern.sub(' ', str(text))


def remove_punc(text):
    exclude = string.punctuation
    for char in exclude:
        text = text.replace(char, "")
    return text


def clean_text_column(series):
    series = series.str.lower()
    series = series.apply(remove_html_tags)
    series = series.apply(remove_url)
    series = series.apply(remove_punc)
    return series


# ---------- COLUMN TYPE DETECTION ----------

def detect_column_types(df):

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    datetime_cols = df.select_dtypes(include=['datetime64']).columns

    object_cols = df.select_dtypes(include=['object']).columns

    text_cols = []
    categorical_cols = []

    for col in object_cols:
        avg_length = df[col].astype(str).str.len().mean()

        # heuristic: long strings → text column
        if avg_length > 30:
            text_cols.append(col)
        else:
            categorical_cols.append(col)

    return numeric_cols, categorical_cols, text_cols, datetime_cols


# ---------- MAIN CLEANING PIPELINE ----------

def clean_data(df):

    df = df.drop_duplicates()

    numeric_cols, categorical_cols, text_cols, datetime_cols = detect_column_types(df)

    # fill numeric
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # fill categorical
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # clean text columns
    for col in text_cols:
        df[col] = clean_text_column(df[col])

    return df