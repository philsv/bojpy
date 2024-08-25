# bojpy

[![PyPI version](https://d25lcipzij17d.cloudfront.net/badge.svg?id=py&r=r&ts=1683906897&type=6e&v=0.0.1&x2=0)](https://badge.fury.io/py/bojpy)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://github.com/philsv/bojpy/blob/main/LICENSE)
[![Weekly Downloads](https://static.pepy.tech/personalized-badge/bojpy?period=week&units=international_system&left_color=grey&right_color=blue&left_text=downloads/week)](https://pepy.tech/project/bojpy)
[![Monthly Downloads](https://static.pepy.tech/personalized-badge/bojpy?period=month&units=international_system&left_color=grey&right_color=blue&left_text=downloads/month)](https://pepy.tech/project/bojpy)
[![Downloads](https://static.pepy.tech/personalized-badge/bojpy?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads)](https://pepy.tech/project/bojpy)

bojpy is a Python package that provides a simple interface to the [BOJ Time-Series Data Search](https://www.stat-search.boj.or.jp/index_en.html).

## Installation

```ini
pip install bojpy
```

## Requirements

* beautifulsoup4
* pandas
* requests

## How to use

```python
from bojpy import boj

# By data series id
df = boj.get_data_series(series="BS01'MABJMTA")

# By Time-series data html url
url = "https://www.stat-search.boj.or.jp/ssi/html/nme_R020MM.3576038.20240826070325.02.html"
df = boj.get_data_html(url)
```

## Output Example

```ini
Date        BS01'MABJMTA Bank of Japan Accounts/Assets/Total(Assets, or Liabilities and Net Assets)(s)
                                                                                                      
2024-07-01                                          7617141.0                                         
2024-06-01                                          7536709.0                                         
2024-05-01                                          7610851.0                                         
2024-04-01                                          7583199.0                                         
2024-03-01                                          7564231.0                                         
...                                                 ...
```

## Disclaimer

This package is nor endorsed by nor affiliated with the [Bank of Japan](https://www.boj.or.jp/en/). Please make sure to not abuse the BOJ servers by sending unnecessary requests.
