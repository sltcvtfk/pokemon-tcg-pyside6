import json

with open('pokedex.json') as f:
    contenu = json.load(f)
    
    
for i in contenu[0:9] : 
    print(i['name']['french'], i['type'])
    
    

