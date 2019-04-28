""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?

def check_same(arr):
    firs = arr[1]
    for i in arr:
        if i != firs:
            return False
    return True

def featureScaling(arr):
    if check_same(arr) == 1:
        return [0.5 for i in range(len(arr))]
    largest = max(arr)
    smallest = min(arr)
    new_array = []

    for each in arr:
        new = (each - smallest) / (largest - smallest)
        new_array.append(new)
    return new_array

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print(featureScaling(data))

