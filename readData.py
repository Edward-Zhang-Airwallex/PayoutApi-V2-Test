import os
import csv
import requests
import json


def get_token():
    headers1 = {
        'Content-Type': 'application/json',
        'x-client-id': '9rnbaw6bTbSxDx4QagRXDw',
        'x-api-key': 'f45c8feabd0bbf2e55b18c089d5d9584ff92166dbd5586cb6603f980f8e9ffc0639ae89c0c74697ebdfa4c0a90805b6c'
    }
    url_token = "https://api-staging.airwallex.com/api/v1/authentication/login?api_key=f45c8feabd0bbf2e55b18c089d5d9" \
                "584ff92166dbd5586cb6603f980f8e9ffc0639ae89c0c74697ebdfa4c0a90805b6c&client_id=9rnbaw6bTbSxDx4QagRXDw"
    headers2 = {
        'Content-Type': 'application/json',
        'Authorization': ''
    }
    r_token = requests.request("POST", url_token, headers=headers1, data={})
    header = json.loads(r_token.text)['token']
    headers2['Authorization'] = 'Bearer ' + header
    return headers2


TOKEN = get_token()


def read(path):
    """
    read csv from path and return condition list data
    """
    data = []
    row_number = 1
    with open(path, newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        for row in csv_reader:
            if row_number == 1:
                row_number += 1
                continue
            # original csv file order in entity_type,bank_country_code,account_currency, payment_method,
            # local_clearing_system. Here we need to reorder in entity_type, payment_method, account_currency,
            # bank_country_code
            if row[3] == 'LOCAL SWIFT':
                condition_1 = [row[0], 'LOCAL', row[2], row[1], row[4]]
                data.append(condition_1)
                condition_2 = [row[0], 'SWIFT', row[2], row[1], row[4]]
                data.append(condition_2)
            else:
                condition = [row[0], row[3], row[2], row[1], row[4]]
                data.append(condition)
            row_number += 1
    return data


def str_data(data):
    str_output = []
    for d in data:
        str_output.append(str(d))
    return str_output


URL = 'https://api-staging.airwallex.com'


class basic_tool():

    @staticmethod
    def option():
        env_dist = os.environ
        if 'URL' in env_dist:
            return env_dist['URL'] + '/api/v1/beneficiary_api_schemas/generate'
        else:
            return URL + '/api/v1/beneficiary_api_schemas/generate'

    @classmethod
    def sendRequest(self, data):
        url = self.option()
        r = requests.post(url, data=json.dumps(data), headers=TOKEN)
        return r
