# fibonacci sequence in python 

count = 0
values = [0, 1]
while count != 25: 
    seq = values[0] + values[1]
    print(seq)
    values.append(seq) 
    values.pop(0)
    count += 1
