import os
import sys

from flask import Flask, request, render_template
from requests import get, post


app = Flask('__main__')
SERVER_API_ADDRESS = ''  # what is the server API address?

@app.route('/')
def downloader():
    context = {}
    return render_template('index.html', context=context)

@app.route('/download', methods = ['POST'])
def proxy():
    return "success!"
    return post(url=f'{SERVER_API_ADDRESS}',
                 headers = {},
                 data=request.get_data()
                ).content

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 8002.
    port_num = 8002
    if len(sys.argv) > 1:
        port_num = int(sys.argv[1])
    port = int(os.environ.get('PORT', port_num))
    app.run(host = '0.0.0.0', port = port)