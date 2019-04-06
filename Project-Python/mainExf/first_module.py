"""
When we run a file directly either by right click or from command line by python -m command. System always assign __main__ for that module.

"""

#if __name__ == '__main__':
#    print("Run directly")
#else:
#    print("Run by import module")

print("This will run always")

def main():
    print("First module's main method")
    
if __name__ == '__main__':
    main()

def add():
    pass