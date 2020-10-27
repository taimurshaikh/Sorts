class Sorts:
    def bubbleSort(self, vals):
        length = len(vals)
        for i in range(length):
            for j in range(length):
                if j == 0:
                    continue
                if vals[j-1] > vals[j]:
                    vals[j-1], vals[j] = vals[j], vals[j-1]
        return vals

    def mergeSort(self, vals):
        pass
    def insertionSort(self, vals):
        pass
    def quickSort(self, vals):
        pass
