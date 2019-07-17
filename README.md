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

Generate MNEMONIC:
- `$ python -m secretsharing --generate=True --number-of-shares=3 --share-threshold=2 --strength=192 --lang=english`

```output
MNEMONIC: method filter spray skate wink glass logic depend write page cup spray near silly remain unit giggle jealous
SHARE-0: 1-78ca015d89f2b9fb6606f756af4015032b130d0b545cefc154402f8cbc1d929a77bfd47d874cb9aadbba5be183f07cb66ba8968a1fb4c3405148f0bf48beaf6e08bd4d0379ff6b3b152c90d83c693a3372d3a1a5cc95afd26e02125a0a9ac243290f19db27d3cab3a3d85c9f6cad51f123c89047dcfb7d753787ea8c357703be6c7457e765e5bbb42dfe252a67e508e2a2d029336a7a3218f398828205a2aeca
SHARE-1: 2-719402bb13e573f6cc0deead5e802a0656261a16a8b9df82a8805f19783b2534ef7fa8fb0e997355b774b7c307e0f96cd7512d143f698680a291e17e917d5edc117a9a06f3fecc2f2eefc77d8643f872f07d60bd2f5523a877b26b6f28eeb839d3d7b706034658a15a68566a5cde00a529e03a84355243f23afb028b91eeb684f12a727d8965537230c4b0ab6ee0580a40f3a4373c3be7f89e19f05c81da4701
SHARE-2: 3-6a5e04189dd82df23214e6040dc03f0981392721fd16cf43fcc08ea63458b7cf673f7d7895e62d00932f13a48bd1762342f9c39e5f1e49c0f3dad23dda3c0e4a1a37e70a6dfe2d2348b2fe22d01eb6b26e271fd49214977e8162c4844742ae307ea05430deb8e68f10f850354d0eaf592ff7e4c08da90a6f3e6e1a8aee66694b75e08d13ace4eb30338b3c2c75dba731df171f3b0dfd9dd8489b5e36fe11df38
```

Recover MNEMONIC:
- `$ python -m secretsharing --recover=True --shares "2-719402bb13e573f6cc0deead5e802a0656261a16a8b9df82a8805f19783b2534ef7fa8fb0e997355b774b7c307e0f96cd7512d143f698680a291e17e917d5edc117a9a06f3fecc2f2eefc77d8643f872f07d60bd2f5523a877b26b6f28eeb839d3d7b706034658a15a68566a5cde00a529e03a84355243f23afb028b91eeb684f12a727d8965537230c4b0ab6ee0580a40f3a4373c3be7f89e19f05c81da4701" "3-6a5e04189dd82df23214e6040dc03f0981392721fd16cf43fcc08ea63458b7cf673f7d7895e62d00932f13a48bd1762342f9c39e5f1e49c0f3dad23dda3c0e4a1a37e70a6dfe2d2348b2fe22d01eb6b26e271fd49214977e8162c4844742ae307ea05430deb8e68f10f850354d0eaf592ff7e4c08da90a6f3e6e1a8aee66694b75e08d13ace4eb30338b3c2c75dba731df171f3b0dfd9dd8489b5e36fe11df38"`

```output
SHARE-0: 2-719402bb13e573f6cc0deead5e802a0656261a16a8b9df82a8805f19783b2534ef7fa8fb0e997355b774b7c307e0f96cd7512d143f698680a291e17e917d5edc117a9a06f3fecc2f2eefc77d8643f872f07d60bd2f5523a877b26b6f28eeb839d3d7b706034658a15a68566a5cde00a529e03a84355243f23afb028b91eeb684f12a727d8965537230c4b0ab6ee0580a40f3a4373c3be7f89e19f05c81da4701
SHARE-1: 3-6a5e04189dd82df23214e6040dc03f0981392721fd16cf43fcc08ea63458b7cf673f7d7895e62d00932f13a48bd1762342f9c39e5f1e49c0f3dad23dda3c0e4a1a37e70a6dfe2d2348b2fe22d01eb6b26e271fd49214977e8162c4844742ae307ea05430deb8e68f10f850354d0eaf592ff7e4c08da90a6f3e6e1a8aee66694b75e08d13ace4eb30338b3c2c75dba731df171f3b0dfd9dd8489b5e36fe11df38
MNEMONIC: method filter spray skate wink glass logic depend write page cup spray near silly remain unit giggle jealous
```