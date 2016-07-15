#include <Servo.h>
//#include <Dynamixel_Serial.h>
//#include <NewSoftSerial.h>

//Initializing our two servos
Servo myservo;
Servo gripper;  


int pos = 0;    // variable to store the servo position
int posGripper = 0;

//because we accidentally bought continuous rotation servos 
//we store the value at which the servo will stop here
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
void loop()
{
  //getting the serial input from the python script
  if (Serial.available())
  {
    int inpu = Serial.read();
    Serial.println("current number");
    Serial.println(inpu);
    int input = int(inpu);
    //ended up having to change the values out because serial adapted them
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
}
