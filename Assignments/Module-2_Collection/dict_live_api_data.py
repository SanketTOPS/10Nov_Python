"""stdata=[
    {
        "id":101,
        "name":"sanket"
    },
    {
        "id":102,
        "name":"nirav"
    },
    {
        "id":103,
        "name":"ashok"
    }
]"""

#print(stdata)
#print(stdata[1])

#print(stdata[0]["name"])

"""for i in stdata:
    print(i["name"])"""
    
import requests

myurl="https://fakestoreapi.com/products"

req=requests.get(myurl)
data=req.json()
#print(data)

for i in data:
    print(i["title"])
    print(i["price"])
    print(i["rating"]["rate"])
