lego_list = []
count = 0
leg_num = input("How many Legos? ")
leg_num_int = int(leg_num)
while count < leg_num_int:
    if count % 3 == 0:
        lego_list.append("black")
    if count % 3 == 1:
        lego_list.append("green")
    if count % 3 == 2:
        lego_list.append("black")
    count += 1
print(lego_list)
