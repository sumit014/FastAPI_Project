import matplotlib.pyplot as plt
import pandas as pd
import io


def generate_histogram(df: pd.DataFrame, columns: list) -> bytes:
    plt.figure(figsize=(10, 6))
    for column in columns:
        plt.hist(df[column], bins=20, alpha=0.5, label=column)
    plt.legend(loc='upper right')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Histogram')

    # Save plot to bytes IO buffer
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)

    return img_buffer.read()


def generate_scatter_plot(df: pd.DataFrame, x_column: str, y_column: str) -> bytes:
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_column], df[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title('Scatter Plot')

    # Save plot to bytes IO buffer
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)

    return img_buffer.read()
