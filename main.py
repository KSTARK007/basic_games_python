from battleship import *
from slotmachine import *
from hangman import *
from magic import *
fp=open("rules.txt","r")
fp.seek(0,0)
def cls():
 print("\n"*100)
dic={1:'Battleship', 2: 'Slot machine', 3: 'Hang a man', 4:'Magic square'}
print("\n\n\n\n")
print(format("WELCOME GUYS THIS IS THE GAME CENTER\n","^157"))
for i in fp:
 print(i)
c=int(input("\n\nwhich game do u want to play?(press 1 for battleship ...)\n\n"))
cls()
if(c>4 or c<=0):
 print("\n\nSorry guys,we have only 4 games so choose form them only\n\n")
else:
 print("so let us start with     " , dic[c],"\n\n\n\n\n\n\n\n")
 if(c==1):
  funct_b()
 elif(c==2):
  disp()
  play()
 elif(c==3):
  rules()
  inp()
 elif(c==4):
  mainf()

print(format("\n\n\n\n\nTHANK YOU \n\n PLEASE VIST US AGAIN"," ^157"))
print("\n\nby-\nKiran\nKrishna\nJay\nHrishi")
f=input("\n\nfeedback please\n\n")
fpp=open("feedbacks.txt","a")
fpp.write(f)
fpp.write("\n\n")
print(":)")
