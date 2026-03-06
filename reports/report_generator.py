from ydata_profiling import ProfileReport
import os


def generate_report(df, file_path):

    # extract original file name
    filename = os.path.basename(file_path)
    name = os.path.splitext(filename)[0]

    # create report name
    report_name = f"report_{name}.html"

    report_path = os.path.join("reports", report_name)

    profile = ProfileReport(df, title="Automated EDA Report")

    profile.to_file(report_path)

    print(f"EDA Report Generated: {report_path}")