import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def extract_data (dataframe):
    columns = ["humidity", "precip", "windgust", "winddir", "tempmax", "tempmin", "windspeed", "datetime"]
    return pd.DataFrame(dataframe.loc[:, columns]).fillna(0)


def fill_nan(data):
    return pd.DataFrame(data).fillna(0)


def transform_data(dataframe):
    dataframe["datetime"] = pd.to_datetime(dataframe["datetime"])
    dataframe["year"] = dataframe.datetime.dt.year
    dataframe["month"] = dataframe.datetime.dt.month
    return dataframe


def get_data_by_year(dataframe, year):
    return fill_nan(dataframe.where(dataframe["year"] == year))


def line_plot_image(data):
    x = "month"
    y = "precip"
    plt.xlabel(x)
    plt.ylabel(y)
    sns.lineplot(data=data, x=x, y=y)


if __name__ == '__main__':
    filename = "antananarivo_2020-11-17_to_2023-08-13.csv"
    df = pd.read_csv(f"./data/{filename}")
    df = extract_data(df)
    df = transform_data(df)

    data2020 = get_data_by_year(df, 2020)
    data2021 = get_data_by_year(df, 2021)
    data2022 = get_data_by_year(df, 2022)

    df.to_csv(f"./result/as{filename}")

    line_plot_image(data2020)
    line_plot_image(data2021)
    line_plot_image(data2022)
