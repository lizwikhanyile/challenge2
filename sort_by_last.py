

### START FUNCTION
def sort_last(tuples):
    
    # function to get the last element of each tuple
    def last(n): return n[-1]

    #sorting by the last element of each tuple in increasing order 
    return sorted(tuples, key=last) 

### END FUNCTION
print(sort_last([(3, 1, 9), (2, 6), (5, 7, 1)]))

