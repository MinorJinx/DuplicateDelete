''' Created by Jeremy Reynolds for UALR COSMOS Team

	Removes usernames from first sheet[0] based on 'filter' 
	usernames from second sheet[1] within a single .xlsx file.
	
	600,000 records with a 200,000 record filter takes ~3.5 minutes.
'''

import time, pandas as pd

# Creates dataframe for each sheet
df1 = pd.read_excel('users.xlsx', sheetname=1, header=None)
df2 = pd.read_excel('users.xlsx', sheetname=0, header=None)

# Converts dataframe to list. [0] is column number
df1list = df1[0].tolist()
df2list = df2[0].tolist()

# Replaces entries in 'df1' if in 'df2'
df1 = df1[~df1[0].isin(df2list)]

# Saves to output file with no header
df1.to_csv('output.csv', index=False, header=False, encoding='utf-8')
