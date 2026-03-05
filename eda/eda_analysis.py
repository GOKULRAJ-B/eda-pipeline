import matplotlib.pyplot as plt
import seaborn as sns

def generate_histograms(df):

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns

    for col in numeric_cols:
        plt.figure()
        sns.histplot(df[col], kde=True)
        plt.title(f"Histogram of {col}")
        plt.savefig(f"reports/{col}_hist.png")


def correlation_heatmap(df):

    plt.figure(figsize=(10,6))
    corr = df.corr(numeric_only=True)

    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("reports/correlation_heatmap.png")


def categorical_counts(df):

    cat_cols = df.select_dtypes(include=['object']).columns

    for col in cat_cols:
        print(f"\nValue Counts for {col}")
        print(df[col].value_counts())