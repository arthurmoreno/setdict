from setdict import SetDict


def dictmerge(dict_list=[], set_keys=[]):
    set_dict = SetDict()
    for _dict in dict_list:
        set_dict.update(iterable=_dict, set_keys=set_keys)
    return set_dict.store
