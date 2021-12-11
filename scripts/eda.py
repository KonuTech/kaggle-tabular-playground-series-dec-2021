import pandas as pd
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns

def count_unique_values(dataframe, variables):
    """
    :param dataframe:
    :param variables:
    :return:
    """
    for column in variables:
        count_unique = dataframe[str(column)].value_counts()
        count_null = pd.Series(dataframe[str(column)].isnull().sum(),index=["nan"])
        count_unique = count_unique.append(count_null, ignore_index=False)

        print("\n")
        print(column + " count distinct:")
        print(count_unique)

        count_unique_normalized = dataframe[str(column)].value_counts(normalize=True)

        print("\n")
        print(column + " count distinct normalized:")
        print(count_unique_normalized)

def visualise_numerics(dataframe, variables):
    """
    :param dataframe:
    :param variables:
    :return:
    """
    for column in variables:
        ax = sns.distplot(dataframe[column].dropna(), fit=norm)
        ax.set_title("Histogram of " + str(column))
        ax.set_xlabel(str(column))
        ax.set_ylabel("Frequency Rate")
        fig = plt.figure()

        res = stats.probplot(dataframe[column], plot=plt)
        fig = plt.figure()

def visualise_objects(dataframe, categories):
    """
    :param dataframe:
    :param categories:
    :return:
    """
    for category in categories:
        ax = sns.countplot(dataframe[category], palette="Paired")
        ax.set_title("Bar plot of " + str(category))
        ax.set_xlabel(str(category))
        fig = plt.figure()

def correlation_matrix(dataframe):
    """
    :param dataframe:
    :return:
    """
    corrmat = dataframe.corr()
    f, ax = plt.subplots(figsize=(10, 10))
    fig = sns.heatmap(corrmat, vmax=1, square=True, annot=True)
    fig.figure.savefig("correlation_matrix.jpg")
    plt.clf()