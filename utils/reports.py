import pandas as pd

def generate_report(data, trends):
    report = f"Market Analysis Report\n\nData:\n{data}\n\nTrends:\n{trends}"
    return report

def save_report(report, file_path):
    with open(file_path, 'w') as file:
        file.write(report)
