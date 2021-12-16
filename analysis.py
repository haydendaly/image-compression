import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import defaultdict
from helper.constants import units

fig, ax = plt.subplots()


def customized_box_plot(percentiles, axes, redraw=True, *args, **kwargs):
    """
    Generates a customized boxplot based on the given percentile values
    """
    box_plot = axes.boxplot(
        [
            [-9, -4, 2, 4, 9],
        ]
        * len(percentiles),
        *args,
        **kwargs,
    )
    # Creates len(percentiles) no of box plots
    min_y, max_y = float("inf"), -float("inf")
    for box_no, (q1_start, q2_start, q3_start, q4_start, q4_end, label) in enumerate(
        percentiles
    ):
        box_plot["caps"][2 * box_no].set_ydata([q1_start, q1_start])
        box_plot["whiskers"][2 * box_no].set_ydata([q1_start, q2_start])
        box_plot["caps"][2 * box_no + 1].set_ydata([q4_end, q4_end])
        box_plot["whiskers"][2 * box_no + 1].set_ydata([q4_start, q4_end])
        box_plot["boxes"][box_no].set_ydata(
            [q2_start, q2_start, q4_start, q4_start, q2_start]
        )
        box_plot["medians"][box_no].set_ydata([q3_start, q3_start])
        min_y = min(q1_start, min_y)
        max_y = max(q4_end, max_y)
        axes.set_ylim([0, max_y])
    x_ticks_labels = [experiment[5] for experiment in percentiles]
    ax.set_xticklabels(x_ticks_labels, fontsize=8)
    if redraw:
        ax.figure.canvas.draw()
    return box_plot


rgb, grayscale = defaultdict(list), defaultdict(list)
# clean data
results = pd.read_csv("./results/benchmarks.csv")
results = results.set_index(keys=["algorithm"])
results = results.drop(columns=["Unnamed: 0"])
# results = results.transpose()

for algo, values in results.iterrows():
    if "rgb8bit" in values["image"]:
        rgb[algo].append(
            (
                values["compress_time"],
                values["decompress_time"],
                values["compression_ratio"],
            )
        )
    else:
        grayscale[algo].append(
            (
                values["compress_time"],
                values["decompress_time"],
                values["compression_ratio"],
            )
        )

rgb_data, grayscale_data = dict(), dict()

for algo, values in rgb.items():
    percentiles = []
    for i in range(3):
        metric = [values[j][i] for j in range(len(values))]
        new_arr = []
        new_arr.append(np.percentile(metric, 0))
        new_arr.append(np.percentile(metric, 25))
        new_arr.append(np.percentile(metric, 50))
        new_arr.append(np.percentile(metric, 75))
        new_arr.append(np.percentile(metric, 100))
        new_arr.append(algo)
        new_arr.append(sum(metric) / len(metric))
        percentiles.append(new_arr)
    rgb_data[algo] = percentiles

for algo, values in grayscale.items():
    percentiles = []
    for i in range(3):
        metric = [values[j][i] for j in range(len(values))]
        new_arr = []
        new_arr.append(np.percentile(metric, 0))
        new_arr.append(np.percentile(metric, 25))
        new_arr.append(np.percentile(metric, 50))
        new_arr.append(np.percentile(metric, 75))
        new_arr.append(np.percentile(metric, 100))
        new_arr.append(algo)
        new_arr.append(sum(metric) / len(metric))
        percentiles.append(new_arr)
    grayscale_data[algo] = percentiles

average_rgb = [[], [], []]
average_gray = [[], [], []]
charts_rgb = [[], [], []]
charts_gray = [[], [], []]
for i in range(3):
    for algo, percentiles in rgb_data.items():
        charts_rgb[i].append(percentiles[i][:6])
        # average_rgb[i].append([algo, percentiles[5]])
for i in range(3):
    for algo, percentiles in grayscale_data.items():
        charts_gray[i].append(percentiles[i][:6])
        # average_gray[i].append([algo, percentiles[5]])

# rgb
for i, metric in enumerate(["compress_time", "decompress_time", "compression_ratio"]):
    fig, ax = plt.subplots()
    customized_box_plot(
        charts_rgb[i], ax, redraw=True, notch=0, sym="+", vert=1, whis=1.5
    )
    plt.title("rgb " + metric)
    plt.ylabel(units[metric])
    fig.savefig(f"results/graphs/rgb_{metric}.png")

# grayscale
for i, metric in enumerate(["compress_time", "decompress_time", "compression_ratio"]):
    fig, ax = plt.subplots()
    customized_box_plot(
        charts_gray[i], ax, redraw=True, notch=0, sym="+", vert=1, whis=1.5
    )
    plt.title("grayscale " + metric)
    plt.ylabel(units[metric])
    fig.savefig(f"results/graphs/gray_{metric}.png")

# for metric, values in results.iterrows():
#     plt.bar([algo.__name__[11:] for algo in algos], values.tolist())
#     plt.ylabel(units[metric])
#     plt.title(metric)
#     plt.savefig(f"./results/graphs/{metric}.png")
#     plt.clf()
