import argparse
import os
import json

from typing import Optional

import requests
import pandas as pd


search_url = "https://api.themoviedb.org/3/search/movie"
movie_url = "https://api.themoviedb.org/3/movie"  # https://api.themoviedb.org/3/movie/{movie_id}

def get_movie_id(name: str, year: str, api_key: str) -> Optional[int]:
    params = {"query": name, "year": year, "api_key": api_key}
    res = requests.get(search_url, params = params)
    # print(res.json())
    try:
        return res.json()['results'][0]["id"]
    except Exception as e:
        print(year, name, e)

def get_data(name: str, year: str, api_key: str) -> object:
    out_file = os.path.join('static', 'data', f'{year} {name}.json')

    if os.path.exists(out_file):
        print(f'using cached response {out_file}')
        with open(out_file, 'r') as f:
            return json.load(f)
    
    movie_id = get_movie_id(name, year, api_key)
    params = {"api_key": api_key}
    res = requests.get(f"{movie_url}/{movie_id}", params = params)
    with open(out_file, 'w+') as f:
        f.write(res.text)
    return res.json()


def read_input(file_name: str):
    return pd.read_csv(file_name, dtype=str, names=["name", "year"], header=None, delimiter='|').fillna("")


def get_all(movies: pd.DataFrame, api_key: str) -> pd.DataFrame:
    return pd.DataFrame([pd.Series(get_data(r["name"], r["year"], api_key)) for _, r in movies.iterrows()])


def run(api_key: str, input_name: str, output_name: str, shuffle: bool = False):
    global bearer_token
    output = read_input(input_name)
    os.makedirs(os.path.join('static', 'data'), exist_ok=True)
    if shuffle:
        output = output.sample(frac=1).reset_index(drop=True)

    get_all(output, api_key).to_csv(output_name, sep='|')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download movie data using OMDb.')
    parser.add_argument('--key', required=True,
                        help='The Movie Database key. Obtainable from https://developer.themoviedb.org/docs/getting-started')
    parser.add_argument('--input', type=str, default="input.csv",
                        help='name of input csv file. Must contain two columns: one for name and one for year')
    parser.add_argument('--output', type=str, default="./static/data.csv",
                        help='name of output csv file. Should be left as default for app to use')
    parser.add_argument('--shuffle', action='store_true', help="Output order randomized")

    args = parser.parse_args()

    run(args.key, args.input, args.output, args.shuffle)
