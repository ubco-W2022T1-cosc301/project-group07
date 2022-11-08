import pandas as pd
import numpy as np

# Method helper to process date
def process_date(df):
    newDate = []

    for index, row in df.iterrows():
            year = row['Release_Date'][7:9]
            if ( int(year) > 20 ):
                year = '19' + row['Release_Date'][7:9]
            else:
                year = '20' + row['Release_Date'][7:9]
            date = row['Release_Date'][0:2]
            month_name = row['Release_Date'][3:6]
            mnum = datetime.datetime.strptime(month_name, '%b').month
            finalDate = datetime.datetime(int(year), mnum, int(date))
            newDate.append(finalDate)
            
    return newDate

def load_and_process(url_or_path_to_csv_file):
    
    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
        .drop(columns=['genre','players', 'developer'])
        .rename(columns={"name": "Name", "platform": "Platform_Name", "r-date": "Release_Date"})
    )
    
     # Helper method for method chaining
    newDateArray = process_date(df1)
    
    df2 = (df1
           .assign(New_Release_Date=newDateArray)
          )
    
    # Needs to separate this for extra adding
    df3 = (df2
           .assign(Release_Year = pd.DatetimeIndex(df2['New_Release_Date']).year)
          )
    
    return df3
