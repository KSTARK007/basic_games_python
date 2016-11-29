def funct_b():
 print(format("WELCOME ABOARD CAPTAIN","^157"))
 print("We have a situation.We are hit with heavy fog and we cannot see the enemy ships.Please give orders to shoot them.According to our men,you have sharp sensory skills.So the Admiral has ordered you to take care of this hostile situation.there are three ships which takes up 2(Minesweeper) , 3(Submarine) , 4(Frigate) spaces ")
 print("X stands for successful enemy strikes and O stands for unsuccessful ones.- are the assigned locations for our attacks. You will be given 12 chances")  
 r1=["-","-","-","-","-","-"]
 r2=["-","-","-","-","-","-"]
 r3=["-","-","-","-","-","-"]

 pr1=["O","O","X","X","X","X"]
 pr2=["O","O","O","X","X","O"]
 pr3=["X","X","X","O","O","O"]

 cr1=["O","O","X","X","X","X"]
 cr2=["O","O","O","X","X","O"]
 cr3=["X","X","X","O","O","O"]


 print(" ".join(r1))
 print(" ".join(r2))
 print(" ".join(r3))
 k1=0;k2=0;k3=0;moves=0;r=0
 chck=int(input("If you want to play press 1 or else 0"))
 count=0
 if(chck):
  def battlebegins(k1,k2,k3,moves):
   n=int(input("Which row do you think,captain?"))
   c=int(input("Which column do you think,captain?"))
   print("FIRE!")
   d=c-1
   if n==1:
    if c==3 or c==4 or c==5 or c==6:
     r1[d]="X"
     cr1[d]="F" 
     k1+=1
    else:
     r1[d]="O"
     cr1[d]=""
   elif n==2:
    if c==4 or c==5:
     r2[d]="X"
     cr2[d]="F"
     k2+=1
    else:
     r2[d]="O"
     cr2[d]=""
   elif n==3:
    if c==1 or c==2 or c==3:
     r3[d]="X"
     cr3[d]="F"
     k3+=1
    else:
     r3[d]="O"
     cr3[d]=""
   if "X" not in cr1:
     print("The frigate has been taken down")
   if "X" not in cr2:
     print("The minesweeper has been taken down")
   if "X" not in cr3:
     print("The submarine has been taken down")
   if ("X" not in cr1 and "X" not in cr2 and "X" not in cr3):
     print("The enemy has been defeated! Way to go Cap!")
     exit() 
   print(" ".join(r1))
   print(" ".join(r2))
   print(" ".join(r3))
   moves+=1
   return moves
  while(k1!=4 and k2!=2 and k3!=3):
   if(count==12):
    print("We almost got them Cap . come back soon we need lot of your help") 
    break
   battlebegins(0,0,0,0)
   count+=1
  else:
   print("thank you for playing")
