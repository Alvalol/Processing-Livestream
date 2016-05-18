desiredSymbols = 5
global rot
rot = 0

def setup():
   size(600,600,P3D)
   smooth(0)
   scale(0.1)
   #PeasyCam(this,100)

   background(0)
   posx = 10
   posy = 0
   for i in range(desiredSymbols):

       newSymbol = Symbol(posx,posy,height)
       SymbolList.append(newSymbol)
       if posx <= width:
            #rectmode
            #posx+=2
            #box mode
            posx+=10

def draw():
       #background(0)

   for Symbol in SymbolList:
       Symbol.update()
   if(mousePressed):
       del SymbolList[:]
       saveFrame(“export-####.png”)
       exit()