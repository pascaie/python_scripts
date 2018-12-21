# debugging

# if an exception is raised in a single line like the following one, it simply makes the script to crash
# raise Exception('This is an error message')

def largeRectangle(): #  function to calculate the area of a rectangle
    # this rectangle should be large
    # exception is thrown if the width and/or the height do not overcome a certain length
    width = int(input('Please, insert the rectangle width: '))  # input the width
    height = int(input('Please, insert the rectangle height: '))  # input the heigth

    if width <= 10 or height <= 10:  # if the dimensions are too small, then raise an exception
        # raise an exception with the respective error message
        raise Exception('The width/heigth that you inputed are too small. Please insert values above 10.')

    area = width * height  # calculate the area by multiplying width and heigth
    return area  # return the area

try:  # try - except statement to catch the exception (if necessary)
    print(largeRectangle())  # print the function output, if the length constraint are respected
# raise the exception if the length constraints are not respected; assign the string message of the exception to the exception object "lenerr"
except Exception as lenErr:
    print('An exception happened: ' + str(lenErr))  # print the error message
