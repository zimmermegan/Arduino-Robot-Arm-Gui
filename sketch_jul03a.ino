#include <Servo.h>
//#include <Dynamixel_Serial.h>
//#include <NewSoftSerial.h>
Servo myservo;
Servo gripper;  // create servo object to control a servo
//Servo joint;
//Servo base;

// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
int posGripper = 0;
int stopingContinous = 95.5;

//input variables
int upbutton = 2;
int downbutton = 3;
int openbutton = 5;
int closebutton = 7;
int grabButton = 13;



void setup() {
  myservo.attach(9);// attaches the servo on pin 9 to the servo object
  gripper.attach(8);//attaching servo to 8 pin
  Serial.begin(9600);
}
void upCont(){
  myservo.write(0);
  delay(50);
  myservo.write(95.5);
  pos +=1;
  }
void downCont(){
  myservo.write(0);
  delay(50);
  myservo.write(95.5);
  pos -=1;
}
/**
void loop() {

  for (pos = 0; pos <= 90; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    //myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(60000000);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 90; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
  //  myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}**/

void openClaw(){
  //left
  gripper.write(180);
  delay(500);
  gripper.write(95.5);
  delay(500);
  posGripper = 1;
  }
void closeClaw(){
  //right
  gripper.write(0);
  delay(500);
  gripper.write(95.5);
  delay(500);
  posGripper = 0;
}
void grab()
{
  gripper.write(180); //left
  delay(500);
  gripper.write(95.5);
  delay(500);
  gripper.write(0);
  delay(500);
  gripper.write(95.5);
  }
void loop() {
  //Serial.println("Hello world from Ardunio!"); // write a string

  if (Serial.available())
  {
    int inpu = Serial.read();
    Serial.println("current number");
    Serial.println(inpu);
    int input = int(inpu);
    
    if (input == 50)
    {
      upCont();
    }
    if(input ==51)
    {
      downCont();
    }
    if(input == 53)
    {
      openClaw();
      }
    if(input ==55)
    {
      closeClaw();
      }
    if(input==49)
    {
      grab();
      }
  }
//  val = analogRead(potpin);            // reads the value of the potentiometer (value between 0 and 1023)
  //val = map(val, 0, 1023, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
  //myservo.write(95.5);  // sets the servo position according to the scaled value
  //grab();
  //delay(6000000000);                           // waits for the servo to get there
}
