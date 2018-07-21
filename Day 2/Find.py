import time
start = time.time()
def find_num(list, num):
    start = time.time()
    for index in range(len(list)):
        print (list)
        if num == list[index]:
            return index
    return -1
    end = time.time()
    x = end - start
    print(str(x))
print(find_num(range(0, 9999999999999999), 9999999999999998))
