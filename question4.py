import pandas as pd


def run(f):
    f.seek(0)
    csv_sheet = pd.read_csv(f)

    print(csv_sheet.groupby(['age'])['age'].count())
    print(csv_sheet.groupby(['height_cm'])['height_cm'].count())
    print(csv_sheet.groupby(['weight_kg'])['weight_kg'].count())
