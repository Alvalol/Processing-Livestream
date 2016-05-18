from source import Source
import gui

add_library('peasycam')

POSX = 90
POSY = 130
pixelcollection = []

global source,sourceMovie

def setup():
    global source, sourceMovie,cp5, minBright,maxBright
    size(1280,720,P3D)
    frameRate(24)
    noSmooth()
    #smooth(8) 
    #PeasyCam(this,100)
    #GUI
    #font = createFont("sansserif",20)
    #cp5 = ControlP5(this)
    #slider = cp5.addSlide("param1","test",minBright,maxBright)
    #slider.setPosition(400,20).setSize(200,20)
     #Movie
    sourceMovie = Movie(this,"movie.mp4")  
#    source = Source(PVector(0,0,0))
    background(0)
    sourceMovie.loop()
    sourceMovie.jump(80)
    sourceMovie.speed(1) 
    sourceMovie.volume(0)




def draw():
    global source
    background(0)
    #background(0)
    scale(1.8)
    pushMatrix()
    translate(197,80,190)
    rectGrid()
    popMatrix()


    #image(sourceMovie,0,0)
    #print brightness(mouseX + mouseY * width)
#   source.run()
    #blender()
    #saveFrame("movie/movietestP2-#######.png")




def movieEvent(source):
    source.read()

def fetchPixels():
        global tSource, sourceMovie, minBright, maxBright, minDepth, maxDepth
        sourceMovie.loadPixels()
        tSource = sourceMovie
        skip = 4
        minBright = 220#140
        maxBright = 255
        minDepth = -5
        maxDepth = 5
        pixelcollection = []

        
        for x in range(0,tSource.width,skip):
            for y in range(0,tSource.height,skip):
                loc = x + y * tSource.width
                if brightness(tSource.pixels[loc]) < minBright or tSource.pixels[loc] > maxBright:
                    pixelcollection.append(PVector(x,y,map(brightness(tSource.pixels[loc]),minBright,maxBright, minDepth,maxDepth)))




        return pixelcollection 


def blender():
      blendMode(SUBTRACT);
      fill(20);
      noStroke();
      rect(0, 0, width*2, height*2);
      blendMode(BLEND);

def rectGrid():
        counter = 0
        moviepixels = fetchPixels()
     #   for x in range(0,tSource.width,4):
     #       for y in range(0,tSource.height,4):

        beginShape(TRIANGLE_STRIP)
        for i in moviepixels:
                fill(map(i.z,minDepth,maxDepth,minBright,maxBright),80)
                counter+=1
                pushMatrix()
                translate(i.x,i.y,i.z)
                #strokeWeight(map(i.z,minDepth,maxDepth,0,2))
                #stroke(0)
                noStroke()
                #strokeWeight(1)
                #fill(255)

                #strokeCap(SQUARE)
                #rect(i.x,i.y,2,2)
                box(4)
                popMatrix()

                #point(i.x,i.y,i.z)
                #curveVertex(i.x,i.y,i.z)

                
              