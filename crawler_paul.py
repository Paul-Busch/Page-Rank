import requests

r = requests.get("https://www.math.kit.edu", verify=False)
print(r.text)