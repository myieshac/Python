#Q: Generate a Random Number using random(), randint(), sample()[import random]

import random
import numpy as np
no = random.random()
print(no)
print(np.random.randint(low=4,high=15,size=7))
print(random.randint(2,20))
list1=[1,2,3,4,5,6,7,8]
print(random.sample(list1,2))
