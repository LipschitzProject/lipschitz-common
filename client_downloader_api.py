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
    
    def download_request(self, request_type: str = '', stock_list: list = [], frequency: str = '', start_time: str = '', end_time: str = '', columns: list = []):
        if (start_time and not self.validate_datetime(start_time)) or (end_time and not self.validate_datetime(end_time)):
            print('Wrong datetime format. Should be yyyy-mm-dd hh:mm')
            return None, None
        
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
            print(response.get('msg', 'An unknown error occurred.'))
            return None, None
        
        quota_str = response.get('quota', '')
        if quota_str:
            quota = int(quota_str)
            print('quota remaining:', quota)
        else:
            quota = None
            print('The server returns no quota info.')

        returned_data_str = response.get('data', '')
        if returned_data_str:
            # print(returned_file_str)
            if request_type == 'trade_day':
                returned_data = bool(returned_data_str)
            elif request_type == 'trade_day_between':
                returned_data = returned_data_str.split("|")
            elif request_type == 'latest_price':
                returned_data = float(returned_data_str)
            else:
                returned_data = pd.read_json(returned_data_str, orient='table')
        else:
            returned_data = None
            print('The server returns no data.')
        
        return returned_data, quota

if __name__ == '__main__':
    downloader = Client_Downloader('test_user', '123456')
    rd, quota = downloader.download_request(request_type='check_quota')
    print(rd)
    print(quota)
    # rd.to_csv("/home/wzhang/workspace/test3.csv")
