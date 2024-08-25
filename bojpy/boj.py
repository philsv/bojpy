import warnings
from urllib.parse import urlencode

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore", category=UserWarning)


def get_data_series(
    series: str,
    skiprows: int = 0,
) -> pd.DataFrame:
    """
    Returns data series from the Bank of Japan (BOJ) Time-Series Data Search.

    Example:
        >>> get_data_series(series="BS01'MABJMTA")
    """
    base_url = "https://www.stat-search.boj.or.jp/ssi/"
    search_path = "cgi-bin/famecgi2?cgi=%24nme_r030_en&chkfrq=MM&rdoheader=SIMPLE&rdodelimitar=COMMA&hdnYyyyFrom=&hdnYyyyTo=&sw_freq=NONE&sw_yearend=NONE&sw_observed=NONE&"
    series_encoded = urlencode({"hdncode": series})
    url = f"{base_url}{search_path}{series_encoded}"

    response = requests.get(url)
    response.raise_for_status()

    page_content = response.content
    soup = BeautifulSoup(page_content, "lxml")
    nodes = soup.select("a[href*=csv]")

    if not nodes:
        raise ValueError(f"Could not find .csv file in {url}")

    url = f"https://www.stat-search.boj.or.jp/{nodes[0]['href']}"
    df = pd.read_csv(url, skiprows=skiprows)

    first_row = df.iloc[0]
    new_columns = df.columns + " " + first_row
    df.columns = new_columns
    df = df.drop(index=0)

    df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
    df = df.replace({"ND": np.nan}, regex=True)

    df = df.rename(columns={df.columns[0]: ""})
    df = df.rename_axis("Date", axis=1)
    df = df.set_index(df.columns[0])
    df = df.astype(float)

    if df.index.is_monotonic_increasing:
        df = df.sort_index(ascending=False)

    df = df.dropna()
    return df


def get_data_html(
    url: str,
    skiprows: int = 0,
) -> pd.DataFrame:
    """
    Returns the HTML content as a DataFrame of a given Time-series data URL.

    Example:
        >>> get_data_html(url="https://www.stat-search.boj.or.jp/ssi/html/nme_R000.3576779.20240826071135.02.html")
    """
    df = pd.read_html(url, skiprows=skiprows)[0]
    df.columns = df.iloc[0]  # type: ignore
    df = df.drop(index=0)

    df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
    df = df.replace({"ND": np.nan}, regex=True)

    df = df.rename(columns={df.columns[0]: ""})
    df = df.rename_axis("Date", axis=1)
    df = df.set_index(df.columns[0])
    df = df.astype(float)

    if df.index.is_monotonic_increasing:
        df = df.sort_index(ascending=False)

    df = df.dropna()
    return df
