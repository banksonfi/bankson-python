class ApiKeys(object):
    def __init__(self, base):
        self.base = base

    def list(self):
        return self.base.get('/apikeys')

    def create(self, data):
        return self.base.post('/apikeys', json=data)

    def remove(self, id):
        return self.base.delete('/apikeys/' + str(id))
