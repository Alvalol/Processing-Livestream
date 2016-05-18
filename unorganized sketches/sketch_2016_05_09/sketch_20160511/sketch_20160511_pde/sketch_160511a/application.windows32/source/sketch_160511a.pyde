#pixels, PImage, img
# x + (y *width)

pixelcollection = []
rot = 0


def setup():
    size(500,500,P3D)
    global photo
    photo = loadImage("img.jpg")

    
def draw():
    background(0)
    global rot
    pushMatrix()
    translate(width/2,height/2)
    rotateY(sin(rot))
    popMatrix()
   
   #image(photo,-100,0)
    photo.loadPixels()     
    for x in range(0,photo.width,4):
        for y in range(0,photo.height,4):
            loc = x + y * photo.width
            if (brightness(photo.pixels[loc]) > 40 and loc % 2 == 0):
                pixelcollection.append(PVector(x,y,map(brightness(photo.pixels[loc]),0,255,0,150)))


    for p in pixelcollection:
        stroke(map(p.z,0,150,0,255))
        strokeWeight(1)
        point(p.x,p.y,p.z)
        
    if len(pixelcollection) > 100:
        pixelcollection.pop(int(random(0,len(pixelcollection)-1)) )
                            

    rot+=0.1