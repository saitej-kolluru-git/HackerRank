s="EQQAEAOQYEQEYYOEEQQYAOEEAQEEOOEYAYOEYAYAEOQYAAYAOYYOQAAYEQAOOAQEAEYAOEEQYYEEAOAOAEQOEYOAOEYOOAAOQEOYEAYYOEAOAQEYYEOQEEEYAOOAYOOAQAEOYOYAEOYQEEEOOQOEAOAAQAOQEYOQEAEAEOOOOQOYQOEQQYEEEYEEOQYYYOEQOQEYAYQQOYEEOAEQOEEEEAAEEYAAQAAQAAYOEAQAQYEYYYEAOYOQEQOOEQOYAYAEEYQAYYQYYAEAYOEYEAOQQQOYYYOYYOYYQYAOEOAOAOYEAAOEOEAEYQAEAQOEOYEEAQOAOQEYOEQOAQQEEYOOAQQOOEYQAQOEEOOOAAQOQEYYOEOOQOOAEYEOOAEQYQOAEYYYAQAYOEYOEYYEEOEEOAYAEEQEQOAAAYAEYQQAYOYQQOAEAOQOOYAEEOAEQAQEEQYOOEEAEEAAOYQYQAOEQYOYEQEAAOYAQAQYEAQEQEEOQQQYEYOQ"
vs,cs='',''
members=[]
score={0:0,1:0}
vowels=['A','E','I','O','U']
for i in s:
    if (i in vowels and i not in vs):
        vs+=i
    else:
        if (i not in vs and i not in cs):
            cs+=i
members.append([cs,vs])
#print(members)


for l in range(len(members[0])):
    score_value=0
    for i in members[0][l]:
        for j in range(s.index(i),len(s)):
            #print(s[s.index(i):j+1])
            temp=s[s.index(i):j+1]
            if(len(temp)<=1):
            #print("count of {} = {}".format(temp,s.count(temp)))
                score_value+=s.count(temp)
            else:
                #count1=0
                for k in range(len(s)):
                #print(temp,s[k:k+len(temp)])
                    if(s[k:k+len(temp)]==temp):
                        score_value+=1
                #print("count of {} = {}".format(temp,count1))
                #score_value+=count1
    #print(kevin)
    score[l]=score_value

if(score[0]>score[1]):
    print("STUART ",score[0])
else:
    print("KEVIN ",score[1])
                    
                    
                                        
        
        
