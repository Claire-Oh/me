key = "Da3OYyq578zwEyfahDXRA"
base = "https://www.goodreads.com"
usernum = "115850746" 

Notes:
##add my own Goodread ID

#%%
me_r = ("{b}/user/show/{u}.xml?key={k}".format(b=base, k=key, u=usernum)) 
xml_data = me_r.content 
me = xmltodict.parse(xml_data)

Notes
Line 9: format puts variables into the curly brackets
Line 10: Extensible Markup Language (XML) is a markup language that defines a set of rules 
for encoding documents in a format that is both human-readable and machine-readable.
Line 11: xmltodict is another simple library that aims at making XML feel like working with JSON.
An XML file can be loaded into a Python dict like this: xmltodict.parse(xml_data)

# print(json.dumps(me, indent=2))
shelves = me["GoodreadsResponse"]["user"]["user_shelves"] 
shelf = [x for x in shelves["user_shelf"] if x["name"] == "read"][0] 

Notes
Line 21: selecting an item in a list
Line 22: For each x in "shelves", if x["name"] is equal to the first item in ["read"], 
add it to the list shelf
