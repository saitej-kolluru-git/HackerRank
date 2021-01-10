#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    
    x=Counter(sorted(s))
    for i in x.most_common(3):
        print(' '.join(map(str,i)))
