from sklearn.model_selection import train_test_split
import numpy as np

def split_data(X, y):
   return train_test_split(X,y)

if __name__ == "__main__":
    arr = np.random.randn(100,10)
    X_train, X_test, y_train, y_test = split_data(arr[:,:-1], arr[:,-1])
    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)