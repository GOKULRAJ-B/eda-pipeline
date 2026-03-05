import os

def save_clean_data(df, file_path):

    # extract original filename
    filename = os.path.basename(file_path)
    name = os.path.splitext(filename)[0]

    # create cleaned_data folder if not exists
    os.makedirs("cleaned_data", exist_ok=True)

    # new file path
    cleaned_file = os.path.join("cleaned_data", f"cleaned_{name}.csv")

    df.to_csv(cleaned_file, index=False)

    print(f"Cleaned dataset saved at: {cleaned_file}")