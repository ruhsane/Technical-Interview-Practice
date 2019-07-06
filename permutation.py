def perm1(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l=[]
        for i in range(len(lst)):
            current_char = lst[i]
            remaining_char = lst[:i] + lst[i+1:]
            for p in perm1(remaining_char):
                l.append([current_char]+p)
                print(p)
        return l

data = list('war')
print(perm1(data))
# for p in perm1(data):
#     print(p)
 
