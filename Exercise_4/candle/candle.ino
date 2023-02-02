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
  
  Serial.begin(9600);
}

// define variables
int redValue;
int greenValue;
int blueValue;
int randomNumber;
void loop()
{
  if(Serial.available() > 0)
  {
    redValue = 255;
    greenValue = 65;
    blueValue = 0;

    int rand=Serial.read();
    //float rand=Serial.read()/255;
    //randomNumber = random(255);
    //float rand = randomNumber/255;
    

    float frandGreen = greenValue*rand;
    float frandBlue = blueValue*rand;
    float frandRed = redValue*rand;

    int randGreen = static_cast<int>(frandGreen);
    int randBlue = static_cast<int>(frandBlue);
    int randRed = static_cast<int>(frandRed);

    //randGreen = rand;

    analogWrite(GREEN, rand);
    analogWrite(BLUE, rand);
    analogWrite(RED, rand);
    
    //Serial.println(rand);
    //delay(500);
    Serial.println("W");
  }
}
