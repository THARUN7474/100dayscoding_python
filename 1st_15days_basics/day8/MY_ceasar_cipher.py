a="tharun"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
shift=4
b=""
for j in range(len(a)):
    index=letters.index(a[j])
    print(index)
    if index<=25-shift:
        newindex=index+shift
        # print(newindex)
        # print(letters[newindex])
        b=b+letters[newindex]
    else:
        newindex=shift-(25-index)
        # print(newindex)
        # print(letters[newindex])
        b=b+letters[newindex]
print(b)
c=""
for i in range(len(b)):
    index=letters.index(b[i])
    print(index)
    if index>=shift:
        newindex=index-shift
        # print(newindex)
        # print(letters[newindex])
        c=c+letters[newindex]
    else:
        newindex=(26-shift)+index
        # print(newindex)
        # print(letters[newindex])
        c=c+letters[newindex]
print(c)
# g=letters
# for i in range(shift):
#     b=g.pop(0)
#     g.append(b)
# print(letters)
# print(g)
# print(letters.index(a[0]))
# b=""
# for j in range(len(a)):
#     index=letters.index(a[j])
#     print(index)
#     b=b+g[index]
# print(b)


