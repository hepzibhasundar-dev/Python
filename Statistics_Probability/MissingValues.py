#Handle missing values
import pandas as pd
df = pd.DataFrame({'score': [5,4,5,3,7]})
#Fill with mean
df['score'].fillna(df['score'].mean(), inplace=True)

#Drop rows with >50% missing
df.dropna(thresh=len(df.columns) * 0.5, inplace=True)

#Forward fill (time series)
#df.fillna(method='ffill', inplace=True)
#obj.ffill()
