
import pandas as pd

def clean_data():
    df = pd.read_csv("data/raw/netflix_titles.csv")

    df = df.drop_duplicates()
    df['duration'] = pd.to_numeric(df['duration'], errors='coerce')
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

    df['rating'] = df['rating'].fillna('Unknown')
    df['country'] = df['country'].fillna('Unknown')

    df.to_csv("data/processed/cleaned_netflix.csv", index=False)

if __name__ == "__main__":
    clean_data()
