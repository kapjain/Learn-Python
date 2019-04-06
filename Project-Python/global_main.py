#import global_config
import global_mod

#print("global main ouput: ",global_config.x)

from global_config import x
def f():
    print("global main ouput: ",x)
f()