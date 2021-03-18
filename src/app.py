import pickle
import os.path
import requests



def check_ip():
    r = requests.get("https://api.myip.com/")
    if r:
        current_ip = r.json()['ip']

        message = f"{current_ip}"
        return current_ip
    else:
    	return "failed"

if __name__ == '__main__':
    current_ip = check_ip()
    print(current_ip)