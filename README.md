# SetDict
[![PyPI version](https://badge.fury.io/py/set-dict.svg)](https://badge.fury.io/py/set-dict)

If you want to merge Python Dicts into a single one, but want some keys to have set property (but remains as a list). Than this package is for you.

The add_to_set method in SetDict class is very similar to MongoDB $AddToSet command.

## Instalation

Just install with pip
```
pip install set-dict
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
>>> from setdict.dictmerge import dictmerge
>>> dict_list = [dictA, dictB, dictC]
>>> merged_dict = dictmerge(dict_list)
>>> merged_dict

{
    'id': 0,
    'weapons': ['bow', 'crossbow', 'spear', 'sword'],
    'equipments': ['cloak', 'hood']
}

```




