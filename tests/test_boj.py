import pandas as pd
import pytest

from bojpy import boj


@pytest.mark.parametrize(
    "series",
    [
        "BS01'MABJMTA",
        "CO'TK99F0000201HCQ00000",
    ],
)
def test_get_data_series(series):
    """Test get_data_series method."""
    df = boj.get_data_series(series)
    assert isinstance(df, pd.DataFrame)


@pytest.mark.parametrize(
    "url",
    [
        "https://www.stat-search.boj.or.jp/ssi/html/nme_R020MM.3576038.20240826070325.02.html",
        "https://www.stat-search.boj.or.jp/ssi/html/nme_R020QQ.3579502.20240826074512.02.html",
    ],
)
def test_get_data_html(url):
    """Test get_data_html method."""
    df = boj.get_data_html(url)
    assert isinstance(df, pd.DataFrame)
