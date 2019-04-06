#***************************Example 1:************************************

def vote():
    try:
        age = int(input("enter your age:"))
        assert (age>18),"you are not eligible for vote" # if condition is false it will through exception
        print ("you are eligible for vote")
    except Exception as e:
        print("Exception: ",str(e))

vote()

#***************************Example 2:************************************
def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0),"Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
try:
    print (KelvinToFahrenheit(-5))
except AssertionError as e:
    print("Exception: ",str(e))