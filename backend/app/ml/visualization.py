import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from app.ml.utils import get_analysis_columns


def create_output_directory():
    """
    Create the directory used to store generated plots.
    """
    os.makedirs("reports/figures", exist_ok=True)


def generate_histograms(dataframe: pd.DataFrame) -> list[str]:
    """
    Generate histogram plots for all numerical analysis columns.
    """
    create_output_directory()

    numerical_columns = get_analysis_columns(dataframe)
    generated_files = []

    for column in numerical_columns:
        plt.figure(figsize=(8, 5))

        sns.histplot(dataframe[column], kde=True)

        plt.title(f"Distribution of {column}")

        plt.tight_layout()

        file_path = f"reports/figures/{column}_histogram.png"

        plt.savefig(file_path)
        plt.close()

        generated_files.append(file_path)

    return generated_files

def generate_boxplots(dataframe: pd.DataFrame) -> list[str]:
    """
    Generate boxplot plots for all numerical analysis columns.
    """
    create_output_directory()

    numerical_columns = get_analysis_columns(dataframe)
    generated_files = []

    for column in numerical_columns:
        plt.figure(figsize=(8, 5))

        sns.boxplot(x=dataframe[column])

        plt.title(f"Boxplot of {column}")

        plt.tight_layout()

        file_path = f"reports/figures/{column}_boxplot.png"

        plt.savefig(file_path)
        plt.close()

        generated_files.append(file_path)

    return generated_files

def generate_correlation_heatmap(dataframe: pd.DataFrame) -> str:
    """
    Generate a correlation heatmap for all numerical analysis columns.
    """
    create_output_directory()

    numerical_columns = get_analysis_columns(dataframe)
    correlation_matrix = dataframe[numerical_columns].corr()

    plt.figure(figsize=(8, 6))

    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f",square=True)

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    file_path = "reports/figures/correlation_heatmap.png"

    plt.savefig(file_path)
    plt.close()

    return file_path