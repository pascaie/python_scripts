# random module example
# exit() example

import random
import sys

for i in range(5):
    n = random.randint(1,10)
    print(n)
    if n > 9:
        print('Limit exceeded')
        sys.exit()
