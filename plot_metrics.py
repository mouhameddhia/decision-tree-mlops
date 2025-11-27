# plot_metrics.py
import matplotlib.pyplot as plt
import os
from datetime import datetime


def save_accuracy_plot(accuracy, output_dir="metrics"):
    """
    Save a plot showing accuracy for the current training run.
    The filename includes a timestamp so each run generates a new plot.
    """
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(output_dir, f"accuracy_{timestamp}.png")

    plt.figure()
    plt.plot([1], [accuracy], marker="o")
    plt.title("Model Accuracy")
    plt.xlabel("Run")
    plt.ylabel("Accuracy (%)")
    plt.ylim(0, 100)
    plt.grid(True)

    plt.savefig(filepath)
    plt.close()

    print(f"📈 Accuracy plot saved at: {filepath}")
    return filepath
