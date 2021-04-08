import urllib3

def check_ip():

    http = urllib3.PoolManager()

    url = 'http://checkip.amazonaws.com/'

    r = http.request('GET', url)

    if r:
      current_ip = r.data.decode('utf-8')
      message = f"Your IP is {current_ip}"
      return message
    else:
        return "failed duh"

if __name__ == '__main__':
  current_ip = check_ip()
  print(current_ip)