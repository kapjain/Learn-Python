import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s :%(levelname)s: %(name)s:%(message)s')
file_handler = logging.FileHandler('test_log.log')

logger.addHandler(file_handler)
file_handler.setFormatter(formatter)


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
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

subtract_result = subtract(num_1,num_2)
logger.debug('subtract: {} + {} = {}'.format(num_1, num_2, subtract_result))

multiply_result = multiply(num_1,num_2)
logger.debug('multiply: {} + {} = {}'.format(num_1, num_2, multiply_result))

divide_result = divide(num_1,num_2)
logger.debug('divide: {} + {} = {}'.format(num_1, num_2, divide_result))