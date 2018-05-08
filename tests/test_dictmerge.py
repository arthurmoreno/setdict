import pytest

from setdict.dictmerge import dictmerge
from tests.constants import DICTA, DICTB, DICTC, DICT_RESULT


def test_dictmerge():
    dict_list = [DICTA, DICTB, DICTC]
    merged_dict = dictmerge(dict_list)
    assert DICT_RESULT.keys() == merged_dict.keys()
    for key in merged_dict.keys():
        merged_dict[key].sort()
        DICT_RESULT[key].sort()
    assert merged_dict == DICT_RESULT
