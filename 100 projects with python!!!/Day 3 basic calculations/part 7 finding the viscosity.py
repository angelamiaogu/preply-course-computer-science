materials_data = {
    'water': [1.5, 500],           # Example values for water
    'honey': [100, 10],             # Example values for honey
    'olive oil': [5, 100],          # Example values for olive oil
    'ketchup': [50, 50],            # Example values for ketchup
    'milk': [2, 100],               # Example values for milk
    'molten chocolate': [200, 20]   # Example values for molten chocolate
}

for each in materials_data:
    #print (each)
    stress,rate = materials_data[each]
    v = stress/rate
    print(each,v)
