
global f,s, poemlist

def setup():
    background(0)    
    global f,s, poemlist,textx,texty
    size(500,500,P2D)
    frameRate(24)
    smooth(8)
    #background(255)
    poemlist = []
    
    font = createFont('ACaslonPro-BoldItalic',32)
    textFont(font)
    textAlign(CENTER,BOTTOM)
    f = loadStrings('poem.txt')
    dictwords = {}
    
    for string in f:
         s = string.encode('utf8') 
         poemlist.append(s)



         #minstrlenght = len(min(f, key= len))
         #maxstrlenght = len(max(f, key= len))
         
         #fill(map(len(string),minstrlenght,maxstrlenght,100,0),
         #     map(len(string),minstrlenght,maxstrlenght,100,0),
         #     map(len(string),minstrlenght,maxstrlenght,100,0))


               


def draw():

    texty = 43
    textx = 42
    blender()
    offx = random(-1,1)


    for phrases in poemlist:
        newphrases =  phrases.split()
        for i in newphrases:

            fill(255,map(len(i),2,11,255,150))
            textSize(map(len(i),2,11,16+offx,32+offx))
            text(i,textx,texty)
            textx+=40
            if textx >= width - 40 :
                texty+=43
                textx = 52
 
def blender():
      blendMode(SUBTRACT);
      fill(40);
      noStroke();
      rect(0, 0, width*2, height*2);
      blendMode(BLEND);
    