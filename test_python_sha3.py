#! usr/bin/env python

# Use pysha3 from pypi for testing
import sha3
import hashlib 

import python_sha3

def main():
  # My implementation
  python_sha3_functions = [ python_sha3.sha3_224, python_sha3.sha3_256,
                            python_sha3.sha3_384, python_sha3.sha3_512]
  # pysha3
  pysha3_hashes = [hashlib.sha3_224, hashlib.sha3_256, hashlib.sha3_384, hashlib.sha3_512]
  x = ""
  print(python_sha3.sha3_512(x).hexdigest())
  # instance = python_sha3.sha3_384(x)
  # instance = python_sha3.sha3_256(x)
  # instance = python_sha3.sha3_224(x).hexdigest()
  # M = (len(x.encode('hex')) * 4, x.encode('hex'))
  # print(M)
  # print(instance.pad10star1(M, 1152))
  # print(len(instance.pad10star1(M, 1152)))
  print(python_sha3.sha3_256(x).hexdigest())
        
if __name__ == '__main__':
  main()
