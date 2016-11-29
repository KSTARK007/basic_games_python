def funct_m():
 print("The rules of the game are quite simple:\n")
 print("You are suppose to enter the values in distint single digit in such a way that the sum of all the horizontal,virtical and diagonal elements should be same ok \n All the best")
 print("\nstill want to continue then press 1 if not press 0")
 ch=int(input())
 if(ch):

  l1=[]
  l2=[]
  l3=[]

  item=0
  for i in range(3):
      print("enter the element ",i+1," of the first line of the magic square")
      item=int(input("--->>"))
      l1.append(item)
  print()	
  print("therefore the first line of the magic square is" ,l1)
  print("-----------------------------------------------------")
  print()

  item=0
  for i in range(3):
      print("enter the element ",i+1," of the second line of the magic square")
      item=int(input("--->>"))
      l2.append(item)
  print()
  print("therefore the second line of the magic square is" ,l2)
  print("-----------------------------------------------------")
  print()
 
  item=0
  for i in range(3):
      print("enter the element ",i+1," of the third line of the magic square")
      item=int(input("--->>"))
      l3.append(item)
  print()
  print("therefore the third line of the magic square is" ,l3)
  print("-----------------------------------------------------")
  print() 

  def func(x):
      return(l1[x] + l2[x] + l3[x])
	
  sum1=func(0)
  sum2=func(1)
  sum3=func(2)

  sumd1=(l1[0] + l2[1] + l3[2])
  sumd2=(l1[2] + l2[1] + l3[0])


  print()
  print("-----------------------------------------------------")
  print("THE MAGIC SQUARE THAT YOU HAVE ENTERED IS ")
  print(l1)
  print(l2)
  print(l3)

  print()
  if (sum1==sum2==sum3==sumd1==sumd2):
      print("CONGRADULATIONS !!!! YOU HAVE CREATED A MAGIC SQUARE")
  else:
      print("SORRY THIS IS NOT A MAGIC SQUARE")
	




#CORRECT ANSWER
#8 3 4

#1 5 9

#6 7 2




	
