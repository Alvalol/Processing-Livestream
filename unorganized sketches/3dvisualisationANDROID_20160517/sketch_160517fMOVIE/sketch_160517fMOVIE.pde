import ketai.camera.*;
import ketai.cv.facedetector.*;
import ketai.data.*;
import ketai.net.*;
import ketai.net.bluetooth.*;
import ketai.net.nfc.*;
import ketai.net.nfc.record.*;
import ketai.net.wifidirect.*;
import ketai.sensors.*;
import ketai.ui.*;


import processing.video.*;
import peasy.*;


PeasyCam cam;
int desiredAgents = 1;
AgentGroup agentGroup;
Movie sourceMovie;


void settings()
{
  size(480,800,P3D);
  smooth(8);
}
void setup() 
{
  
  //debug
  
 
  
  sourceMovie = new Movie(this, "movie.mp4");
  sourceMovie.loop();
  
  agentGroup = new AgentGroup(sourceMovie);

  
  for(int x = 0; x < desiredAgents; x++)
  {
    Agent agent = new Agent();
    agentGroup.addAgent(agent);

  }


}

void draw()
{
  background(0);
  pushMatrix();
  agentGroup.run();
  popMatrix();
  println(frameRate);

}

void movieEvent(Movie m)
{
     m.read(); 
}

void blender()
{
    blendMode(SUBTRACT);
    fill(10);
    noStroke();
    rect(0,0,width*2,height*2);
    blendMode(BLEND);
}     
               