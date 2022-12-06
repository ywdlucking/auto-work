import numpy as np
import pandas as pd

df = pd.read_csv('data/read_book.csv', header=0, sep=',', names=['stu_id', 'book_id', 'score'])
print(df)
df_groupby = df.groupby('book_id', as_index=False)
print('组内的键值：\n{}'.format(df_groupby.groups.keys()))
df_agg = df_groupby.agg(['min','mean','max'])
print(df_agg)

df_score_agg = df_groupby.agg({'score':['min','mean','max']})
print(df_score_agg)