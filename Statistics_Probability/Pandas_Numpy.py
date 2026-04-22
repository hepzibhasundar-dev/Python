#Find top 3 most frequent values in a column
import pandas as pd

df = pd.DataFrame({'category': ['A', 'B','A','C','B','A','D','B']})
top3 = df['category'].value_counts().head(3)
print(top3)