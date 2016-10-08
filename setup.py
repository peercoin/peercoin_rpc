from setuptools import setup

setup(name='peercoin_rpc',
      version='0.3',
      description='Library to communicate with peercoin daemon via JSON-RPC protocol.',
      url='https://github.com/peerchemist/peercoin_rpc',
      download_url = 'https://github.com/peerchemist/peercoin_rpc/archive/v0.2.tar.gz',
      author='Peerchemist',
      author_email='peerchemist@protonmail.ch',
      license='MIT',
      packages=['peercoin_rpc'],
      install_requires=['requests'],
      keywords = ['peercoin', 'json-rpc', 'cryptocurrency'],
      classifiers=[],
      zip_safe=False)
