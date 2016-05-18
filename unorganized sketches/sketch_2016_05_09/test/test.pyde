*/

// dynamic list with our points, PVector holds position
ArrayList<PVector> points = new ArrayList<PVector>();

// global configuration
float vector_scale = 0.01; // vector scaling factor, we want small steps
float time = 0.001; // time passes by

void setup() {
 size(540, 540);
 background(200);
 // create points from [-3,3] range
 for (float x=-3; x<=3; x+=0.1) {
  for (float y=-3; y<=3; y+=0.1) {
     PVector v = new PVector(x, y);
     points.add(v);
   }
 }
}

void draw() {
 fill(150,2);
 noStroke();
 rect(0,0,width,height);
 float a = 0,
       ia = TAU/36;
 for (PVector p : points) {
   // map floating point coordinates to screen coordinates
   float xx = map(p.x, -6, 6, 0, width);
   float yy = map(p.y, -6, 6, 0, height);

   float cr = map(xx,0,width,0,150),
         cb = map(yy,0,height,0,150),
         cg = map(xx+yy,0,width+height,0,150);
   stroke(cr,cg,cb,20);
   point(xx, yy); //draw

   // placeholder for vector field calculations
   float n = a/time * map(noise(p.x/5,p.y/5),0,1,-1,1); // 100, 300 or 1000
   // v is vector from the field
   PVector v = new PVector(cos(n),sin(n));

   a += ia;

   p.x += vector_scale * v.x;
   p.y += vector_scale * v.y;
 }
 time += 0.001;
}
#generateme#thanks#code#processing#vector field#creative code#color#design#video#noise#generative art