#pixels, PImage, img
# x + (y *width)

pixelcollection = []



def setup():
    background(255)
    size(500,500,P2D)
    global photo
    photo = loadImage("image.jpg")
    photo.loadPixels()  
    
def draw():
    #background(0)
   #image(photo,-100,0)
   
    for x in range(photo.width):
        for y in range(photo.height):
            loc = x + y * photo.width
            if (brightness(photo.pixels[loc]) > 50): #and loc % 10 == 0):
                pixelcollection.append(PVector(x,y,map(brightness(photo.pixels[loc]),0,255,0,100)))
                if len(pixelcollection) > 100:
                    pixelcollection.pop(0)

    for p in pixelcollection:
        stroke(0)
        strokeWeight(5)
        pushMatrix()
        translate(mouseX,mouseY)
        point(p.x,p.y,p.z)
        popMatrix()
    