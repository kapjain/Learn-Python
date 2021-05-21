a = 15
def outer_function():
    a = 5
    def inner_function():
        a = 10
        print("1. functionEx: ",a)
    inner_function()
    print("2. functionEx: ",a)

outer_function()
print("3. functionEx: ",a)


a = 15
def outer_function():
    global a
    a = 5
    def inner_function():
        a = 10
        print("1. functionEx: ",a)
    inner_function()
    print("2. functionEx: ",a)

outer_function()
print("3. functionEx: ",a)

a = 15
def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("1. functionEx: ",a)
    inner_function()
    print("2. functionEx: ",a)

outer_function()
print("3. functionEx: ",a)


a = 15
def outer_function():
    a = 5
    def inner_function():
        global a
        a = 10
        print("1. functionEx: ",a)
    inner_function()    
    print("2. functionEx: ",a)

outer_function()
print("3. functionEx: ",a)

# Note: at a time , you can use either nonlocal or global keyword. otherwise it will throw error
a = 15
def outer_function():
    global a
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("1. functionEx: ",a)
    inner_function()
    print("2. functionEx: ",a)

outer_function()
print("3. functionEx: ",a)
