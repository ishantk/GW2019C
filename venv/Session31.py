import pandas as pd

"""
    Python
    Storage Containers : Data Structures
    Tuple, List, ....
    Numpy
    Pandas will give us 2 Data Structure:
    1. Series
        stores data as 1-D Array
    2. DataFrame
        stores data as 2-D Array (Tabular Form)
        
"""

print(pd.__version__)

series = pd.Series()
frame = pd.DataFrame()

print(series, type(series))
print(frame, type(frame))
