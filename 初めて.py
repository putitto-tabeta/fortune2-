#初めて
print ("hello world")

import random
fortune=random.randint(1,10)
print (fortune)

if fortune==10:
    print ("大吉")

elif fortune>=8:
    print ("中吉")

elif fortune>=5:
    print ("小吉")

elif fortune>=2:
     print ("凶")

else:
     print ("大凶")      


