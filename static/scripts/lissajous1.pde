void setup()
{
  size(100, 100);
  background(240);
  noStroke();
  fill(50, 50, 255);
  //frameRate(10);
}

float A = 1, B = 1;
float a = 2, b = 2;
float d = PI/2;
float tCircle = 0;
float step = .02;
float guideDotSize = 8;
float scale = 50;

float pa, pb, pd;
float px, py;

//float colrtheta = random(0, PI), colgtheta = random(0, PI), colbtheta = random(0, PI), cola = 255;
float colrtheta = 0, colgtheta = 0, colbtheta = 0, cola = 255;

float[] aValues = {1, 1, 1, 2, 2, 2, 3, 3, 3, 3};
float[] bValues = {1, 2, 3, 1, 3, 5, 1, 2, 4, 5};

void draw()
{
  // Oscillate colors
  fill(getColor(colrtheta), getColor(colgtheta), getColor(colbtheta), cola%256);
  colrtheta += random(0, .001);
  colgtheta += random(0, .002);
  colbtheta += random(0, .003);
  //cola += random(0,5);

  int index = aValues.length - 1 - getIndexViaMouse();
  a = aValues[index];
  b = bValues[index];

  step = .02121212121;

  d += .01;

  A = 40;
  B = 40; 

  // Clear the screen
  if (pa != a || pb != b || pd != d)
  {
    background(255);
    //t = 0;
  }

  PVector[] points = getLissajous(A, B, a, b, d, step);
  PVector[] fourPoints = new PVector[4];
  for (int i = 0; i < points.length-3; i++)
  {
    for(int j = 0; j < 4; j++)
    {
      fourPoints[j] = new PVector(width/2 + points[i+j].x, height/2 + points[i+j].y); 
    }
    curve(fourPoints[0].x, fourPoints[0].y, fourPoints[1].x, fourPoints[1].y, fourPoints[2].x, fourPoints[2].y, fourPoints[3].x, fourPoints[3].y);
  }

  // Guide Dot
  float x = A*sin(a*tCircle+d);
  float y = B*sin(b*tCircle);
  fill(255, 220, 50);
  ellipse(width/2 + x, height/2 + y, guideDotSize, guideDotSize);
  tCircle += step/2;

  pa = a;
  pb = b;
  pd = d;
}


/** Draw all points at once */
PVector[] getLissajous(float A, float B, float a, float b, float d, float step)
{
  int n = 209;
  step = PI / n * 10;
  float t = 0;

  PVector[] points = new PVector[n];

  for (int i = 0; i < n; i++)
  {
    float x = A*sin(a*t+d);
    float y = B*sin(b*t);    
    points[i] = new PVector(x, y);

    t += step;
  }

  return points;
}

/**
  Colors follow a sine curve to remain cyclical
*/
float getColor(float theta)
{
  return min(abs(sin(theta)) * 255F, 200); 
}

int getIndexViaMouse()
{
  return round((mouseX / (float)width + mouseY / (float)height) / 2F * aValues.length); 
}