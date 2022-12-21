from time import sleep
import requests

ip_addresses = []
ip_with_country = {}
with open('ips.txt', 'r+') as f:
    ip_addresses = [line.strip() for line in f]


def get_location(ip_list):
    for ip in ip_list:
        response = requests.get(f'http://www.geoplugin.net/json.gp?ip={ip}', verify=False).json()
        print(f'IP address is {ip} and country is {response.get("geoplugin_countryName")}')
        ip_with_country[ip] = response.get("geoplugin_countryName")
        print(ip_with_country)
        sleep(5)
        
get_location(ip_addresses)