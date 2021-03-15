import os
import pandas as pd

AUTHOR_INPUT = "./json/authors.tang.json"
AUTHOR_OUTPUT = "./data_tang/"
POEM_DIR = "./json/"
POEM_OUTPUT = "./data_tang/"


def convert_authors():
    author_df = pd.read_json(AUTHOR_INPUT)
    author_df.to_csv(f'{AUTHOR_OUTPUT}authors_tang.csv', index=False)


def convert_poems():
    poem_df = pd.DataFrame()
    for file in os.listdir(POEM_DIR):
        if file.startswith("poet.tang."):
            df = pd.read_json(f"{POEM_DIR}{file}")
            poem_df = poem_df.append(df)
    poem_df.to_csv(f"{POEM_OUTPUT}poems_tang.csv", index=False)


if __name__ == "__main__":
    convert_authors()
    convert_authors()

