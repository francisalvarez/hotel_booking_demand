import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/hotel_bookings.csv")



def plot_numerical_pairplot_with_loess(df):
    """
    Creates a pairplot for all numerical variables in the DataFrame with LOESS lines.

    Parameters:
    df (pd.DataFrame): The input DataFrame with numerical variables.
    """
    # Select only numerical columns
    numerical_df = df.select_dtypes(include=['number'])

    # Plot pairplot with LOESS lines
    sns.pairplot(numerical_df.iloc[:, 1:3], kind="reg", plot_kws={'lowess': True})
    plt.show()

plot_numerical_pairplot_with_loess(df)