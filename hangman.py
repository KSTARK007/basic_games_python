l = ['''



   +---+

   |   |

       |

       |

       |

       |

 =========''', '''

   +---+

   |   |

   O   |

       |

       |

       |

 =========''', '''



   +---+

   |   |

   O   |

   |   |

       |

       |

 =========''', '''



   +---+

   |   |

   O   |

  /|   |

       |

       |

 =========''', '''



   +---+

   |   |

   O   |

  /|\  |

       |

       |

 =========''', '''



   +---+

   |   |

   O   |

  /|\  |

  /    |

       |

 =========''', '''



   +---+

   |   |

   O   |

  /|\  |

  / \  |

       |

 =========''']





def rules():
 print(format("Welcome aboard player"," ^157"))
 print("The rules of the game are quite simple:\n")
 print("You have to guess a word which is related to the topic given to you if u get the word correct you win or else for every wrong alphabet a part  of man appers. If you manage to make more than 7 mistake in guessing the man will be hung and the game end\n\n ")






topic={1:'animals',2:'things',3:'names'}
animals={1:'lion',2:'tiger',3:'cat'}
things={1:'pen',2:'book',3:'phone'}
names={1:'jay',2:'krish',3:"rishi",4:"rachel",5:"chandler"}












def inp():
 from random import randint
 check=int(input("do you still wish to play? if yes the press 1 else 0\n"))
 if(check):
  t=topic[randint(1,3)]
  print("\n ok then here is your topic:   ",t,"\n\nNOTE:The alphabets are suppose to be in lower case\n\n")
  if(t=="animals"):
   q=animals[randint(1,3)]
  elif(t=="things"):
   q=things[randint(1,3)]
  elif(t=="names"):
   q=names[randint(1,5)]
 # print(q)
  i=0
  o=0
  p=0
  m=0
  while(i<len(q)):
   if(m):
    break
   s=1
   print("enter the",i+1,"   alphabet")
   ans=input()
   while(s):
    if(m):
     break
    if(ans!=q[i]):   
     if(o==(len(l)-1)):
      print(l[o],"\n ohhhh nooooo!!!!!")
      m=1
      print("thank you for playing\n You played awsome let us do it again somtime soon ;P")
      break
     print(l[o],format("", "-^143"))
     s=1
     print("try again")
     print("enter the",i+1,"   alphabet")
     ans=input()
     if(m):
      break
     o+=1
    else:
     s=0
     i=i+1
     p=p+1
     if(o==(len(l)-1)):
      print("thank you for playing you played awsome let us do it again")
      break
     
   if(p==len(q)):
    print(format("YOU WIN"," ^157"))
    print(format("WAY TO GO"," ^157"))
    break  
   
   if(m):
    break
 else:
  print("it is not your cup of tea ;P")
 
 
