import requests

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

payload={}
headers = {
  'X-Auth-Token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGVjNGU0ZjRjYTdmOTIyMmM4MmRhNjYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4ZSJdLCJ0ZW5hbnRJZCI6IjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4NyIsImV4cCI6MTY2ODM1OTQ4OSwiaWF0IjoxNjY4MzU1ODg5LCJqdGkiOiIzNjM2M2EzOS03YzRlLTRiZDctOWYwYy1mNDIzYWM5Njc5NjIiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.LaiFBiGfDZmL2k7DNuLc3SfNQLlGDwj0s-oCuIiDAEQE56YO28de2Peg-g5oGSlYpbTeKQKWjGI8rRDX6bXjvaNlWRNxr0oBYm566owWYxWFQrQFjHnIKtyuQYAwoXY3T-ze2aEUejQn4vka9P80SvF0PwLYQctEkJzfMMEdsNA1cSVTSKguQL8ai33-VQyg8OAy3HMBSCFVDu5nyxfOl5rEssDaYPHg0z1pcSvM88ftceIO_AzApo2Gw6j3QPNU3zSfr3SABp-f5sVA_zxLV0WqK-yRQysrvQy9QmXDO5RbkE5c-fl2mKZY7fDwjXqy9xOakkK-kpv6WNQM0kbYcQ',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("GET", url, verify=False, headers=headers, data=payload)

print(response.text)
