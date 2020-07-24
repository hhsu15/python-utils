lst = [1, 2, 3, 5]
nl = []
for e in lst:
    if e % 2 == 0:
       nl.append(e)
       breakpoint()       
print(nl)
print("done")
