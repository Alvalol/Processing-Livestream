class Flock(object):
    
    def __init__(self):
        self.flock = []

        
    def run(self):
        for b in self.flock:
            b.run(self.flock)
            print(len(self.flock))
       # self.cleanup()

            
    def addBird(self, b):
           self.flock.append(b)
           
    def cleanup(self):
        if frameRate < 20:
            self.flock.pop(0)