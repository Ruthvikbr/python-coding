a = [1,2,3,4]

for i in a:
    print(i)

for i in range(4):
    print(i)  #0,1,2,3

for i in range(4,6):
    print(i) #4,5

for i in range(1,11,2): #start,#end,#step
    print(i) # 0,1,3,5,9


cast = {
    "Jerry Seinfeld": "Jerry Seinfeld",
    "Julia Louis-Dreyfus": "Elaine Benes",
    "Jason Alexander": "George Costanza",
    "Michael Richards": "Cosmo Kramer"
}

# iterating through dictionaries

for key in cast:
    print(key)

for key,value in cast.items():
    print(key+" : "+value)