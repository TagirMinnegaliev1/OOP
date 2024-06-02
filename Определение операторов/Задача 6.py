class SparseArray:
    def __init__(self):
        self.array = {}

    def __setitem__(self, key, value):
        self.array[key] = value

    def __getitem__(self, key):
        return self.array.get(key, 0)
    
def print_elem(array, ind):
    print('arr[{}] = {}'.format(ind, array[ind]))


arr = SparseArray()
index = 1000000000
arr[index] = 123

print_elem(arr, index - 1)
print_elem(arr, index)
print_elem(arr, index + 1)
