low = 402328
hi = 864247

password = low
count = 0

#Password is stricly non-increasing
def strictDecrease(pw):
    while pw > 10:
        if pw % 10 >= pw/10 % 10:
            pw = pw/10
        else:
            return False
    return True

#Password has two contiguous similar digits
def hasDouble(pw):
    while pw > 10:
        if pw % 10 == pw/10 % 10:
            return True
        else:
            pw = pw/10
    return False

#Brute force solution
while(password < hi):
    password += 1
    if strictDecrease(password):
        if hasDouble(password):
            count += 1

print(count)

