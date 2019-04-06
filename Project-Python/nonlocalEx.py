a = 15
def outer_function():
    global a
    a = 5
    def inner_function():
        #nonlocal a # if you don't declare as nonlocal output will be 10, 5 but if you declare as nonlocal output will be 10, 10
        
        a = 10
        print("Inner functionEx: ",a)
    inner_function()
    print("Outer functionEx: ",a)

outer_function()