# randomisation and lists.......modules


# python has a many modules us for funny stuff and projects learn so much by doing so much 
# go throgh documentation ......not only python any technology so that u get idea what can be done 
# when it required u will have idea it can be done then u can refer it and work it out

'''go through python documentation and ASK python a resource .....check when u needed 
googling is not wrong ....but make it own after refering'''

# random---by computers by pseudorandomasiation .....mersenne twister ...high math
# khan accadmy---pseudorandom number generators

# import modulename.........our own and inbult like random,,and we use the data in that module
# useful in more like games....
# import day4

import random

a=random.randint(10,100)
print(a)

# lists

l=[1,2,3,"tharun",4.55]
g=[1,2,3]
leng=len(l)
for i in l:
    print(i,"\t")
for i in range(0,leng):
    print(l[i],"\t")
# print(l[leng])
m=[l,g]
print(m[1][0])