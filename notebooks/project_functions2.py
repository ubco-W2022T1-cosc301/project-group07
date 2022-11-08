import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):  
    
    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .drop(columns=["name", "platform", "players"])
          .dropna(axis=0, subset=["developer"])
          .dropna(axis=0, subset=["genre"])
          .rename(columns={"developer" : "Developer"})
          .rename(columns={"genre" : "Genre"})
          .rename(columns={"r-date" : "Release Date"})
      )
    
    df1["Developer"] = (
        df1["Developer"]
          .str.replace(r"(?<=[a-z])(?=[A-Z])", " ", regex=True).str.strip()
          .str.replace(",", ", ").str.strip()
    )
    
    df1["Genre"] = (
        df1["Genre"]
          .str.split(",")
          .apply(pd.unique)
    )

    df1["Release Year"] = (
        df1["Release Date"]
          .apply(pd.to_datetime).dt.year
    )
    
    df2 = (
          df1
          .explode("Genre")
      )

    return df2 