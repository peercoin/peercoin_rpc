from setuptools import setup
from os import path
from io import open

classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Financial and Insurance Industry',
  'Programming Language :: Python',
  'Operating System :: OS Independent',
  'Natural Language :: English',
  'License :: OSI Approved :: MIT License'
]

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='peercoin_rpc',
      version='0.59',
      description='Library to communicate with peercoin daemon via JSON-RPC protocol.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/peercoin/peercoin_rpc',
      author='Peerchemist',
      author_email='peerchemist@protonmail.ch',
      license='MIT',
      packages=['peercoin_rpc'],
      install_requires=['requests'],
      keywords=['peercoin', 'json-rpc', 'cryptocurrency', 'blockchain'],
      classifiers=classifiers,
      platforms="any")
