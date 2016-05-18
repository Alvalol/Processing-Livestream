from Source import Source

POSX = 90
POSY = 130
pixelcollection = []

global source,sourceMovie

def setup():
    global source, sourceMovie
    size(500,500,P3D)
     
    sourceMovie = Movie(this,"movie.mp4") 
#    source = Source(PVector(0,0,0))
   
    sourceMovie.loop()
    sourceMovie.speed(0.18) 


def draw():
    global source
    background(0)
    fetchPixels()
    #image(sourceMovie,POSX,POSY)
#    source.run()



def movieEvent(source):
    source.read()

def fetchPixels():
        global tSource, sourceMovie
        sourceMovie.loadPixels()
        tSource = sourceMovie
        skip = 4
        minBright = 100
        maxBright = 255
        minDepth = -250
        maxDepth = 250
        
        for x in range(0,tSource.width,skip):
            for y in range(0,tSource.height,skip):
                loc = x + y * tSource.width
                if (brightness(tSource.pixels[loc]) > 100):
                   pixelcollection.append(PVector(x,y,map(brightness(tSource.pixels[loc]),minBright,maxBright, minDepth,maxDepth)))
                   print pixelcollection
                    


print(pixelcollection)

def display():
        moviepixels = self.fetchPixels()
        
        for p in moviepixels:
            stroke(255)
            point(p.x,p.y,p.z)
            