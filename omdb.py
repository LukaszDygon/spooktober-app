import argparse

import requests
import pandas as pd

api_url = "http://www.omdbapi.com"

def get_data(name: str, year: str, api_key: str) -> object:
    params = {"t": name, "y": year, "type": "movie", "apikey": api_key}
    res = requests.get(api_url, params=params)
    print(res.url)
    return res.json()


def read_input(file_name: str):
    return pd.read_csv(file_name, dtype=str, names=["name", "year"], header=None).fillna("")


def get_all(movies: pd.DataFrame, api_key: str) -> pd.DataFrame:
    return pd.DataFrame([pd.Series(get_data(r["name"], r["year"], api_key)) for _, r in movies.iterrows()])


def run(api_key: str, input_name: str, output_name: str, shuffle: bool = False):
    output = read_input(input_name)
    if shuffle:
        output = output.sample(frac=1).reset_index(drop=True)
    get_all(output, api_key).to_csv(output_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download movie data using OMDb.')
    parser.add_argument('--key', required=True,
                        help='Open Movie Database key. Obtainable from http://www.omdbapi.com/apikey.aspx')
    parser.add_argument('--input', type=str, default="input.csv",
                        help='name of input csv file. Must contain two columns: one for name and one for year')
    parser.add_argument('--output', type=str, default="./static/data.csv",
                        help='name of output csv file. Should be left as default for app to use')
    parser.add_argument('--shuffle', action='store_true', help="Output order randomized")

    args = parser.parse_args()

    run(args.key, args.input, args.output, args.shuffle)
