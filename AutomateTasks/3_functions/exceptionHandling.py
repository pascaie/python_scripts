# exception handling with "try" and "except"

# dividing by zero (0) returns the ZeroDivisionError
def division(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print('Error: the denominator cannot be zero')  # this message is displayed and the script can continue

num = 100
for den in (5, 10, 20, 0, 50):
    print(division(num, den))
# OBS: when the division by 0 is performed, the exception is thrown
# after this, , the loop continues with its last cycle by dividing num by 50
