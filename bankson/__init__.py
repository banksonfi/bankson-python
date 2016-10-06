import rsa
import requests
import time
import base64

class Bankson(object):

    def __init__(self, **kwargs):
        self.api_key = kwargs['api_key']
        self.private_key = rsa.PrivateKey.load_pkcs1(kwargs['private_key'], 'PEM')
        self.base_url = kwargs.get('base_url', 'https://api.bankson.fi')

    def me(self):
        return self.get('/me')

    def get(self, path):
        r = requests.get(self.base_url + '/' + path, headers=self.headers())
        return r.json()

    def headers(self):
        timestamp = str(int(time.time() * 1000))
        to_sign = self.api_key + timestamp
        signature = base64.b64encode(rsa.sign(to_sign, self.private_key, 'SHA-256'))
        return { 'Authorization': 'BanksonRSA ApiKey=' + self.api_key + ', Timestamp=' + timestamp + ', Signature=' + signature }

