add_library('video')

class Source():
    
    
    def __init__(self, pos):
        self.pos = pos
        self.pixelcollection = []
        
        
    def run(self):
        self.display()
        self.fetchPixels()
        
    def display(self):
        moviepixels = self.fetchPixels()
        
        for p in moviepixels:
            stroke(255)
            point(p.x,p.y,p.z)
            
        
    def fetchPixels(self):
        global tSource, sourceMovie
        sourceMovie.loadPixels()
        skip = 4
        minBright = 100
        maxBright = 255
        minDepth = -250
        maxDepth = 250
        
        for x in range(0,tSource.width,skip):
            for y in range(0,tSource.height,skip):
                loc = x + y * tSource.width
                if (brightness(tSource.pixels[loc]) > 100):
                    self.pixelcollection.append(PVector(x,y,map(brightness(tSource.pixels[loc]),minBright,maxBright, minDepth,maxDepth)))
                    
        return self.pixelcollection