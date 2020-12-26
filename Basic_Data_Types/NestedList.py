if __name__ == '__main__':
    student,marks=[],[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        #saving all the score details into a list (marks)
        marks.append(score)
        #saving all the name, score details into a list (student)
        student.append([name,score])
    
    #sorting the data and saving into the same variable
    student=sorted(student,key= lambda student: student[1])
    marks= sorted(marks)
    
    #storing the second lowest score into a variable second
    if(marks.count(min(marks))==len(marks)):
        second=min(marks)
    else:
        score_temp= [i for i in marks if min(marks)!=i]
        second=min(score_temp)
    
    #printing the names of the students with the second lowest value 
    for i in sorted(student, key= lambda student: student[0]):
        if (i[1] == second):
            print(i[0])
    
