d = {
    "2020-12-16": {
        "name": "Joe"
    }
}

d2 = {
    "2020-12-16": {
        "name2": "Smith"
    }
}

for key, val in d2.items():
    new_dict = d.get(key, {})
    new_dict.update(val)
    d[key] = new_dict
print(d)

d = {
    "2020-12-16": [{
        "name": "Joe"
    }]
}

d2 = {
    "2020-12-16": {
        "name": "Smith"
    }
}

for key, val in d2.items():
    entry = d.get(key, [])
    entry.append(val)

print(d)