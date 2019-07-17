"""
Secret Sharing
==============

"""

from setuptools import setup

setup(
    name='bip39-secretsharing',
    version='0.0.1',
    url='https://github.com/seedhodler/secret-sharing',
    license='MIT',
    author='Seedhodler',
    author_email='support@seedhodler.io',
    description="Tools for generating bip39 mnemonics and sharing them using Shamir Secret Sharing. This tool is only for demo purposes",
    packages=[
        'secretsharing',
    ],
    zip_safe=True,
    dependency_links=['https://github.com/trezor/python-mnemonic.git#egg=mnemonic-0.18'],
    install_requires=[
        'pycrypto'
        'mnemonic==0.18'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
