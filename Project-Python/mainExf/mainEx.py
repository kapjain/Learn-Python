#from . import first_module # when the are in same label with same directory
import sys
def main(a,b):
    return a*b

if __name__ == '__main__':
    multiply  = main(int(sys.argv[1]),int(sys.argv[2]))
    print(multiply)
    
if __name__ == '__main__':
    multiply  = main(int(sys.argv[1]),int(sys.argv[2]))
    print(multiply)