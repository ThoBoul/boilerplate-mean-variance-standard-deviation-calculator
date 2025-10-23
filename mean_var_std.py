import numpy as np

def calculate(list):
    
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    list2d = [list[0:3], list[3:6], list[6:9]]
    numpy_array = np.array(list2d)

    calculations = {
        'mean': [[float(numpy_array[:, i].mean()) for i in range(0,3)], 
                 [float(numpy_array[i].mean()) for i in range(0,3)], 
                 float(numpy_array.mean())],
        'variance': [[float(numpy_array[:, i].var()) for i in range(0,3)], 
                     [float(numpy_array[i].var()) for i in range(0,3)], 
                     float(numpy_array.var())],
        'standard deviation': [[float(numpy_array[:, i].std()) for i in range(0,3)], 
                               [float(numpy_array[i].std()) for i in range(0,3)], 
                               float(numpy_array.std())],
        'max': [[float(numpy_array[:, i].max()) for i in range(0,3)], 
                [float(numpy_array[i].max()) for i in range(0,3)], 
                float(numpy_array.max())],
        'min': [[float(numpy_array[:, i].min()) for i in range(0,3)], 
                [float(numpy_array[i].min()) for i in range(0,3)], 
                float(numpy_array.min())],
        'sum': [[float(numpy_array[:, i].sum()) for i in range(0,3)], 
                [float(numpy_array[i].sum()) for i in range(0,3)], 
                float(numpy_array.sum())]
    }

    return calculations