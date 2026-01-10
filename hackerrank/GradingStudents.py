def gradingStudents(grades):
    rs=[]
    for g in grades:
        if g<38:
            rs.append(g)
        else:
            n5=((g//5)+1)*5
            if n5-g<3:
                rs.append(n5)
            else:
                rs.append(g)

    return rs