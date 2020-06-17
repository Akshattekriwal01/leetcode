def minheap:
    def heapify(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            sink(arr, i)

    def swim(arr, root):
        """
        step1: move the path of smaller child up one position from root
        step2: place root item at leaf of the path
        step3: move the path down one position until parent is smaller (sink)
        """
        item = arr[root]
        i = root
        j = 2 * i + 1
        while j < len(arr):
            if j + 1 < n and arr[j] > arr[j + 1]:
                j += 1
            arr[i] = arr[j]
            i = j
        arr[j] = item
        sink(arr, root, j)
        
    def sink(arr, root, i):
        item = arr[i]
        while i > root:
            j = (i - 1) // 2
            if arr[j] < arr[i]:
                arr[i] = arr[j]
                i = j
            else:
                break
        arr[i] = item

    def pop(arr):
        last = arr.pop()
        if len(arr) > 0:
            top = arr[0]
            arr[0] = last
            swim(arr, 0)
            return top
        else:
            return last

    def push(arr, item):
        arr.append(item)
        sink(arr, 0, len(arr) - 1)