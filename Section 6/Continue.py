# with continue
for x in range(20):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)

# without continue
for x in range(20):
    if x % 3 != 0 and x % 5 != 0:
        print(x)
