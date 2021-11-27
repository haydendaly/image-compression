import matplotlib.pyplot as plt
import pandas as pd
from helper.constants import units
from main import algos

# clean data
results = pd.read_csv('./results/benchmarks.csv')
results = results.set_index(keys=['algorithm'])
results = results.drop(columns=['Unnamed: 0'])
results = results.transpose()

for metric, values in results.iterrows():
    plt.bar([algo.__name__[11:] for algo in algos], values.tolist())
    plt.ylabel(units[metric])
    plt.title(metric)
    plt.savefig(f"./results/graphs/{metric}.png")
    plt.clf()
