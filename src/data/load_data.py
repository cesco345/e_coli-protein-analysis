import pandas as pd
from ucimlrepo import fetch_ucirepo

def fetch_ecoli_data():
    ecoli_data = fetch_ucirepo(name="ecoli")
    df = pd.DataFrame(ecoli_data['data']['features'])
    df['class'] = ecoli_data['data']['targets']
    return df

def save_data(df, path):
    df.to_csv(path, index=False)

if __name__ == "__main__":
    df = fetch_ecoli_data()
    save_data(df, 'data/raw/ecoli_protein_dataset.csv')