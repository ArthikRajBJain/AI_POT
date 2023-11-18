


int num=200; // Number of Samples to be taken
int time=15; // Time interval in milli seconds between two samples
double next;
int count=0;

void setup()
{
  Serial.begin(1000000); // Start Serial
  pinMode(13, OUTPUT);     // Onboard LED set as OUTPUT
  pinMode(2, INPUT_PULLUP);       // Switch pin set to INPUT
  pinMode(A0, INPUT);      // X-Axis Input
  pinMode(A1, INPUT);      // Y-Axis Input
}

void loop()
{
  if(!digitalRead(2))
  {
    next=millis()+time;
    while(1)
    {
      if(millis()>=next)
      {
        next=millis()+time;
        Serial.print(analogRead(A0));
        Serial.print(",");
        Serial.print(analogRead(A1));
        count++;
        if(count==num)
        {
          Serial.print("\n");
          count=0;
          break;
        }
        else
        {
          Serial.print(",");
        }
      }
    }
  }
}