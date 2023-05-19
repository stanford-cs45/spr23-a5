#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
assert run("1 + 2").output == "3"
assert run("5 + 7").output == "12"

###

print("All tests passed!")
