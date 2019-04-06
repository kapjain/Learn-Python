import logging

#DEBUG: Detailed information, typically of interest only when diagnosing problems
#INFO: Confirmation that things are working as expected
#WARNING: An indication that something unexpected happened, or indicative of some problem in the near future(e.g. 'disk space low'). The software still working as expected
#ERROR: Due to a more serious problem, the software has not been able to perform some function
#CRITICAL: A serious error, indicating that the program itself may be unable to continue running

#default label is WARNING


logging.basicConfig(filename= 'test.log' ,level = logging.DEBUG, format = '%(asctime)s :%(levelname)s: %(name)s:%(message)s')

def add(x,y):
    """add function"""
    return x + y

def subtract(x,y):
    """subtract function"""
    return x + y

def multiply(x,y):
    """multiply function"""
    return x + y

def divide(x,y):
    """divide function"""
    return x + y

num_1 = 10
num_2 = 5

add_result = add(num_1,num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

subtract_result = subtract(num_1,num_2)
logging.debug('subtract: {} + {} = {}'.format(num_1, num_2, subtract_result))

multiply_result = multiply(num_1,num_2)
logging.debug('multiply: {} + {} = {}'.format(num_1, num_2, multiply_result))

divide_result = divide(num_1,num_2)
logging.debug('divide: {} + {} = {}'.format(num_1, num_2, divide_result))
print('divide: {} + {} = {}'.format(num_1, num_2, divide_result))
#logging.debug('divide: {} + {} = {}'.format(num_1, num_2, divide_result))
#logging.warning('divide: {} + {} = {}'.format(num_1, num_2, divide_result))
#logging.info('divide: {} + {} = {}'.format(num_1, num_2, divide_result))
#logging.critical('divide: {} + {} = {}'.format(num_1, num_2, divide_result))
#logging.error('divide: {} + {} = {}'.format(num_1, num_2, divide_result))


