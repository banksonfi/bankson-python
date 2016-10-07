from distutils.core import setup

requires = [
        'rsa>=3.4.2',
        'requests>=2.11.1'
]

setup(
  name = 'bankson',
  packages = ['bankson'], # this must be the same as the name above
  version = '0.1',
  install_requires=requires,
  description = 'Bankson API client',
  author = 'Codesense',
  author_email = 'niklas@codesense.fi',
  url = 'https://github.com/banksonfi/bankson-python', # use the URL to the github repo
  download_url = 'https://github.com/banksonfi/bankson-python/tarball/0.1', # I'll explain this in a second
  keywords = ['bankson'], # arbitrary keywords
  classifiers = [],
)
