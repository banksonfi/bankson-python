class BankAccounts(object):
    def __init__(self, base):
        self.base = base

    def list(self):
        return self.base.get('/bankaccounts')

    def create(self, data):
        return self.base.post('/bankaccounts', json=data)

    def remove(self, id):
        return self.base.delete('/bankaccounts/' + str(id))
