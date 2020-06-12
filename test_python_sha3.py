#! usr/bin/env python

# Use pysha3 from pypi for testing
import random
import string
import sha3
import hashlib 

import python_sha3

def main():
  # Our library
  python_sha3_functions = [ python_sha3.sha3_224, python_sha3.sha3_256,
                            python_sha3.sha3_384, python_sha3.sha3_512]
  # pysha3
  pysha3_hashes = [hashlib.sha3_224, hashlib.sha3_256, hashlib.sha3_384, hashlib.sha3_512]
  x = ""
  for a in range(500):
    x = x + random.choice(string.ascii_letters);
    print("testing for: " + x )
    for i,j in zip(python_sha3_functions, pysha3_hashes):
      if i(x).hexdigest() != j(x).hexdigest():
        print (x)
        return
        
if __name__ == '__main__':
  main()
