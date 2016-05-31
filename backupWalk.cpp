// COMPILE: g++ -std=c++11 -pthread -o walk walk.cpp -I/usr/include/python2.7/ -lpython2.7

#include <stdlib.h>
#include <string>
#include <vector>
#include <math.h>
#include <iostream>
#include <unistd.h>
#include <ctime>
#include <Python.h>

#define PI 3.14159265

int legs[6][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {10, 11, 12}, {13, 14, 15}, {16, 17, 18} };
float a       = 197;                                            //lengte femur
float alpha   = 0.5 * PI;                                 //hoek van de maximale stap (90 graden) in radialen!!
float beta    = 0.5 * PI;                                 //hoek tussen tibia en femur (90 graden) in radialen!!
float c       = 200;                                      //lengte tibia
float e       = 10;                                       //hoogte frame van as servo1 tot de grond
float f       = 40;

float b       = sqrt(pow(a, 2)+pow(c,2)-2*a*c*cos(beta));        //afstand b
float gammaa  = acos(pow(c,2)-pow(a,2)-pow(b,2))/(-2*a*b);    //hoek gammaa
float d       = sqrt(pow(b,2)-pow(e,2));                  //afstand d

float delta   = atan(d/e);                                      //hoek delta
float l       = d+f;                                           //uitslag poot in breedterichting

float ss      = l*sin(0.5*alpha);                              //helft van de stap
float s       = 2*ss;                                           //grootte stap van de poot in lengterichting
float sss     = l*cos(0.5*alpha);                               //breedte tot helft van de stap

int y = round(-ss);

int ys[6] = {y, y, y, y, y, y};



void move(int leg[], int pos1, int pos2, int pos3){


    int speed = 200;	
    int speed1 = 500;
    int speed2 = 500;
    int speed3 = 500;

    system(("./original.py " + std::to_string(leg[0]) + " " + std::to_string(leg[1]) + " " + 
         std::to_string(leg[2]) + " " + std::to_string(pos1) + " " + std::to_string(pos2) + " " + 
         std::to_string(pos3) + " " + std::to_string(speed) + " " + std::to_string(speed) + " " + 
         std::to_string(speed)).c_str());
}

void calcLeg(int leg){
    float x = abs(sss-sqrt(pow(l,2)-pow(ys[leg],2)));            //waarbij y is waarde tussen de ss en de -ss maar x moet positief zijn en $
    float dd = d-x;                                       //d herberekend
    float bb = sqrt(pow(dd,2)+pow(e,2));                  //b herberekend
    float betabeta = (acos((pow(bb,2)-pow(a,2)-pow(c,2))/(-2*a*c)));  //beta herberekend
    float gammaagammaa = (acos((pow(c,2)-pow(a,2)-pow(bb,2))/(-2*a*bb)));       //gammaa herberekend

    float servo1 = (ys[leg]/ss) * alpha * 0.5;                              //hoek die de servo ten opzichte van het midden maakt
    float servo2 = delta + gammaagammaa - 0.5 * PI;                //idem. met hoek(90) in radialen
    float servo3 = PI-betabeta;                             //idem.

    float gservo1 = (5.0 / 6.0) * PI - servo1;                       //gecompenseerde hoek t.a.v. servo (150) in radialen
    float gservo2 = (5.0 / 6.0) * PI + servo2;                      //idem. hoek (150) in radialen
    float gservo3 = servo3 + (5.0 / 6.0) * PI;                        //idem. hoek (150) in radialen

    int stappena = round((gservo1/((5.0 / 3.0)*PI))*1023);
    int stappenb = round((gservo2/((5.0 / 3.0)*PI))*1023);                 //idem voor servo2
    int stappenc = round((gservo3/((5.0 / 3.0)*PI))*1023);                 //idem voor servo3

    move(legs[leg], stappena, stappenb, stappenc);
    //std::cout << "Stappen: " << stappena << " - " << stappenb << " - " << stappenc << "\n";
}



int main(){
    while(true){
    	while(ys[2] < ss){
    	    calcLeg(2);
    	    ys[2] += 100;
    	
	    usleep(10000);
    	}
    	
    	move(legs[2], 512, 800, 1000);
    	ys[0] = y;
    	ys[2] = y;
    	usleep(1000000);;
    }
    return 1;
}