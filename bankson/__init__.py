import rsa
import requests
import time
import base64

from bankson.apikeys import ApiKeys
#from bankson.applications import Applications
#from bankson.bankaccountstatements import BankAccountStatements
#from bankson.bankaccounts import BankAccounts
#from bankson.calls import Calls
from bankson.certificates import Certificates
#from bankson.inboundpayments import InboundPayments
#from bankson.payments import Payments
#from bankson.webhooks import Webhooks

class Bankson(object):

    def __init__(self, **kwargs):
        self.api_key = kwargs['api_key']
        self.private_key = rsa.PrivateKey.load_pkcs1(kwargs['private_key'], 'PEM')
        self.base_url = kwargs.get('base_url', 'https://api.bankson.fi')

        self.apikeys = ApiKeys(self)
        self.certificates = Certificates(self)


    def me(self):
        return self.get('/me')

    def get(self, path):
        r = requests.get(self.base_url + '/' + path, headers=self.headers())
        if r.status_code >= 400:
            raise RequestError('Request error', r)
        return r.json()

    def post(self, path, **kwargs):
        r = requests.post(self.base_url + '/' + path, headers=self.headers(), **kwargs)
        if r.status_code >= 400:
            raise RequestError('Request error', r)
        return r.json()

    def headers(self):
        timestamp = str(int(time.time() * 1000))
        to_sign = self.api_key + timestamp
        signature = base64.b64encode(rsa.sign(to_sign, self.private_key, 'SHA-256'))
        return { 'Authorization': 'BanksonRSA ApiKey=' + self.api_key + ', Timestamp=' + timestamp + ', Signature=' + signature }

class RequestError(Exception):
    def __init__(self, message, response):
        super(RequestError, self).__init__(message)
        if response.headers['content-type'].startswith('application/json'):
            body = response.json()
        else:
            body = { 'error': response.text }
        self.body = body
        self.status = response.status_code
