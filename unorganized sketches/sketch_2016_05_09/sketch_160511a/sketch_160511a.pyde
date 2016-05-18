rot = 0
desiredPoints = 1000

class Portrait():
    def __init__(self,pos,photo):
        
        self.photo = photo
        self.pos = pos
        self.xoff = 0.0
        self.rot = 0.0
        self.pixelcollection = []
            

    def display(self):
        
        pix = self.fetchPoints()

        for p in pix:
            stroke(map(p.z,-100,100,0,255),100)
            #stroke(255)
            rectMode(CENTER)
            strokeCap(SQUARE)
            strokeWeight(3)


            point(p.x,p.y,p.z)

            offset = PVector.random3D()
            offset.mult(0.9)
            #p.add(offset)

        self.rot+=0.05
        endShape()


    
    def fetchPoints(self):
        newphoto = loadImage(self.photo)
        newphoto.loadPixels()
        #image(newphoto,0,0)
        


        for x in range(0,newphoto.width,4):
            for y in range(0,newphoto.height,4):
                loc = x + y * newphoto.width
                if (brightness(newphoto.pixels[loc]) >100):
                  self.pixelcollection.append(PVector(x,y,map(brightness(newphoto.pixels[loc]),100,255,-250,250)))

                if len(self.pixelcollection) > loc/10:
                  self.pixelcollection.pop(0)
        return self.pixelcollection


portrait = Portrait(PVector(10,10,10),"img.jpg")




def setup():
    size(500,500,P3D)
    frameRate(24)

    #PeasyCam(this,100)



    
def draw():
    background(10)
    global rot 
    rotateX(rot)
    portrait.display()

    
    rot+=0.005
    saveFrame("asdf-######.png")
    