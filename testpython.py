import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
df = pd.read_csv('owid-covid-data1.csv')
dfs =df[['date','new_cases']]
#dfs = dfs.fillna(0)
dfs.plot(kind='bar')
##dfs['date'],dfs['new_cases'])
#plt.show()
dfs.show()