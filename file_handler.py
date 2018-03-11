import os.path
import shutil

import requests


def download_file(file_name, url):
    split = url.split('/')
    original_file_name = split[len(split) - 1]
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        print('Downloaded ' + file_name)
        with open(original_file_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
            os.rename('./' + original_file_name, './' + file_name)


def download_csv_sheet(csv_sheet_name, url):
    if not os.path.exists('./' + csv_sheet_name):
        download_file(
            csv_sheet_name,
            url
        )
