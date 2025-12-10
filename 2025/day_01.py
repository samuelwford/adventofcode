#!/usr/bin/env python3

import utils

turns = [(line[0], int(line[1:])) for line in utils.read_input('day_01.txt')]
print("turns:", turns)