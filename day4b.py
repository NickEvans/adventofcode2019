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

#Only doubles
def noOddStreaks(pw):
    pw = str(pw)
    pw = [digit for digit in str(pw)]
    count = 0

    for d in range(len(pw) - 1):
        if pw[d] == pw[d+1]:
            count += 1
        else:
            if count == 1:
                return True
            count = 0
    if count == 1:
        return True
    return False

#Brute force solution
while(password < hi):
    password += 1
    if strictDecrease(password):
        if noOddStreaks(password):
            count += 1

print(count)

