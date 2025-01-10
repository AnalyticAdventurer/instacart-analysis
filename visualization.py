import matplotlib.pyplot as plt

def plot_bar_chart(data, title, xlabel, ylabel, rotation=45):
    """
    Plot a bar chart.
    Args:
        data (Series): Data to plot.
        title (str): Title of the chart.
        xlabel (str): Label for x-axis.
        ylabel (str): Label for y-axis.
        rotation (int): Rotation angle for x-axis labels.
    """
    data.plot(kind='bar', figsize=(12, 6), title=title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation)
    plt.show()
