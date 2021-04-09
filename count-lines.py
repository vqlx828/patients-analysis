"""This module counts the number of lines in standard input
Input: any string from the system standard input
Output: a string with the total number of lines
"""

import sys

count = 0

for line in sys.stdin:
	count += 1

print(count, "lines in standard input")


