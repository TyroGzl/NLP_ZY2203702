import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


class GMM:
    def __init__(self, data, n, theta=None, miu=None, sigma=None):
        self.data = data
        self.n = n
        if theta is not None:
            self.theta = theta
        else:
            self.theta = [1 / self.n for i in range(self.n)]

        if miu is not None:
            self.miu = miu
        else:
            self.miu = []
            for i in range(self.n):
                sample_count = int(len(self.data) * self.theta[i])
                sample = random.sample(self.data, sample_count)
                self.miu.append(sum(sample) / sample_count)

        if sigma is not None:
            self.sigma = sigma
        else:
            self.sigma = [1 for i in range(self.n)]


if __name__ == '__main__':
    data_read = pd.read_csv('height_data.csv')
    data = []
    for i in range(data_read.size):
        data.append(data_read.values[i].tolist()[0])
    g = GMM(data, 3)
    print(data[1])
    print(1)
