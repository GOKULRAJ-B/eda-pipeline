from ydata_profiling import ProfileReport

def generate_report(df):

    profile = ProfileReport(df, title="Automated EDA Report")

    profile.to_file("reports/eda_report.html")

    print("EDA Report Generated")