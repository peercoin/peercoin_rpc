from setuptools import setup

setup(name='peercoin_rpc',
      version='0.55.1',
      description='Library to communicate with peercoin daemon via JSON-RPC protocol.',
      url='https://github.com/peerchemist/peercoin_rpc',
      author='Peerchemist',
      author_email='peerchemist@protonmail.ch',
      license='MIT',
      packages=['peercoin_rpc'],
      install_requires=['requests'],
      keywords=['peercoin', 'json-rpc', 'cryptocurrency'],
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6'
      ],
      platforms="any")
