#include <MsTimer2.h>

void interupt();

void setup() { 
    Serial.begin(9600); 
    MsTimer2::set(1000, interupt); 
    MsTimer2::start();
} 
 
void loop() {
    int data = Serial.read() - '0';
    digitalWrite(13, data);
    delay(1000);
}

void interupt(){
    Serial.println("interupt!");
}
