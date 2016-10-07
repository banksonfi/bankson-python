# Bankson.fi Python client

API documentation: [Official bankson.fi documentation](http://docs.bankson.fi)

## Installation

```
pip install bankson
```

## Usage

First create an API key in [Bankson settings](https://app.bankson.fi/settings/apikeys) and save the private key locally.

```python
from bankson import Bankson, RequestError

with open('/path/to/private_key_file') as privatefile:
    keydata = privatefile.read()
client = Bankson(api_key='<api key uuid>', private_key=keydata)

try:
    print client.inboundpayments.list()
except RequestError as err:
    print 'Request error'
    print err.status
    print err.body
```

The snippet above will list all inbound reference payments. For more examples see [Official bankson.fi documentation](http://docs.bankson.fi)

## Test mode

To use Bankson API in test mode specify `test=True` while initializing:

```python
client = Bankson(api_key='', private_key='', test=True)
```

## License

The MIT License
