def mainf():
 from random import randint
 def func(x):
    return(l[0][x] + l[1][x] + l[2][x])
 
 a,b,c,d=[0,0,0,0]
 a={1:[[4,9,2],[3,5,7],[8,1,6]],2:[[8,1,6],[3,5,7],[4,9,2]],3:[[6,1,8],[7,5,3],[2,9,4]]}
 q={1:[["a",9,"b"],[3,"c",7],[8,1,"d"]],2:[[8,1,"a"],["b",5,"c"],["d",9,2]],3:[["a",1,8],[7,"b",3],["c",9,"d"]]}
 
 qq=[[4,2,1,6],[6,3,7,4],[6,5,2,4]]
 
 print("The rules of the game are quite simple:\n")
 print("You are suppose to enter the values in single digit in such a way that the sum of all the horizontal,virtical and diagonal elements should be same k \n All the best")
 print("\nstill want to continue then press 1 if not press 0")
 check=input()
 print("Ok so welcome to the game\n")
 print("here is ur question \n")
 k=randint(1,3)
 s=1
 while(s==1):
  print(q[k])
  #print(a[k])
  print("\n")
  a=int(input("\nenter a: "))
  b=int(input("\nenter b: "))
  c=int(input("\nenter c: "))
  d=int(input("\nenter d: "))
  m=list()
  ch=0
  if(k==1):
   if(qq[0][0]==a and  qq[0][1]==b and  qq[0][2]==c and qq[0][3]==d):
    ch=1
  if(k==2):
   if(qq[1][0]==a and  qq[1][1]==b and  qq[1][2]==c and qq[1][3]==d):
    ch=1
  if(k==3):
   if(qq[2][0]==a and  qq[2][1]==b and  qq[2][2]==c and qq[2][3]==d):
    ch=1
  if(ch):
   print("CONGRATULATIONS !!!! YOU HAVE GOT A MAGIC SQUARE CORRECT")
   s=0 
  else:
   print("SORRY WRONG ANS TRY AGAIN ") 
   s=0

