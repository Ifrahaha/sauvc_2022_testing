#include <Servo.h>

byte servoPin1 = 9;
byte servoPin2 = 11;
byte servoPin3 = 10;
byte servoPin4 = 6;
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

void setup() {
    servo1.attach(servoPin1);
    servo2.attach(servoPin2);
    servo3.attach(servoPin3);
    servo4.attach(servoPin4);
    servo1.writeMicroseconds(1500); 
    servo2.writeMicroseconds(1500); 
    servo3.writeMicroseconds(1500); 
    servo4.writeMicroseconds(1500); 
    delay(7000); 
}

void loop() { 
    delay(10000);
    forward(100);
    delay(10000);
    right(100);
    delay(2500);
    forward(100);
    delay(10000);
    up(150);
    delay(10000);
    back_down(100);
    delay(10000);
    left_down(100);
    delay(2500);
    down(150);
    delay(10000);
    hold();
}

void backward(int x)
{
    servo1.writeMicroseconds(1500+x);
    servo2.writeMicroseconds(1500+x);
}

void forward(int x)
{
    servo1.writeMicroseconds(1500-x);
    servo2.writeMicroseconds(1500-x);
}

void right(int x)
{
    servo1.writeMicroseconds(1500+x);
    servo2.writeMicroseconds(1500-x);
}

void left(int x)
{
    servo1.writeMicroseconds(1500-x);
    servo2.writeMicroseconds(1500+x);
}

void up(int x)
{
    servo3.writeMicroseconds(1500+x);
    servo4.writeMicroseconds(1500+x);
}

void down(int x)
{
    servo3.writeMicroseconds(1500-x);
    servo4.writeMicroseconds(1500-x);
}

void hold()
{
    servo1.writeMicroseconds(1500);
    servo2.writeMicroseconds(1500);
    servo3.writeMicroseconds(1500);
    servo4.writeMicroseconds(1500);
}

void for_down(int x)
{
    servo3.writeMicroseconds(1500+x);
    servo4.writeMicroseconds(1500+x);
    servo1.writeMicroseconds(1500-x);
    servo2.writeMicroseconds(1500-x);
}

void back_down(int x)
{
    servo3.writeMicroseconds(1500+x);
    servo4.writeMicroseconds(1500+x);
    servo1.writeMicroseconds(1500+x);
    servo2.writeMicroseconds(1500+x);
}

void left_down(int x)
{
    servo3.writeMicroseconds(1500+x);
    servo4.writeMicroseconds(1500+x);
    servo1.writeMicroseconds(1500-x);
    servo2.writeMicroseconds(1500+x);
}

