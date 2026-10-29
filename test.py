import pandas as pd 

df = pd.read_csv('data.csv') # read file (file handling)

NaN --> Null --> df.dropna(inplace == 'True') # clean ALL rows with NaN/NULL

Empty --> 0 or [   ] --> df.dropna() # clean empty cells ******* 

df.dropna({'row''column'}

df.loc[7,'Duration'] = 45 # replacing values 
