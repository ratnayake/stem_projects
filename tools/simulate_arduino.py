from pathlib import Path
import subprocess,re,tempfile
root=Path(__file__).resolve().parents[1]
arduino=r'''
#pragma once
#include <algorithm>
#include <cmath>
#include <cstring>
#include <sstream>
#include <string>
#include <deque>
#include <cassert>
#include <cstdint>
using byte=unsigned char;
const int HIGH=1,LOW=0,INPUT=0,OUTPUT=1,INPUT_PULLUP=2,A0=14,A1=15;
unsigned long clock_ms=0;
int inputs[32],outputs[32],pwm[32];
unsigned long echoes[32];
std::deque<char> incoming;
unsigned long millis(){return clock_ms;}
void delay(unsigned long t){clock_ms+=t;}
void delayMicroseconds(unsigned long){}
void pinMode(byte,int){}
int digitalRead(byte p){return inputs[p];}
void digitalWrite(byte p,int v){outputs[p]=v;}
void analogWrite(byte p,int v){pwm[p]=v;}
int analogRead(byte){return 512;}
unsigned long pulseIn(byte p,int,unsigned long){return echoes[p];}
void tone(byte,int,unsigned long=0){}
void noTone(byte){}
void randomSeed(unsigned long){}
long random(long a,long){return a;}
using std::min; using std::max;
template<class T> T constrain(T v,T a,T b){return std::min(b,std::max(a,v));}
struct Printer {
 std::string text;
 void begin(int){}
 template<class T> void print(T v){std::ostringstream s;s<<v;text+=s.str();}
 void print(double v,int){print(v);}
 template<class T> void println(T v){print(v);text+='\n';}
 void println(){text+='\n';}
} Serial;
void tick(unsigned long t){clock_ms+=t;}
'''
software=r'''
#pragma once
#include <Arduino.h>
struct SoftwareSerial {
 SoftwareSerial(byte,byte){}
 void begin(int){}
 bool available(){return !incoming.empty();}
 char read(){char c=incoming.front();incoming.pop_front();return c;}
};
'''
servo=r'''
#pragma once
int servo_angle=0;
struct Servo {void attach(byte){} void write(int angle){servo_angle=angle;}};
'''
lcd=r'''
#pragma once
#include <Arduino.h>
struct hd44780_I2Cexp: Printer {
 int begin(int,int){return 0;}
 void backlight(){}
 void clear(){text.clear();}
 void setCursor(int,int){}
};
'''
tests={
8:r'''
int main(){
 std::fill(inputs,inputs+32,HIGH);setup();
 // Starting with a held button never runs the countdown.
 inputs[2]=LOW;loop();tick(30);loop();
 for(int i=0;i<10;i++){tick(1000);loop();}
 for(int p=3;p<=7;p++)assert(outputs[p]==LOW);
 inputs[2]=HIGH;loop();tick(30);loop();
 tick(1000);loop();assert(outputs[3]==HIGH);
 // Even an early raw press cancels, including during the first light.
 inputs[8]=LOW;loop();assert(Serial.text.find("False start")!=std::string::npos);
 for(int p=3;p<=7;p++)assert(outputs[p]==LOW);
 // Start a new race and provide no reactions; it must show two timeouts, no winner.
 inputs[8]=HIGH;loop();tick(30);loop();tick(2100);loop();
 inputs[2]=LOW;loop();tick(30);loop();inputs[2]=HIGH;loop();tick(30);loop();
 for(int i=0;i<5;i++){tick(1000);loop();}tick(1001);loop();tick(3001);loop();
 assert(Serial.text.find("P1: timeout")!=std::string::npos);
 assert(Serial.text.find("P2: timeout")!=std::string::npos);
 assert(Serial.text.find("No winner")!=std::string::npos);
}
''',
12:r'''
int main(){
 std::fill(inputs,inputs+32,HIGH);setup();
 echoes[10]=0;
 assert(medianDistance()<0); // Five timeouts never become 400cm.
 echoes[10]=1750;float d=medianDistance();assert(d>29 && d<31);
}
''',
13:r'''
int main(){
 std::fill(inputs,inputs+32,HIGH);setup();
 echoes[10]=600; // Hand about 10cm away.
 for(int i=0;i<100;i++){tick(25);loop();}assert(servo_angle==90);
 echoes[10]=6000; // Reference target beyond clear threshold.
 for(int i=0;i<170;i++){tick(25);loop();}assert(servo_angle<90);
 echoes[10]=0; // Missing echo while closing must reopen rather than close.
 for(int i=0;i<100;i++){tick(25);loop();}assert(servo_angle==90);
 for(int i=0;i<200;i++){tick(25);loop();}assert(servo_angle==90);
}
''',
14:r'''
int main(){
 std::fill(inputs,inputs+32,HIGH);setup();
 echoes[10]=600;echoes[12]=600; // Approaching car and occupied barrier.
 for(int i=0;i<100;i++){tick(25);loop();}assert(servo_angle==95);
 echoes[10]=6000;echoes[12]=6000;
 for(int i=0;i<115;i++){tick(25);loop();}assert(servo_angle<95);
 echoes[12]=0;
 for(int i=0;i<100;i++){tick(25);loop();}assert(servo_angle==95);
 for(int i=0;i<200;i++){tick(25);loop();}assert(servo_angle==95);
}
''',
18:r'''
int main(){
 std::fill(inputs,inputs+32,HIGH);setup();assert(pwm[5]==0 && pwm[6]==0);
 incoming.push_back('F');loop();assert(pwm[5]>0 && pwm[6]>0);
 tick(399);loop();assert(pwm[5]>0);
 tick(1);loop();assert(pwm[5]==0 && pwm[6]==0); // Lost link stops at timeout.
 for(int i=0;i<10;i++){tick(100);incoming.push_back('F');loop();assert(pwm[5]>0);}
 incoming.push_back('X');loop();assert(pwm[5]==0 && pwm[6]==0);
 incoming.push_back('F');incoming.push_back('\r');incoming.push_back('\n');loop();assert(pwm[5]>0);
 incoming.push_back('S');loop();assert(pwm[5]==0 && pwm[6]==0);
}
'''
}
with tempfile.TemporaryDirectory(prefix='electronics-runtime-') as folder:
 p=Path(folder)
 (p/'Arduino.h').write_text(arduino);(p/'SoftwareSerial.h').write_text(software)
 (p/'Servo.h').write_text(servo);(p/'Wire.h').write_text('#pragma once\n');(p/'hd44780.h').write_text('#pragma once\n')
 (p/'hd44780ioClass').mkdir();(p/'hd44780ioClass'/'hd44780_I2Cexp.h').write_text(lcd)
 for n,test in tests.items():
  path=next((root/'projects').glob(f'project-{n:02}-*.md'))
  code=re.findall(r'```cpp\n(.*?)```',path.read_text(),re.S)[0]
  source=p/f'project_{n}.cpp';source.write_text(code+'\n'+test)
  executable=p/f'project_{n}'
  subprocess.run(['g++','-std=c++11','-I',str(p),str(source),'-o',str(executable)],check=True)
  subprocess.run([str(executable)],check=True)
  print(f'PASS simulated failure/edge cases: project {n:02}',flush=True)
