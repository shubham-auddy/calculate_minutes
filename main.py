# Calculate the number of minutes passed between two given times in the format as shown bellow :
# 2:00am-1:00am = 960

def calculate_minutes(str):

    inputs = str.split('-')

    inputs[0] = inputs[0][:-2]
    inputs[1] = inputs[1][:-2]

    i1 = inputs[0].split(':')
    i2 = inputs[1].split(':')

    i1 = [int(x) for x in i1]
    i2 = [int(x) for x in i2]

    if i1[0] == 12:
        i1[0] = 0

    if str.count('am') <= 1 and str.count('pm') <= 1:
        i2[0] = i2[0]+12
    else:
        if i2[0] < i1[0]:
            i2[0] = i2[0]+24

    var1 = i1[0]*60 + i1[1]
    var2 = i2[0]*60 + i2[1]
    return var2 - var1


time_input = input("Enter the durations in 12hr format : ")
result = calculate_minutes(time_input)
print(result)
