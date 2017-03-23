#include <dht.h>

dht DHT;

#define DHT11_PIN 2

int soilPin = 7;
int soilValue = 0;
int LDR = 5;
int LDRValue = 0;

void setup()
{
  Serial.begin(115200);
}

void loop()
{
  // READ DATA
  int chk = DHT.read11(DHT11_PIN);
  soilValue = analogRead(soilPin);
  LDRValue = analogRead(LDR);

  // DISPLAY DATA
  Serial.print(DHT.humidity, 1);
  Serial.print("\t");
  Serial.print(DHT.temperature, 1);
  Serial.print("\t");
  Serial.print(soilValue);
  Serial.print("\t");
  Serial.println(LDRValue, DEC);
  delay(100);
}
