stdata={
    "id":1,
    "name":"sanket",
    "mobile":9724799469,
    "city":"rajkot"
}
"""print(stdata)
print(stdata["name"])
print(stdata.get("city"))
print(len(stdata))"""


"""print(stdata)
stdata["city"]="baroda"
stdata["sub"]="python"""

"""print(stdata)
print(stdata.keys())
print(stdata.values())"""

"""for i in stdata:
    print(i)
"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""


"""for i,j in stdata.items():
    #print(i,j)
    print(f"Key={i} and Value={j}")"""
    

"""if 'name' in stdata:
    print("Yes...")
else:
    print("Noo")"""
    
"""if 'sanket' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""
    
# -------------------------- #
print(stdata)
#stdata.pop("mobile")
#del stdata["name"]
#del stdata
#stdata.clear()

#newdata=stdata.copy()
#print(newdata)