//www.elegoo.com
//2016.12.8

// define pins
#define BLUE 3
#define GREEN 5
#define RED 6

void setup()
{
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  digitalWrite(RED, HIGH);
  digitalWrite(GREEN, HIGH);
  digitalWrite(BLUE, HIGH);
}

// define variables
int redValue;
int greenValue;
int blueValue;

// main loop
void loop()
{
#define delayTime 10 // fading time between colors

  redValue = 255;
  greenValue = 65;
  blueValue = 0;
  analogWrite(GREEN, greenValue);
  analogWrite(BLUE, blueValue);
  analogWrite(RED, redValue);

  


  
}
