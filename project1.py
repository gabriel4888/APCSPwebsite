import time

class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    BROWN   = '\033[38;2;150;75;0m]'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class bg:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    BROWN   = '\033[38;2;150;75;0m]'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

class style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET_ALL = '\033[0m'

#this is a function with paramaters
def color(tColor,bColor,text):
  #retun means give back something at the line where you call the funtion
  return tColor+bColor+text+fg.RESET+bg.RESET;
#print("Do you want, "+ color(fg.YELLOW, bg.MAGENTA, "door 1")+"or"+color(fg.CYAN, bg.MAGENTA, "door 2")+"?")

#def lines(numChars, numLines, char):
#  for i in range()
  

def colorTester():
  choice=input("Do you want "+color(fg.RED,bg.BLACK,"coke")+" or"+color(fg.GREEN,bg.YELLOW,"Mt Dew")+"?")
  if choice=="coke":
    print("Enjoy your coke")
  elif choice=="Mt Dew":
    print("Enjoy your Mt.Dew")
#colorTester()

print("Hello, Welcome to my adventure")

def askForName():
  global name
  name=input("What is your name?")

def setting():
  print(name+" its 5am on a Saturday moring")
  time.sleep(2)
  print("Your on the California Delta lauching your kayak")
  time.sleep(2)
  print("Your the only one as the lauch this moring")
  time.sleep(2)
  print("You get an errie fealing")
  time.sleep(2)
  print("Your not sure why")
  time.sleep(2)
  print("But you still launch")
  
def yes():
  time.sleep(2)
  print("Do you fish the tullies near the ramp")
  time.sleep(2)
  print("Or go to a spot that your freind did good at last week.")
  time.sleep(2)
  print("Fish here or leave")
  I=input()
  if I.lower()=="here":
    here()
  elif I.lower()=="leave":
    leave()
  else:
    print("Not an option")
    print("")
  
def dotted():
    print("")
    print("")
  
def here():
  time.sleep(2)
  print("Ok, you start fishing")
def leave():
  time.sleep(2)
  print("Ok, you spent 45 minutes paddling to the spot.")
  time.sleep(2)
  print("Your arms are sore but you made it.")
  
def lureChoice():
  time.sleep(2)
  print("Its a rising tide and some mild moring winds from the west")
  time.sleep(2)
  print("What do you want to throw?")
  time.sleep(2)
  global LC
  LC=input("You have a "+color(fg.WHITE,bg.CYAN,"Spinnerbait")+", "+ color(fg.WHITE,bg.GREEN,"Bladedjig")+", or a "+color(fg.CYAN,bg.YELLOW,"Topwater"))
  if LC.lower()=="spinnerbait":
    time.sleep(1)
    print(color(fg.RESET,bg.GREEN,"Good Choice"))
  elif LC.lower()=="bladedjig":
    time.sleep(1)
    print(color(fg.RESET,bg.GREEN,"Good Choice"))
  elif LC.lower()=="topwater":
    global TC
    time.sleep(1)
    TC=input("Buzzbait, Spook, or plopper")
    TC=LC
  else:
    time.sleep(1)
    print("Not an option")
    lureChoice()
    
def sFa():
  time.sleep(1)
  print("Ok, you start casting your "+LC+" along the tulies")
  time.sleep(1.5)

def sF(x):
  time.sleep(2)
  print(color(fg.RED,bg.RESET,"THUMP"))
  time.sleep(2)
  print("You slam the hook set and "+color(fg.RED,bg.RESET,"Fish ON!"))
  time.sleep(2)
  print("You get it to the boat its a nice "+str(x)+" lber")
  
def sFa2():
  print("You keep throwing your "+LC+" along the tulies")
  
def EM():
  print("The moring bite seems to be coming to an end")
  time.sleep(2)
  print("The sun is high in the sky and its getting hot")
  time.sleep(2)
  print("The wind has stoped and the water is glass")
  time.sleep(2)
  
def lureChoice2():
  print("Its time to take off the reaction bait and slow down")
  print("What do you want to throw?")
  global LC2
  LC2="a"
  LC2=input("You have a "+color(fg.GREEN,bg.RESET,"Wacky-Rig")+", "+ color(fg.BLUE,bg.BLACK,"Jig")+", or a "+color(fg.BLUE,bg.GREEN,"Punch-Rig"))
  if LC2.lower()=="wacky-rig":
    print(color(fg.RESET,bg.GREEN,"Good Choice"))
  elif LC2.lower()=="jig":
    print(color(fg.RESET,bg.GREEN,"Good Choice"))
  elif LC2.lower()=="punch-rig":
    print(color(fg.RESET,bg.GREEN,"Good Choice"))
  else:
    print("Not an option")
    lureChoice2()
def sFa2():
  print("Ok, you start flipping your "+LC2+" along the tulies")
  time.sleep(1.5)

def sF2(x):
  print(color(fg.RED,bg.RESET,"THUMP"))
  time.sleep(1.5)
  print("You slam the hook set and "+color(fg.RED,bg.RESET,"Fish ON!"))
  time.sleep(1.5)
  print("You get it to the boat its a nice "+str(x)+" lber")
  
def bgs():
  time.sleep(2)
  print("Thats a big one, bigest one so far")
  
def tp():
  time.sleep(2)
  print("One hour goes by ...")
  time.sleep(2)
  print("Another hour goes by, nothing ...")
  time.sleep(3)
  print("...")
  time.sleep(2)
  global M
  print("Its been 3 hours since your last bite, and the tide has droped, and the sun is high in the sky.")
  time.sleep(2)
  M=input("Should you A, swtich spots or or B, start cover water")
  if M.lower()=="a":
    print(color(fg.BLUE,bg.BLACK,"You move to some shaded docks"))
  elif M.lower()=="b":
    print(color(fg.BLUE,bg.RESET,"You tie on a bladed jig and start covering water"))
  #CALLING FUNCTIONS
  
def docks():
  time.sleep(3)
  print("You start skiping a "+LC2+" under the shaded docks")
def cover():
  time.sleep(3)
  print("You start casting a bladed jig everywhere while drifting with the current")
  time.sleep(2)
  print("You cast it along tullies, grass, rocks, and docks")
  
def tdEnd():
  time.sleep(3)
  print("Its been a long day, its probly time to get heading out")
  time.sleep(2)
  print("You start paddleing back")
  time.sleep(1)
  print("...")
  time.sleep(1)
  print("...")
  time.sleep(1)
  print("...")
  time.sleep(2)
  print("You made it back to the launch")
  time.sleep(1)
  print("You put your kayak back on the trailer and head home")
  
def dback():
  time.sleep(2)
  print("While driving back you recap over the day while on a call with your freind")
  time.sleep(3)
  print("It was a good day, not a ton of numbers, but good quality fish")
  time.sleep(3)
  print("You stop to get In-N-Out on the way home")
  
def InNOut():
  time.sleep(3)
  print("You go to order, what do you want")
  time.sleep(2)
def burger():
  global ichoice1
  print(color(fg.RED,bg.YELLOW,"Single")+" or "+color(fg.RED,bg.YELLOW,"Double-double ")+"?")
  ichoice1=input()
  if ichoice1.lower()=="single":
    print(color(fg.WHITE, bg.GREEN,"Good Choice"))
  elif ichoice1.lower()=="double-double":
    print(color(fg.WHITE, bg.GREEN,"Good Choice"))
  else:
    print("Please pick something on the menu")
    burger()
def side():
  time.sleep(2)
  global ichoice2
  global n
  ichoice2=input("Now for sides, "+color(fg.YELLOW, bg.RESET,"Fries")+", "+color(fg.YELLOW, bg.WHITE,"Milkshake"))
  if ichoice2.lower()=="fries":
    time.sleep(2)
    global ichoice3
    ichoice3=input(color(fg.YELLOW, bg.RED,"Animal style?"))
    if ichoice3.lower()=="yes":
      print("Ok, one "+ichoice1+", one "+ichoice2+" Animal style, Coming up!")
      print("Your number is 63")
      n=63
    elif ichoice3.lower()=="no":
      print("Ok, one "+ichoice1+", one "+ichoice2+", Coming up!")
  if ichoice2.lower()=="milkshake":
    ichoice3=input(color(fg.YELLOW, bg.WHITE,"Vanila ")+", "+color(fg.BROWN,bg.WHITE,"Chocolate")+", or"+color(fg.RED,bg.WHITE,"Strawberry"))
    if ichoice3.lower()=="vanila":
      pass
    elif ichoice3.lower()=="chocolate":
      pass
    elif ichoice3.lower()=="strawberry":
      pass
    else:
      print("Not an option")
      
    print("Ok, one "+ichoice1+", one "+ichoice3+" "+ichoice2)
    print("Your number is 64")
    n=64
  elif ichoice3.lower()=="no":
    time.sleep(2)
    print("Ok, one "+ichoice1+", one "+ichoice2)
    print("Your number is 62")
    n=62
def CN():
  global n
  time.sleep(2)
  print("You go sit down")
  time.sleep(2)
  print("...")
  time.sleep(2)
  print("The anaouncer yells 62")
  if n==62:
    print("You go up, order for"+name+"right?")
    print("Yep, you claim your "+ichoice1+", and one "+ichoice2)
    n=0
  else:
    print("...")
  if n==63 or n==64:
    print("The anaouncer yells 63")
    if n==63:
      print("You go up, order for"+name+"right?")
      print("Yep, claim your "+ichoice1+", one "+ichoice2+" Animal style")
    else:
      print("...")
  if n==64:
    print("The anaouncer yells 64")
    if n==64:
      print("You go up, order for"+name+"right?")
      print("Yep, you claim your "+ichoice1+", one "+ichoice3+" "+ichoice2)

def CNC():
  time.sleep(2)
  print("You finish eating, it was pretty good")
  time.sleep(2)
  print("You get up, get in your car and drive home")
  time.sleep(2)
  print("Its been a long day, your so tired you just lay down on your bed and fall asleap")
  time.sleep(1)
  print("You sleep with all of your fishing cloths on, but you sleep great.")
  time.sleep(1)
  print("THE END")

  
    
#I have _ functions and _ functions with parameters
#My special feture is The in-and-out number calling thing
#timeing? YES
#spaceing YES
#color on choices YES     colorFunction from schoolage YES
#invalad choices YES
#lowercase/uppercase respnces same YES
#name repeted
#code is mine YES
    
    #Calling Functions
askForName()
dotted()
setting()
dotted()
yes()
lureChoice()
sFa()
sF(2)
dotted()
sFa()
sF(1)
dotted
sFa()
dotted
sF(3)
EM()
dotted()
lureChoice2()
sFa2()
sF2(5)
bgs()
tp()
if M.lower=="a":
  docks()
  sF2(0.5)
  print("You catch 3 more small one's but nothing of size")
if M.lower=="b":
  cover()
  sF(2)
dotted()
tdEnd()
dback()
dotted()
InNOut()
burger()
side()
CN()
CNC()
