import numpy as np

def calculate(lst):
    # Raise error in case the list is not 9 elements in len
    if len(lst) != 9:
        raise ValueError('List must contain nine numbers.')

    # Creating the 3x3 matrix based on the list
    npArr = np.array(lst).reshape(3, 3)

    # Initializing a calculations dict
    calculations = {}

    # List of operations to perform with correct test names (could be using an array/tuple and being more efficient)
    operations = {
        'mean': 'mean',
        'variance': 'var',
        'standard deviation': 'std',
        'max': 'max',
        'min': 'min',
        'sum': 'sum'
    }

    # Loop through the operations and calculate 'calculations' for axis 0, axis 1, and the entire array
    for key, op in operations.items():
        calculations[key] = [getattr(npArr, op)(axis=0).tolist(),
                             getattr(npArr, op)(axis=1).tolist(),
                             getattr(npArr, op)()]

    return calculations