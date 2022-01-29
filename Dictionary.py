mydict = {"key1": "Value1", "Key2": "value2"}
#print(mydict["key1"])
print(mydict["key1"])
print(mydict.get("key1"))
mydict["key3"]="value3"
print(mydict)


States=["TN","KA","AP"]
HQs=["Chennai","Bglr", "Hyd"]

Mapping=dict(zip(States, HQs))
print(Mapping)