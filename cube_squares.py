### START FUNCTION
def sq_cube(numbers):
    # empty list to store the resulting list of lists
    evenNum = [] 
    for n in numbers:

        # rounding to the nearest integer
        num = round(n) 

        # check if number is even
        if num % 2 == 0: 

            # square and cube of a number
            num_sq = num**2 
            num_cb = num**3 

            # append eveNum list with a list containing square and cube
            evenNum.append([num_sq, num_cb]) 
    return evenNum
    
### END FUNCTION
print(sq_cube([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]))
### END FUNCTION