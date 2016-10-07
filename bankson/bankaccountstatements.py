class BankAccountStatements(object):
    def __init__(self, base):
        self.base = base

    def list(self):
        return self.base.get('/bankaccountstatements')

    def refresh(self, certificate_id):
        return self.base.post('/bankaccountstatements', json={'certificate_id': certificate_id})

    def get(self, id, format='json'):
        accept = 'application/json'
        if format == 'xml':
            accept = 'text/xml'
        if format == 'html':
            accept = 'text/html'
        if format == 'text':
            accept = 'text/plain'
        if format == 'pdf':
            accept = 'application/pdf'
        return self.base.get('/bankaccountstatements/' + str(id), headers = { 'Accept': accept })
