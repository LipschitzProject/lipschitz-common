# lipschitz-common

## Quickstart
### 1. Install needed modules
```bash
pip install requests
pip install pandas
```
### 2. Use the Downloader
2.1. Copy `client_downloader_api.py` into your project folder

2.2. Import the `Client_Downloader` Class in your program
```python
# at the top of your program

from client_downloader_api import Client_Downloader
```

2.3. Initialize the Class in your program
```python
# Somewhere before you use the downloader in your program
# You can use any variable name
# Replace your_username_str and your_password_str with your own username and password

downloader = Client_Downloader("your_username_str", "your_password_str")
```
2.4. Use the downloader in your porgram (refer to the **Parameters** section)

## Parameters
### request_type (str)
- `'min_between'`: get minute-level data between two time points (inclusive)
    + return a DataFrame formatted as below and your remaining quota:
    ```bash
    code        date_time            column_1  column_2  column_3  ...
    888888_EG   YYYY-mm-DD HH:MM:00   info_1    info_2    info_3   ...
    ...            ...                 ...       ...       ...     ...
    ```
- `'real_time'`: get real-time data
    + return a DataFrame fromatted as below and your remaining quota:
    ```bash
                date_time               column_1  column_2  column_3  ...
    888888_EG   YYYY-mm-DD HH:MM:SS:00   info_1    info_2    info_3   ...
    ...            ...                    ...       ...       ...     ...
    ```
- `'day_between'`: get day-level data between two dates (inclusive)
    + return a DataFrame formatted as below and your remaining quota:
    ```bash
    code        date_time    column_1  column_2  column_3  ...
    888888_EG   YYYY-mm-DD    info_1    info_2    info_3   ...
    ...            ...         ...       ...       ...     ...
    ```
- `'stock_name'`: find stock name of the code
    + return a DataFrame formatted as below and your remaining quota:
    ```bash
                stock_name
    888888_EG   中文名称
    ```
- `'trade_day'`: determine if a certain day is a trading day (for A-share only)
    + return a boolean (True for trading day, False for non-trading day) and your remaining quota
- `'trade_day_between'`: find all trading days between two dates (inclusive, for A-share only)
    + return a list formatted as below and your remaining quota:
    ```bash
    ['YYYY-mm-DD', 'YYYY-mm-DD', 'YYYY-mm-DD', ...]
    ```
- `'latest_price'`: get the latest price of a stock
    + return a float (price) and your remaining quota
- `'check_quota'`: check your remaining quota
    + return null data and your remaining quota

### stock_list (list[str])
- a list of stock codes formatted as below:
```python
# both '_' and '.' are supported

['888888_EG', '666666_EG', '233333_EG', ...]  # preferred
or
['888888.EG', '666666.EG', '233333.EG', ...]
```
- only needed when **request_type** is:
    + `'min_between'`
    + `'real_time'`
    + `'day_between'`
    + `'stock_name'`
    + `'latest_price'`

### frequency (str)
- a string indicating the time interval between two adjacent lines in data
- support `'1', '3', '5', '10', '15', '30', '60'`
- only needed when **request_type** is:
    + `'min_between'`

### start_time (str)
- a string of the start time with the format "YYYY-mm-DD HH:MM"
- only needed when **request_type** is:
    + `'min_between'`
    + `'day_between'`
    + `'trade_day'` (serve as the queried date)
    + `'trade_day_between'`
- please still add random "HH:MM" ("00:00" recommended) when exact time is not needed

### end_time (str)
- a string of the end time with the format "YYYY-mm-DD HH:MM"
- only needed when **request_type** is:
    + `'min_between'`
    + `'day_between'`
    + `'trade_day_between'`
- please still add random "HH:MM" ("00:00" recommended) when exact time is not needed

### columns (list[str])
- a list of info you want to query formatted as below:
```python
['column_1', 'column_2', 'column_3', ...]
```
- only needed when **request_type** is:
    + `'min_between'`
    + `'real_time'`
    + `'day_between'`
- supported queries are listed as below:
    * for stock (A-share):
        + `'open'`: 开盘价
        + `'high'`: 最高价
        + `'low'`: 最低价
        + `'close'`: 收盘价
        + `'avgPrice'`: 均价
        + `'volume'`: 成交量
        + `'amount'`: 成交额
        + `'change'`: 涨跌
        + `'changeRatio'`: 涨跌幅
        + `'turnoverRatio'`: 换手率
        + `'sellVolume'`: 内盘
        + `'buyVolume'`: 外盘
        + `'changeRatio_accumulated'`: 涨跌幅（累计）
    * for stock (HK):
        + `'open'`: 开盘价
        + `'high'`: 最高价
        + `'low'`: 最低价
        + `'close'`: 收盘价
        + `'avgPrice'`: 均价
        + `'volume'`: 成交量
        + `'amount'`: 成交额
        + `'change'`: 涨跌
        + `'sellVolume'`: 内盘
        + `'buyVolume'`: 外盘
    * for fund
        + `'open'`: 开盘价
        + `'high'`: 最高价
        + `'low'`: 最低价
        + `'close'`: 收盘价
        + `'avgPrice'`: 均价
        + `'volume'`: 成交量
        + `'amount'`: 成交额
        + `'change'`: 涨跌
        + `'changeRatio'`: 涨跌幅
    * for index
        + `'open'`: 开盘价
        + `'high'`: 最高价
        + `'low'`: 最低价
        + `'close'`: 收盘价
        + `'avgPrice'`: 均价
        + `'volume'`: 成交量
        + `'amount'`: 成交额
        + `'change'`: 涨跌
        + `'changeRatio'`: 涨跌幅
        + `'changeRatio_accumulated'`: 涨跌幅（累计）
    * for bond
        + `'open'`: 开盘价
        + `'high'`: 最高价
        + `'low'`: 最低价
        + `'close'`: 收盘价
        + `'avgPrice'`: 均价
        + `'volume'`: 成交量
        + `'amount'`: 成交额
        + `'change'`: 涨跌
        + `'changeRatio'`: 涨跌幅
        + `'sellVolume'`: 内盘
        + `'buyVolume'`: 外盘
    * for option
        + `'open'`: 开盘价
        + `'high'`: 最高价
        + `'low'`: 最低价
        + `'close'`: 收盘价
        + `'volume'`: 成交量
        + `'amount'`: 成交额
        + `'change'`: 涨跌
        + `'changeRatio'`: 涨跌幅
        + `'sellVolume'`: 内盘
        + `'buyVolume'`: 外盘
        + `'openInterest'`: 持仓量
    * for future
        + `'open'`: 开盘价
        + `'high'`: 最高价
        + `'low'`: 最低价
        + `'close'`: 收盘价
        + `'volume'`: 成交量
        + `'amount'`: 成交额
        + `'change'`: 涨跌
        + `'sellVolume'`: 内盘
        + `'buyVolume'`: 外盘
        + `'openInterest'`: 持仓量
        + `'changeRatio_accumulated'`: 涨跌幅（累计）
    * for new three board
        + `'open'`: 开盘价
        + `'high'`: 最高价
        + `'low'`: 最低价
        + `'close'`: 收盘价
        + `'avgPrice'`: 均价
        + `'volume'`: 成交量
        + `'amount'`: 成交额
        + `'change'`: 涨跌
        + `'changeRatio'`: 涨跌幅
        + `'turnoverRatio'`: 换手率
        + `'sellVolume'`: 内盘
        + `'buyVolume'`: 外盘

## Examples
```python
# import the "Client_Downloader" class
from client_downloader_api import Client_Downloader

# Initialize the downloader
downloader = Client_Downloader('your_username_str', 'your_password_str')

# rd is the returned data, quota is your remaining data
rd, quota = downloader.download_request(request_type='min_between', stock_list=['885779_TI'], frequency='1', start_time='2022-10-01 09:30', end_time='2022-10-01 15:30', columns=['open', 'high', 'low', 'close', 'avgPrice', 'volume'])

rd, quota = downloader.download_request(request_type='real_time', stock_list=['885779_TI'], columns=['open', 'high', 'low', 'close', 'avgPrice', 'volume'])

rd, quota = downloader.download_request(request_type='day_between', stock_list=['885779_TI'], start_time='2022-10-01 00:00', end_time='2022-10-31 00:00', columns=['open', 'high', 'low', 'close', 'avgPrice', 'volume'])

rd, quota = downloader.download_request(request_type='stock_name', stock_list=['885779_TI', '864005_TI'])

rd, quota = downloader.download_request(request_type='trade_day', start_time='2022-10-01 00:00')

rd, quota = downloader.download_request(request_type='trade_day_between', start_time='2022-10-01 00:00', end_time='2022-10-31 00:00')

rd, quota = downloader.download_request(request_type='latest_price', stock_list=['885779_TI'])

rd, quota = downloader.download_request(request_type='check_quota')
```

## Appendix
### Quota usage
- Defult user quota is **3,000,000 per week**
- Quota will be reset at **00:00, Monday**
- The *maximum* data size of a single query is **2,000,000**
- Quota deduction<sup>*</sup> is listed as follows:
    + `'min_between'`<sup>#</sup>: stocks * columns * (total minutes / frequency)
    + `'real_time'`: stocks * columns
    + `'day_between'`<sup>^</sup>: stocks * columns * total days
    + `'stock_name'`: stocks
    + `'trade_day'`: 1
    + `'trade_day_between'`<sup>^</sup>: total days
    + `'latest_price'`: 1
    + `'check_quota'`: 0
- <sup>*</sup> Sometimes the API will **not** return certain columns (either connection failure or no records), but the quota will still be deducted
- <sup>#</sup> "total minutes" refers to the **queried interval**, not actual returned number of lines
- <sup>^</sup> "total days" refers to the **queried interval**, not actual returned number if lines

### How convert DataFrame into csv file?
```python
import pandas as pd

rd.to_csv("/your/save/path/csv_file_name.csv")
```
- Note: Chinese characters may not be correctly shown in csv files opened by Excel (It's a problem caused by Excel)