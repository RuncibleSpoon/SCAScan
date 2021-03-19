import pickle
import os.path
import requests



def check_ip():
    r = requests.get("http://checkip.amazonaws.com/")
    print (r.status_code)
    if r:
        current_ip = r.text

        message = f"{current_ip}"
        return current_ip
    else:
    	return "failed duh"

if __name__ == '__main__':
    current_ip = check_ip()
    print(current_ip)