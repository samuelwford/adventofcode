#!/usr/bin/env python3

import os

def input_filename(filename):
    return os.path.dirname(os.path.realpath(__file__)) + '/inputs/' + filename
    
def read_input(filename):
    with open(input_filename(filename), 'r') as input_file:
        return input_file.readlines()