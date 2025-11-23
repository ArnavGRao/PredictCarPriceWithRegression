import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def load_car_data():
    return pd.read_csv("dataset/CarPrice_Assignment.csv")


"""
def partition_dataset():
    car = load_car_data()
    car["avgmpg"] = (car["citympg"] + car["highwaympg"]) / 2

    # Creating test set
    car["mileage_cat"] = pd.cut(
        car["avgmpg"],
        bins=[0, 20, 25, 30, 35, 40, 45, np.inf],
        labels=[1, 2, 3, 4, 5, 6, 7],
    )

    # car["mileage_cat"].value_counts().sort_index().plot.bar(grid=True)
    # plt.show()

    train_set, test_set = train_test_split(
        car, test_size=0.2, stratify=car["mileage_cat"], random_state=42
    )

    # Drop unnecessary columns
    for set_ in (train_set, test_set):
        set_.drop(["mileage_cat", "citympg", "highwaympg"], axis=1, inplace=True)

    return train_set, test_set
"""


def partition_dataset():
    car = load_car_data()

    # Binning to allow creation of test set
    car["engsize_cat"] = pd.cut(
        car["enginesize"],
        bins=[50, 100, 150, 200, np.inf],
        labels=[1, 2, 3, 4],
    )

    train_set, test_set = train_test_split(
        car, test_size=0.2, stratify=car["engsize_cat"], random_state=42
    )

    # Drop unnecessary columns
    for set_ in (train_set, test_set):
        set_.drop("engsize_cat", axis=1, inplace=True)

    return train_set, test_set
