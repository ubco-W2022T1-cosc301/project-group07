import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):  
    
    # Load data and remove rows with missing values
    df = (
          pd.read_csv(url_or_path_to_csv_file)
          .drop(columns=["name", "r-date", "developer"])
      )
    
    
    df = (
        df.drop(df[df.players == 'No info'].index)
    )

    
    df['genre'] = (
         df["genre"]
        .str.split(",")
        .apply(pd.unique)     
    )

    
    df1 = (
          df
          .explode("genre")
      )

    return df1