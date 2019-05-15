from fancyimpute import KNN
import pandas as pd

data = pd.read_csv("Fortune500beg.csv")
print(data)
train_cols = list(data)
train = pd.DataFrame(KNN(k=5).fit_transform(data))
train.columns = train_cols
