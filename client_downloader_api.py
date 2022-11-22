import json
import requests
import datetime

SERVER_DOWNLOADER_URL = '0.0.0.0/download_request'  # change to deployment server ip

headers = {'Content-Type': 'application/json'}

class Client_Downloader:
    def __init__(self, username: str = '', password: str = ''):
        self.username = username
        self.password = password

    def download_request(self, request_type: str, stock_list: list, frequency: str, start_time: datetime, end_time: datetime, columns: list):
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

        response = json.loads(requests.post(SERVER_DOWNLOADER_URL, headers = headers, data = data))
        # error handling
        if response.get('code', -1) != 0:
            print(response.get('msg', 'An error occurred.'))
            return
        
        # can json contain dafaframe?
        dataframe_file = response.get('data', None)
        print(dataframe_file)

if __name__ == '__main__':
    downloader = Client_Downloader('user_test', 'password_test')
    downloader.download_request('user_test', 'password_test', '')
