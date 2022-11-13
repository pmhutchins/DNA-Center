import requests
import json
from getpass import getpass
from pprint import pprint
from requests.auth import HTTPBasicAuth

username = input("Please provide your username: ")
password = getpass("Please enter your password: ")

BASEURL = 'https://sandboxdnac.cisco.com'
authAPI = "/dna/system/api/v1/auth/token"
deviceListAPI = "/dna/intent/api/v1/network-device"

authPayload={}
authHeaders = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

dnaAuth = BASEURL + authAPI

authResponse = requests.post(dnaAuth, auth=HTTPBasicAuth(username, password), verify=False, headers=authHeaders, data=authPayload)

tokenJSON = authResponse.json()

TOKEN = tokenJSON['Token']

dnaDeviceList = BASEURL + deviceListAPI

getPayload={}
getHeaders = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-Auth-Token': TOKEN
}

getResponse = requests.get(dnaDeviceList, verify=False, headers=getHeaders, data=getPayload)

getJSON = getResponse.json()

pprint(getJSON)
