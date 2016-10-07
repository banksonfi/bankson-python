class Certificates(object):
    def __init__(self, base):
        self.base = base


    def list(self):
        return self.base.get('/certificates')

    def upload(self, file, data):
        files = { 'certificate': file }
        return self.base.post('/certificates/upload', files=files, data=data)

    def request(self, file, data):
        return self.base.post('/certificates/request', json=data)

    def remove(self, id):
        return self.base.delete('/certificates/' + str(id))

    def renew(self, id, data):
        return self.base.post('/certificates/' + str(id) + '/renew', json=data)
