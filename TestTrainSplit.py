from sklearn.model_selection import train_test_split
import pandas as pd

X = pd.read_pickle('datasets/combined-u/x_train_alpha(0.005).pkl')
X_train, X_test = train_test_split(X, test_size=0.2, random_state=25) # test = 20%
X_train.to_pickle("datasets/combined-u/x_train_split_alpha(0.005).pkl")
X_test.to_pickle("datasets/combined-u/x_test_split_alpha(0.005).pkl")
