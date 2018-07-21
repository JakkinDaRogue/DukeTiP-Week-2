import time
tic = time.time()
a = [47923184587125690283465, 39847291465715, 18274910759723, 825678549125672, 987298648918456194152634, 25364271537482764]

x = 1
for x in range(1, len(a)):
    key = a[x]
    i = x - 1
    while i >= 0 and a[i] > key:
        a[i + 1] = a[i]
        i -= 1
    a[i + 1] = key
    #x = x + 1
print(a)

toc = time.time()
print(str(toc-tic) + "sec elapsed")
