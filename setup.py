from distutils.core import setup

requires = [
        'rsa>=3.4.2',
        'requests>=2.11.1'
]

VERSION='0.5'

setup(
  name = 'bankson',
  packages = ['bankson'],
  version = VERSION,
  install_requires=requires,
  description = 'Bankson API client',
  author = 'Codesense',
  author_email = 'niklas@codesense.fi',
  url = 'https://github.com/banksonfi/bankson-python',
  download_url = 'https://github.com/banksonfi/bankson-python/tarball/' + VERSION,
  keywords = ['bankson'], # arbitrary keywords
  classifiers = [],
)
