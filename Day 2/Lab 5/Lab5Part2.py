def process(name):
    # name is a file, returns a list of strings
    #    from the file
    f = open(name)
    answer = []
    for line in f:
        line = line.strip()
        line = line.split(":")
        answer.append(line)
        #answer.append(line.strip())
    return answer

def averageHeight(name):
    answer1 = 0
    answer2 = 0
    count = 0
    while count < 39:
        answer = data[count][4]
        answer1 = int(answer) + answer1
        count += 1
        answer2 = answer1 / 39
    print(answer2)

def heightRange(name, height1, height2):
    count = 0
    while count < 39:
        if int(data[count][4]) <= int(height2) and int(data[count][4]) >= int(height1):
            print(data[count][4])
        count+=1

def group(filename, gender, sport):
    count = 0
    while count < 39:
        if gender == data[count][2] and sport == data[count][3]:
            print(data[count][0] + " " + data[count][1])
        count+=1

if __name__ == '__main__':
    filename = "C:\\Users\\train916.ADRICE\\Desktop\\Week 2\\Day 2\\Lab 5\\athletes.txt"
    data = process(filename)
    print ("THE DATA IS:")
    for item in data:
        print (item)

print("average height of everybody")
averageHeight(filename)

print("range of heights")
heightRange(filename, 72, 78)

print("different range of heights")
heightRange(filename, 74, 74)

print("women in basketball")
group(filename, "women", "basketball")

print("women in tennis")
group(filename, "women", "tennis")
#1.it follows the address of the file
#2.a string
#3.it turns the .txt file into a list of strings
#4. look up
#5. 71.4 inches
#6. def heightRange(name, height1, height2):
#    count = 0
#    while count < 39:
#        if int(data[count][4]) <= int(height2) and int(data[count][4]) >= int(height1):
#            print(data[count][4])
#        count+=1
#7. heightRange(filename, 72, 78)
#8. def heightRange(name, height1, height2):
    #count = 0
    #while count < 39:
    #    if int(data[count][4]) <= int(height2) and int(data[count][4]) >= int(height1):
    #        print(data[count][4])
    #    count+=1
#9. heightRange(filename, 74, 74), 2
#10. def group(filename, gender, sport):
    #count = 0
    #while count < 39:
        #if gender == data[count][2] and sport == data[count][3]:
            #print(data[count][0] + " " + data[count][1])
        #count+=1
#11. group,4
#12.
