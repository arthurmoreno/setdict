# SetDict

If you want to merge Python Dicts into a single one, but want some keys to have set property (but remains as a list). Than this package is for you.

The add_to_set method in SetDict class is very similar to MongoDB $AddToSet command.

## Instalation

Just install with pip
```
pip install -e git+https://github.com/arthurmoreno/setdict.git#egg=SetDict
```

## Usage

Supose that you have this three dictionaries:
```
dictA = {
    'id': 0,
    'weapons': ['sword', 'spear']
}

dictB = {
    'id': 0,
    'weapons': ['bow', 'crossbow'],
    'equipments': ['cloak']
}

dictC = {
    'id': 0,
    'equipments': ['hood']
}
```

To merge this dicts just make:

```
>>> dict_list = [dictA, dictB, dictC]
>>> set_keys = ['weapons', 'equipments']
>>> merged_dict = dictmerge(dict_list, set_keys)
>>> merged_dict

{
    'id': 0,
    'weapons': ['bow', 'crossbow', 'spear', 'sword'],
    'equipments': ['cloak', 'hood']
}

```




