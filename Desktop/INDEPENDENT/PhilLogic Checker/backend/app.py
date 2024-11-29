import pandas as pd
from datasets import Dataset
# loading train split as pandas df
df = pd.read_json("/Users/VishalVunnam/Desktop/INDEPENDENT/aaac/aaac02_train.jsonl", lines=True, orient="records")
# creating dataset from pandas df
Dataset.from_pandas(df)
