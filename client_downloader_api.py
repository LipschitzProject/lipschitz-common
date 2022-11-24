import json
import requests
import pandas as pd
from datetime import datetime

SERVER_DOWNLOADER_URL = 'http://127.0.0.1:8002/download_request'  # change to deployment server ip

headers = {'Content-Type': 'application/json'}

class Client_Downloader:
    def __init__(self, username: str = '', password: str = ''):
        self.username = username
        self.password = password

    def validate_datetime(self, datetime_str):
        try:
            datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
        except ValueError:
            return False
        return True
    
    def download_request(self, request_type: str, stock_list: list, frequency: str, start_time: str, end_time: str, columns: list):
        if (start_time and not self.validate_datetime(start_time)) or (end_time and not self.validate_datetime(end_time)):
            print('Wrong datetime format. Should be yyyy-mm-dd hh:mm')
            return
        
        data = {
            'username': self.username,
            'password': self.password,
            'request_type': request_type,
            'stock_list': stock_list,
            'frequency': frequency,
            'start_time': start_time,
            'end_time': end_time,
            'columns': columns
        }

        response = requests.post(SERVER_DOWNLOADER_URL, headers = headers, data = json.dumps(data))
        # print(response, type(response))
        response = json.loads(response.text)
        # error handling
        if response.get('code', 0) != 0:
            print(response.get('msg', 'An error occurred.'))
            return
        
        returned_file_str = response.get('data', '')
        if returned_file_str:
            # print(returned_file_str)
            if request_type == 'trade_day':
                is_trade_day = bool(returned_file_str)
                print(is_trade_day)
                return is_trade_day
            elif request_type == 'trade_day_between':
                trade_days = returned_file_str.split("|")
                print(trade_days, type(trade_days))
                return trade_days
            elif request_type == 'latest_price':
                latest_price = float(returned_file_str)
                print(latest_price)
                return latest_price
            else:
                dataframe_file = pd.read_json(returned_file_str, orient='table')
                print(dataframe_file)
                return dataframe_file
        else:
            print('The server returns no data.')

if __name__ == '__main__':
    downloader = Client_Downloader('test_user', '123456')
    # downloader.download_request('min_between', ['885779.TI'], '1', '1900-01-01 00:00', '1900-01-01 00:00', ['open', 'high', 'low', 'close', 'avgPrice', 'volume'])
    df = downloader.download_request('min_between', ['885779.TI'], '1', '2022-11-24 10:14', '2022-11-24 10:15', ['open', 'high', 'low', 'close', 'avgPrice', 'volume'])
    print()
    df = downloader.download_request('real_time', ['885779.TI'], '', '', '', ['open', 'high', 'low', 'close', 'avgPrice', 'volume'])
    print()
    df = downloader.download_request('day_between', ['885779.TI'], '', '2022-11-21 10:00', '2022-11-24 00:00', ['open', 'high', 'low', 'close', 'avgPrice', 'volume'])
    print()
    df = downloader.download_request('stock_name', ['885779.TI', '864005.TI'], '', '', '', [])
    print()
    df = downloader.download_request('trade_day', [], '', '2022-11-24 10:14', '', [])
    print()
    df = downloader.download_request('trade_day_between', [], '', '2022-11-21 10:14', '2022-11-24 10:15', [])
    print()
    df = downloader.download_request('latest_price', ['885779.TI'], '', '', '', [])
    # df.to_csv("/home/wzhang/workspace/test2.csv")
