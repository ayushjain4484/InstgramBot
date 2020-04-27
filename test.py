
import random
from time import sleep
while False:
    comment = 0
    random_num = random.randint(2, 100)
    if random_num%4 == 1:
        comment = 1
    else:
        comment = 0
    sleep(2)

print('😍😎')