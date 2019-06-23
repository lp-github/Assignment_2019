// TableTrafficLight.c
// Runs on LM4F120 or TM4C123
// Index implementation of a Moore finite state machine to operate
// a traffic light.
// Daniel Valvano, Jonathan Valvano
// July 20, 2013

/* This example accompanies the book
   "Embedded Systems: Introduction to ARM Cortex M Microcontrollers",
   ISBN: 978-1469998749, Jonathan Valvano, copyright (c) 2013
   Volume 1 Program 6.8, Example 6.4
   "Embedded Systems: Real Time Interfacing to ARM Cortex M Microcontrollers",
   ISBN: 978-1463590154, Jonathan Valvano, copyright (c) 2013
   Volume 2 Program 3.1, Example 3.1

 Copyright 2013 by Jonathan W. Valvano, valvano@mail.utexas.edu
    You may use, edit, run or distribute this file
    as long as the above copyright notice remains
 THIS SOFTWARE IS PROVIDED "AS IS".  NO WARRANTIES, WHETHER EXPRESS, IMPLIED
 OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, IMPLIED WARRANTIES OF
 MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE APPLY TO THIS SOFTWARE.
 VALVANO SHALL NOT, IN ANY CIRCUMSTANCES, BE LIABLE FOR SPECIAL, INCIDENTAL,
 OR CONSEQUENTIAL DAMAGES, FOR ANY REASON WHATSOEVER.
 For more information about my classes, my research, and my books, see
 http://users.ece.utexas.edu/~valvano/
 */

// east facing red light connected to PB5
// east facing yellow light connected to PB4
// east facing green light connected to PB3
// north facing red light connected to PB2
// north facing yellow light connected to PB1
// north facing green light connected to PB0
// north facing car detector connected to PE1 (1=car present)
// east facing car detector connected to PE0 (1=car present)
#include "..//inc//tm4c123gh6pm.h"
#include "PLL.h"
#include "SysTick.h"
#include "Timer0A.h"
#include "UART.h"
#define LIGHT                   (*((volatile unsigned long *)0x40025038))
#define GPIO_PORTB_OUT          (*((volatile unsigned long *)0x400050FC)) // bits 5-0

#define GPIO_PORTE_IN           (*((volatile unsigned long *)0x4002401C)) // bits 2-0
#define SENSOR                  (*((volatile unsigned long *)0x40025004))


#define SYSCTL_RCGC2_GPIOE      0x00000010  // port E Clock Gating Control
#define SYSCTL_RCGC2_GPIOB      0x00000002  // port B Clock Gating Control


#define GPIO_PORTF_IN           (*((volatile unsigned long *)0x4002401C)) // bits 2-0
	
#define SYSCTL_RCGC2_GPIOF      0x00000020
//#define NVIC_ST_CURRENT_R   (*((volatile unsigned long *)0xE000E018))

// Linked data structure
struct State {
  unsigned long Out; 
  unsigned long Time;  
  unsigned long Next[8];}; 
typedef  struct State STyp;
#define goE   0
#define waitE 1
#define goN   2
#define waitN 3
#define walkState 1
#define normalState 0
#define F16HZ (50000000/16)
#define F20KHZ (50000000/20000)
unsigned long S;  // index to the current state 
unsigned long Input; 
long last = 0;
int timestamp = 0;
int state= normalState;
void DisableInterrupts(void); // Disable interrupts
void EnableInterrupts(void);  // Enable interrupts
long StartCritical (void);    // previous I bit, disable interrupts
void EndCritical(long sr);    // restore I bit to previous value
void WaitForInterrupt(void);  // low power mode

// global variable visible in Watch window of debugger
// increments at least once per button press
volatile uint32_t FallingEdges = 0;
void EdgeCounter_Init(void){                          
  SYSCTL_RCGCGPIO_R |= 0x00000020; // (a) activate clock for port F
	FallingEdges = 0;             // (b) initialize counter
  GPIO_PORTF_LOCK_R = 0x4C4F434B;
	GPIO_PORTF_CR_R=0x03;
	GPIO_PORTF_DIR_R &= ~0x11;    // (c) make PF0 in (built-in button)
  GPIO_PORTF_AFSEL_R &= ~0x11;  //     disable alt funct on PF0
  GPIO_PORTF_DEN_R |= 0x11;     //     enable digital I/O on PF0   
  GPIO_PORTF_PCTL_R &= ~0x000F000F; // configure PF0 as GPIO
  GPIO_PORTF_AMSEL_R = 0;       //     disable analog functionality on PF
  GPIO_PORTF_PUR_R |= 0x11;     //     enable weak pull-up on PF0
  GPIO_PORTF_IS_R &= ~0x11;     // (d) PF0 is edge-sensitive
  GPIO_PORTF_IBE_R &= ~0x11;    //     PF0 is not both edges
  GPIO_PORTF_IEV_R &= ~0x11;    //     PF0 falling edge event
  GPIO_PORTF_ICR_R = 0x11;      // (e) clear flag0
  GPIO_PORTF_IM_R |= 0x11;      // (f) arm interrupt on PF0 *** No IME bit as mentioned in Book ***
  NVIC_PRI7_R = (NVIC_PRI7_R&0xFF00FFFF)|0x00A00000; // (g) priority 5
  NVIC_EN0_R = 0x40000000;      // (h) enable interrupt 30 in NVIC
  EnableInterrupts();           // (i) Clears the I bit
	/*
	  SYSCTL_RCGCGPIO_R |= 0x00000020; // (a) activate clock for port F
	FallingEdges = 0;             // (b) initialize counter
  GPIO_PORTF_LOCK_R = 0x4C4F434B;
	GPIO_PORTF_CR_R=0x03;
	GPIO_PORTF_DIR_R = 0x02;    // (c) make PF0 in (built-in button)
  GPIO_PORTF_AFSEL_R &= ~0x03;  //     disable alt funct on PF0
  GPIO_PORTF_DEN_R |= 0x03;     //     enable digital I/O on PF0   
  GPIO_PORTF_PCTL_R &= ~0x000000FF; // configure PF0 as GPIO
  GPIO_PORTF_AMSEL_R = 0;       //     disable analog functionality on PF
  GPIO_PORTF_PUR_R |= 0x03;     //     enable weak pull-up on PF0
  GPIO_PORTF_IS_R &= ~0x01;     // (d) PF0 is edge-sensitive
  GPIO_PORTF_IBE_R &= ~0x01;    //     PF0 is not both edges
  GPIO_PORTF_IEV_R &= ~0x01;    //     PF0 falling edge event
  GPIO_PORTF_ICR_R = 0x03;      // (e) clear flag0
  GPIO_PORTF_IM_R |= 0x01;      // (f) arm interrupt on PF0 *** No IME bit as mentioned in Book ***
  NVIC_PRI7_R = (NVIC_PRI7_R&0xFF00FFFF)|0x00A00000; // (g) priority 5
  NVIC_EN0_R = 0x40000000;      // (h) enable interrupt 30 in NVIC
  EnableInterrupts();           // (i) Clears the I bit
	*/
}
	
STyp FSM[5]={
 {0x08,200,{waitE,goE,goN,waitN}}, 
 {0x0A, 100,{goN,goE,goE,goE}},
 {0x02,200,{waitN,goE,waitE,waitE}},
 {0x0A, 100,{goE,goE,goN,goN}}
};

void OutCRLF(void){
  UART_OutChar(CR);
  UART_OutChar(LF);
}
void GPIOPortF_Handler(void){
	
	long now=timestamp;
	GPIO_PORTF_ICR_R = 0x11;      // acknowledge flag0
	if(now-last<10){
		last=timestamp;
		return;
	}
	if((GPIO_PORTF_DATA_R&0x01)==0x01){
		
		state=1-state;
		if(state==walkState){
			UART_OutString("Changed to walker mode");
		}
		else{
			UART_OutString("Changed to normal mode");
		}
		OutCRLF();
		FallingEdges = FallingEdges + 1;
		//GPIO_PORTF_DATA_R ^= 0x02;
	}
	if((GPIO_PORTF_DATA_R&0x10)==0x10){
		unsigned long s;
		UART_OutString("input time to goE/goN:(seconds)");
		OutCRLF();
		s=UART_InUHex();
		FSM[0].Time=s*100;
		FSM[2].Time=S*100;
		UART_OutString("goE/goN states now last for ");
		UART_OutUDec(s);
		UART_OutString(" seconds");
		OutCRLF();
	}
	last = timestamp;
}


void UserTask(void){
  
  
  timestamp+=1;
}

int main1(void){
  char i;
  char string[20];  // global to assist in debugging
  uint32_t n;

  PLL_Init();               // set system clock to 50 MHz
  UART_Init();              // initialize UART
  OutCRLF();
  for(i='A'; i<='Z'; i=i+1){// print the uppercase alphabet
    UART_OutChar(i);
  }
  OutCRLF();
  UART_OutChar(' ');
  for(i='a'; i<='z'; i=i+1){// print the lowercase alphabet
    UART_OutChar(i);
  }
  OutCRLF();
  UART_OutChar('-');
  UART_OutChar('-');
  UART_OutChar('>');
  while(1){
    UART_OutString("InString: ");
    UART_InString(string,19);
    UART_OutString(" OutString="); UART_OutString("*");UART_OutString(string);UART_OutString("*"); OutCRLF();

    UART_OutString("InUDec: ");  n=UART_InUDec();
    UART_OutString(" OutUDec="); UART_OutUDec(n); OutCRLF();

    UART_OutString("InUHex: ");  n=UART_InUHex();
    UART_OutString(" OutUHex="); UART_OutUHex(n); OutCRLF();

  }
}


int main(void){ volatile unsigned long delay;
	char i;
  char string[20];  // global to assist in debugging
  uint32_t n;

  PLL_Init();               // set system clock to 50 MHz
  UART_Init();              // initialize UART
  UART_OutString("Traffic Light Management Program started!");
	OutCRLF();
	//UART_OutString("enter help to");
	EdgeCounter_Init();
  PLL_Init();       // 80 MHz, Program 10.1
  SysTick_Init();   // Program 10.2
	UART_Init();  
	
  SYSCTL_RCGC2_R |= 0x12;      // 1) B E
  delay = SYSCTL_RCGC2_R;      // 2) no need to unlock
  GPIO_PORTE_AMSEL_R &= ~0x07; // 3) disable analog function on PE2-0
  GPIO_PORTE_PCTL_R &= ~0x00000FFF; // 4) enable regular GPIO
  GPIO_PORTE_DIR_R &= ~0x07;   // 5) inputs on PE2-0
  GPIO_PORTE_AFSEL_R &= ~0x07; // 6) regular function on PE2-0
  GPIO_PORTE_DEN_R |= 0x07;    // 7) enable digital on PE2-0
  GPIO_PORTB_AMSEL_R &= ~0x3F; // 3) disable analog function on PB5-0
  GPIO_PORTB_PCTL_R &= ~0x00FFFFFF; // 4) enable regular GPIO
  GPIO_PORTB_DIR_R |= 0x3F;    // 5) outputs on PB5-0
  GPIO_PORTB_AFSEL_R &= ~0x3F; // 6) regular function on PB5-0
  GPIO_PORTB_DEN_R |= 0x3F;    // 7) enable digital on PB5-0
  S = goN;  
	
	SYSCTL_RCGC2_R |= 0x20;      // 1) B E
  delay = SYSCTL_RCGC2_R;      // 2) no need to unlock

  GPIO_PORTF_AMSEL_R &= ~0x1F; // 3) disable analog function on PB5-0
  GPIO_PORTF_PCTL_R &= ~0x000FFFFF; // 4) enable regular GPIO
  GPIO_PORTF_DIR_R |= 0x0E;    // 5) outputs on PB5-0
  GPIO_PORTF_AFSEL_R &= ~0x0E; // 6) regular function on PB5-0
  GPIO_PORTF_DEN_R |= 0x0E;    // 7) enable digital on PB5-0
  S = goN;  
	GPIO_PORTF_DATA_R |= 0x08;
	Timer0A_Init(&UserTask, F16HZ);  // initialize timer0A (16 Hz)
	UART_OutString("normal mode");
	OutCRLF();
	UART_OutString("state goE/goN last for 2 seconds");
	OutCRLF();
	UART_OutString("state waitE/waitN last for 1 seconds");
	OutCRLF();
  while(1){
		UART_OutString("traffic light state:\t");
		if(S==goN){
			UART_OutString("goN");
		}
		else if(S==goE){
			UART_OutString("goE");
		}
		else if(S==waitN){
			UART_OutString("waitN");
		}
		else if(S==waitE){
			UART_OutString("waitE");
		}
		else{
			UART_OutString("INVALID STATES");
		}
		OutCRLF();
    LIGHT = FSM[S].Out;  // set lights
    SysTick_Wait10ms(FSM[S].Time);
    Input = SENSOR;     // read sensors
    S = FSM[S].Next[state];  
  }
}

