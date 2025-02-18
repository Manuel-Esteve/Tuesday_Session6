d = {} # empty dictionary
print(d)

eng_to_spa = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_to_spa)
print(eng_to_spa["one"])
print(eng_to_spa["two"])
eng_to_spa["tree"] = "arbol" # add item into the dict
print(eng_to_spa["tree"])
eng_to_spa.update({"yes": "si", "no": "no"})
print(eng_to_spa)

del eng_to_spa["yes"]
print(eng_to_spa)

print("These are the Spanish words that I know:")
for key in eng_to_spa:
    print(f"{eng_to_spa[key]} means {key}")

print(dir(eng_to_spa))
eng_spa2 = eng_to_spa.copy()
eng_to_spa.clear()
print(eng_spa2)
new_d = eng_spa2.fromkeys(eng_spa2, "YES")
print(new_d)
# get is one of the most useful
print(f"you say car as {eng_spa2.get('car', 'UNKNOWN')}")
print(list(eng_spa2.items()))
print(eng_spa2.pop("one"))
eng_spa2.setdefault("red", "Rojo!!")
print(eng_spa2)