#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

assert run("1 + 1").output == "2"
assert run("1 - 1").output == "0"
assert run("2 \* 2").output == "4"
assert run("6 / 3").output == "2"
assert run("34 plus 7").exit_status != 0
###

print("All tests passed!")
