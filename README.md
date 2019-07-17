# bip39-secretsharing

### Disclaimer
> <emp>This project is a proof of concept and in *no way should EVER be used* for anything EVER. </emp>

### About

This project is a proof of concept for generating BIP39 Mnemonics and splitting them using Shamir Secret sharing. It aims to be a simple python command line utility. 

It sources code from:
- https://github.com/trezor/python-mnemonic
- https://github.com/blockstack/secret-sharing


### Setup
Requires python3 and pip

- `$ git clone https://github.com/seedhodler/secret-sharing.git`
- Create new python virtual environment
 - `$ python -m venv .venv`
 - `$ source .venv/bin/activate`
- Install module into python environment
 - `$ python setup.py install`
 
### Help

- `$ python -m secretsharing --help`

```
  -h, --help            show this help message and exit
  -g GENERATE, --generate GENERATE
  -m NUMBER_OF_SHARES, --number-of-shares NUMBER_OF_SHARES
  -n SHARE_THRESHOLD, --share-threshold SHARE_THRESHOLD
  -s {128,160,192,224,256}, --strength {128,160,192,224,256}
  -l LANG, --lang LANG
  -r RECOVER, --recover RECOVER
  --shares SHARES [SHARES ...]
```

### Usage

#### Generate MNEMONIC:
```
$ python -m secretsharing --generate=True --number-of-shares=3 --share-threshold=2 --strength=192 --lang=english
```

Output:
```
MNEMONIC: method filter spray skate wink glass logic depend write page cup spray near silly remain unit giggle jealous
SHARE-0: 1-78ca015d89f2b9fb66...
SHARE-1: 2-719402bb13e573f6cc0deead5e802a065626...
SHARE-2: 3-6a5e04189dd82df23214e6040dc03f098139...
```
<small>Note: truncated shares due to verbosity</small>

#### Recover MNEMONIC:
```
$ python -m secretsharing --recover=True --shares "2-719402bb13e573f6cc0deead5e802a065626" "3-6a5e04189dd82df23214e6040dc03f098139"
```

Output:
```
SHARE-0: 2-719402bb13e57...
SHARE-1: 3-6a5e04189dd82df2321...
MNEMONIC: method filter spray skate wink glass logic depend write page cup spray near silly remain unit giggle jealous
```
<small>Note: truncated shares due to verbosity</small>