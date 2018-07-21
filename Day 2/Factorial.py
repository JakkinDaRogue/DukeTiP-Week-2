import time
def factorial(num):
    answer = 1
    start = time.time()
    count = 1
    while count <= num:
        answer = answer * count
        count += 1
    end = time.time()
    x = end - start
    v = (x / 1000) / 60
    print (str(v))
factorial(999999)
