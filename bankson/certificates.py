class Certificates(object):
    def __init__(self, base):
        self.base = base


    def list(self):
        return self.base.get('/certificates')
