from setuptools import setup

setup(name='peercoin_rpc',
      version='0.1',
      description='Standardized common API for several cryptocurrency exchanges.',
      url='https://github.com/peerchemist/peercoin_rpc',
      author='Peerchemist',
      author_email='peerchemist@protonmail.ch',
      license='MIT',
      packages=['peercoin_rpc'],
      install_requires=['requests'],
      zip_safe=False)
