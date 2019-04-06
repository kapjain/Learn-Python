






#Write a Python program to find the single element in a list where every element appears three times except for one.
def single_nbr(lst):
    n_set = set(lst)
    for i in n_set:
        if lst.count(i) == 1:
            return i
    return None
print(single_nbr([5, 3, 4, 3, 5, 5, 3,4]))


#Write a Python program to check if a given positive integer is a power of two
def check_pow_two(n):
    if n<0:
        raise Exception("not a positive integer")
    for i in range(0,n):
        if n == pow(2,i):
            return True
        elif n < pow(2,i):
            return False

print(check_pow_two(64))
print(check_pow_two(65))



def check_pow_of(n,powof=2):
    if n<0:
        raise Exception("not a positive integer")
    for i in range(0,n):
        if n == pow(powof,i):
            return True
        elif n < pow(powof,i):
            return False

print(check_pow_of(27,3))
print(check_pow_of(65))

#Write a Python program to find missing number from a list.
def missing_number(num_list):
    return sum(range(num_list[0],num_list[-1]+1)) - sum(num_list)
print(missing_number([1,2,3,4,6,7,8]))
print(missing_number([10,11,12,14,15,16,17]))

#Write a Python program to find missing numbers from a list.
def missing_numbers(num_list):
    original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
    num_list = set(num_list)
    return (list(num_list ^ set(original_list)))

print(missing_numbers([1,2,3,4,6,7,10]))
print(missing_numbers([10,11,12,14,17]))



#Write a Python program to find three numbers from an array such that the sum of three numbers equal to a given number

# returns true if there is triplet with 
# sum equal to 'sum' present in A[]. 
# Also, prints the triplet 
def find3Numbers(A, n):
    arr_size = len(A)
    # Fix the first element as A[i] 
    for i in range( 0, arr_size-2): 

        # Fix the second element as A[j] 
        for j in range(i + 1, arr_size-1): 
            
            # Now look for the third number 
            for k in range(j + 1, arr_size): 
                if A[i] + A[j] + A[k] == n: 
                    print("Triplet is", A[i], 
                        ", ", A[j], ", ", A[k]) 
                    return True
    
    # If we reach here, then no 
    # triplet was found 
    return False

# Driver program to test above function 
A = [1, 4, 45, 6, 10, 8] 
n = 22
 
find3Numbers(A, n) 

# A simple Python 3 program 
# to find three elements whose 
# sum is equal to zero 

# Prints all triplets in 
# arr[] with 0 sum 
def findTriplets(arr, n): 

    found = True
    for i in range(0, n-2): 
    
        for j in range(i+1, n-1): 
        
            for k in range(j+1, n): 
            
                if (arr[i] + arr[j] + arr[k] == 0): 
                    print(arr[i], arr[j], arr[k]) 
                    found = True
    
            
    # If no triplet with 0 sum 
    # found in array 
    if (found == False): 
        print(" not exist ") 

# Driver code 
arr = [0, -1, 2, -3, 1] 
n = len(arr) 
findTriplets(arr, n) 
