import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

def preprocess_data(df):
    X = df.drop('class', axis=1)
    y = df['class']
    
    le = LabelEncoder()
    y = le.fit_transform(y)
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, y, le.classes_

def split_data(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

if __name__ == "__main__":
    df = pd.read_csv('data/raw/ecoli_protein_dataset.csv')
    X, y, classes = preprocess_data(df)
    X_train, X_test, y_train, y_test = split_data(X, y)
    # Save processed data...