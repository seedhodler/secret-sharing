from mnemonic import Mnemonic
from binascii import hexlify, unhexlify
from .sharing import PlaintextToHexSecretSharer
import base64
import argparse

def generate_mnemonic(*, strength, lang, num_shares, share_threshold):
       mnemo = Mnemonic(lang)
       code = mnemo.generate(strength)
       shares = PlaintextToHexSecretSharer.split_secret(code, share_threshold, num_shares)
       print(f'MNEMONIC: {code}')
       print_shares(shares)

def recover_mnemonic(*, shares):
    print_shares(shares)
    code = PlaintextToHexSecretSharer.recover_secret(shares)
    print(f'MNEMONIC: {code}')

def print_shares(shares):
    for idx, share in enumerate(shares):
            print(f'SHARE-{idx}: {share}')

        
def __main__():
    parser = argparse.ArgumentParser()
    
    # Generate 
    parser.add_argument('-g', '--generate', default=True)
    parser.add_argument('-m', '--number-of-shares', default=5, type=int)
    parser.add_argument('-n', '--share-threshold', default=3, type=int)
    parser.add_argument('-s', '--strength', default=128, choices=[128, 160, 192, 224, 256], type=int)
    parser.add_argument('-l', '--lang', default="english")

    # Recover
    parser.add_argument('-r', '--recover', default=False)
    parser.add_argument('--shares', nargs='+')
    args = parser.parse_args()

    if (args.share_threshold > args.number_of_shares):
        raise Exception("share-threshold should be <- number-of-shares")

    if args.recover:
        recover_mnemonic(shares=args.shares)
    else:
        generate_mnemonic(strength=args.strength, lang=args.lang, num_shares=args.number_of_shares, share_threshold=args.share_threshold)

if __name__ == "__main__":
    __main__()