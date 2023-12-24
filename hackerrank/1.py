n = int(input().strip())
if n%2!=0:
    print("Weird")
elif n in range(2,6) or n not in range(6,21):
    print("Not Weird")
else:
    print("Weird")     