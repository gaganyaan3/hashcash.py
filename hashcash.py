import hashlib
import argparse
import time
start_time = time.time()
parser = argparse.ArgumentParser(description='hashcash parameters')
parser.add_argument('--data', type=str,
                    help='Data in text')

# parser.add_argument('--hashalgo', type=str,
#                     help='hash algorithm',default="sha256")

parser.add_argument('--difficulty', type=int,
                    help='difficulty is find zero*difficulty at the end of hash', default=1)

args = parser.parse_args()

data = args.data
# hashalgo = args.hashalgo
difficulty= args.difficulty


def hashcash(data, difficulty):
    hashdata=hashlib.sha512(data.encode('utf-8')).hexdigest().strip()[difficulty*-1:]
    i=0
    while True:
      i = i+1
      data_inc = data+str(i)
      hashdata=hashlib.sha512(data_inc.encode('utf-8')).hexdigest()
      hashdata_strip=hashdata.strip()[difficulty*-1:]

      if(hashdata_strip == "0"*difficulty):
        print("Data: "+data)
        print("Data_inc: "+data_inc)
        print("Difficulty: "+str(difficulty))
        print("Hash: "+hashdata)
        print("Time(seconds): %s" % (time.time() - start_time))
        exit()

hashcash(data,difficulty)

# python3 hashcash.py --data "example data123"  --difficulty 4