class InboundPayments(object):
    def __init__(self, base):
        self.base = base

    def list(self):
        return self.base.get('/inboundpayments')

    def refresh(self, certificate_id):
        return self.base.post('/inboundpayments', json={ 'certificate_id': certificate_id })
