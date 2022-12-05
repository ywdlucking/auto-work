import numpy as np
import pandas as pd

dates = pd.date_range("20130101", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

print(df['A'].to_numpy())


print(df.loc[:, ["A", "B"]])


df = pd.DataFrame({
  "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
  "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
  "C": np.random.randn(8),
  "D": np.random.randn(8),
})

print(df.groupby("A")[["C", "D"]].sum()) 

s = pd.Series(range(10))

print(s.rolling(window=5).mean())