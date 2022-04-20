import sys
import pytest

sys.path.append("../")
from main import replace_enter


# < ------------- 以下がテストコード -------------- >
def test_correct_arguments():
    tar_str = 'Hello.\n My name is Taro.\n'
    char_before_rep = '\n'
    char_after_rep = ' '

    expect_str = "Hello. My name is Taro. "
    assert replace_enter(tar_str, char_before_rep, char_after_rep) == expect_str