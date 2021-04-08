import pickle
import os.path
import urllib3



def check_ip():

http = urllib3.PoolManager()

url = 'http://checkip.amazonaws.com/'

r = http.request('GET', url)

  if r:
    current_ip = r.text
    message = f"{current_ip}"
    return current_ip
  else:
    return "failed duh"

if __name__ == '__main__':
  current_ip = check_ip()
  print(current_ip)