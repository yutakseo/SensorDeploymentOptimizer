
test_data = [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1]

orginal_data = test_data
converted_data = []
for i in range(len(orginal_data)):
    if (orginal_data[i-1] == 0) & (orginal_data[i] == 1):
        converted_data.append(1)
    elif (orginal_data[i-1] == 1) & (orginal_data[i] == 0):
        converted_data[-1] = 1
        converted_data.append(0)
    elif (orginal_data[i-1] == 1) & (orginal_data[i] == 1):
        converted_data.append(0)
    else:
        converted_data.append(0)

for i in range(len(orginal_data)):
    if orginal_data[i] == 1:
        converted_data.append(1)
    elif (orginal_data[i-1] == 1) & (orginal_data[i] == 0):
        converted_data.append(0)
    elif (orginal_data[i-1] == 1) & (orginal_data[i] == 1):
        converted_data.append(0)
    

print(converted_data)    