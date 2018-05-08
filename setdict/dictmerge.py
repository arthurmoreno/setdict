from setdict.setdict import SetDict


def dictmerge(dict_list=[]):
    set_dict = SetDict()
    for _dict in dict_list:
        set_dict.update(iterable=_dict)
    return set_dict.store
