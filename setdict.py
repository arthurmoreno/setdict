import collections

from utils import encode_list, decode_list


class SetDict(collections.MutableMapping):
    """A dictionary that have add to set behavior on primary keys"""

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        return self.store[self.__keytransform__(key)]

    def __setitem__(self, key, value):
        self.store[self.__keytransform__(key)] = value

    def __delitem__(self, key):
        del self.store[self.__keytransform__(key)]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __str__(self):
        return str(self.store)

    def __repr__(self):
        return repr(self.store)

    def __keytransform__(self, key):
        return key

    def add_to_set(self, key, value):
        if key in self.store.keys():
            if type(self.store[key]) == list:
                hashed_set = set(encode_list(self.store[key]))
                hashed_obj = obj_to_hash(value)
                hashed_set.add(hashed_obj)
                self.store[key] = decode_list(list(hashed_set))
            elif self.store[key] != value:
                new_list = [self.store[key], value]
                list.sort(new_list)
                self.store[key] = new_list
        else:
            self.store[key] = value
    
    def update(self, iterable=None, set_keys=[]):
        if isinstance(iterable, collections.MutableMapping):
            for key, value in iterable.items():
                if key in set_keys:
                    self.add_to_set(key, value)
                else:
                    self.store[key] = value
        else:
            raise Exception('akushefkuashef')
