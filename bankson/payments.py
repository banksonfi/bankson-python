class Payments(object):
    def __init__(self, base):
        self.base = base

    def list(self):
        return self.base.get('/payments')

    def create(self, data, bank_account):
        data['from'] = bank_account
        return self.base.post('/payments', json=data)

    def refresh(self):
        return self.base.post('/payments/feedback')
