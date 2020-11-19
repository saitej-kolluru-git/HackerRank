#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    """
    Method 01 ----> old fashion

    if((n%2==0 and ((n>=2 and n<=5)) or ((n%2==0)and(n>20)))):
        print("Not Weird")
    else:
        print("Weird")
    """
    
    print(''.join(["Not Weird" if ((n%2==0 and ((n>=2 and n<=5)) or ((n%2==0)and(n>20)))) else "Weird" for i in range(0,1)]))
