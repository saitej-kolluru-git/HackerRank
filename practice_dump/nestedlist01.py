k=[]
ps = [['Harsha', 37.21], ['Beria', 37.21], ['Varun', 37.2], ['Kakunami', 41], ['Vikas', 39]]
marks=[37.21,37.21,37.2,41,39]
ps=sorted(ps,key = lambda ps: ps[1], reverse=False)
print(ps)
marks= sorted(marks, reverse=False)
print(marks)
if(marks.count(min(marks)) == len(marks)):
    print('0')
else:
    second= [i for i  in marks if min(marks)!= i ]
    print(min(second))
    
