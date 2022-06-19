def arithmetic_arranger(problems,*calcula):
  
  if len(problems)>5:
    return "Error: Too many problems."
  # arranged_problems=""
  arranged_problems=[]
  for index,value in enumerate(problems):
    # print(index,value)
    elementos=value.split(" ")        
    if elementos[1] not in "-+":
      return "Error: Operator must be '+' or '-'."
    if len(str(elementos[0]))>4 or len(str(elementos[2]))>4:
         return 'Error: Numbers cannot be more than four digits.' 
    try:
        val1=int(elementos[0])
        val2=int(elementos[2])
        
    except ValueError:  
         return "Error: Numbers must only contain digits."      
    dim1=len(str(val1))
        
    dim2=len(str(val2))

    ma=max(dim1,dim2)
    nt=ma+2

    esp1=nt-dim1
    esp2=nt-dim2
    v1=' '*esp1+str(val1)
    v2=elementos[1]+' ' *(esp2-1)+str(val2) 
    lin='-'*nt
    if elementos[1]=='+':
      v3=val1+val2
    else:
      v3=val1-val2
      
    
    
    v3=' '*(nt-len(str(v3)))+str(v3)
    


    linea1=f"{elementos[0]:>{nt}}"
    # linea2=f"{elementos[1]} {elementos[2]:>{nt}}"
    # linea2=f"{f'{elementos[1]} {elementos[2]}':>{nt}}"
    linea2=elementos[1]+f"{elementos[2]:>{nt-1}}"
    linead='-'*nt
    linea3=f"{v3:>{nt}}"
    if calcula:
      try:
         arranged_problems[0]+=' '*4+linea1
      except IndexError:
         arranged_problems.append(linea1)
       # arranged_problems+=' '*4+linea1
      try:
         arranged_problems[1]+=' '*4+linea2
      except IndexError:
         arranged_problems.append(linea2)
        # arranged_problems+=' '*4+linea2
      try:
         arranged_problems[2]+=' '*4+linead
      except IndexError:
         arranged_problems.append(linead)
      try:
         arranged_problems[3]+=' '*4+linea3
      except IndexError:
         arranged_problems.append(linea3)  
    
    else:
        
      try:
         arranged_problems[0]+=' '*4+linea1
      except IndexError:
         arranged_problems.append(linea1)
       # arranged_problems+=' '*4+linea1
      try:
         arranged_problems[1]+=' '*4+linea2
      except IndexError:
         arranged_problems.append(linea2)
        # arranged_problems+=' '*4+linea2
      try:
         arranged_problems[2]+=' '*4+linead
      except IndexError:
         arranged_problems.append(linead)

  if calcula:
     return f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}\n{arranged_problems[3]}"
  else:
      return f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"
# print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49'],True)) 

print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
print('   32         1      45      123      988\n'
        '- 698    - 3801    + 43    +  49    +  40\n'
         '-----    ------    ----    -----    -----\n'
         ' -666     -3800      88      172     1028')