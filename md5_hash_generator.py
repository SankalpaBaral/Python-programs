import hashlib
import sys

'''
Usages: 

python md5_hash_generator.py anything

'''



string = sys.argv[1]

hash_value = hashlib.md5(string.encode()).hexdigest()

print(hash_value)

