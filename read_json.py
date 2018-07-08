import json

#obrim el fitxer en mode lectura
with open("exemple_json.json","r") as f:
    #carreguem el contingut del fitxer
    #ens retornara directament un diccionari
    json_as_dict = json.load(f)

#mostrem el cntingut de la variable
print("Contingut: \n{}".format(json_as_dict))
#comprovem el tipus de la variable
print("Tipus de la variable: {}".format(type(json_as_dict)))