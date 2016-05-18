public class Agent
{
  public PVector pos;
  public color col;
  
 public Agent()
 {
   pos = new PVector(0,0);
   col = color(0);
  // float xoff = 0.0;

 }
  
 void run()
 {
     display();
 }
 
 void display()
 {
        
        fill(col,255);
        noStroke();
        pushMatrix();
        translate(pos.x,pos.y,pos.z);
        box(8);
        popMatrix();

 }
 
 
}