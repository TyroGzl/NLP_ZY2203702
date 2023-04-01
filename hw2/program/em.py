import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv('height_data.csv')
    data1 = data.values.tolist()

    print(data1[1])
    print(1)
