#include<reg24le1.h>
#include<nRF-SPICommands.h>
#include<hal_delay.h>
#include<hal_adc.h>

#define LED_VM	P03
#define LED_VD	P06
#define BTN1		P14
#define BTN2		P02

/**************************************************/
//** AD feature configuration function *** /
//* Function Name: adc_config (); no parameters passed, used to initialize the AD conversion * /
void adcInit(void)
{
	ADCCON2  = 0x00; // set to single-step conversion and energy, speed 2ksps
	ADCCON3 |= 0x60; // precision 12bit, the data right justified
	ADCDATH &= 0xF0; // conversion result register is cleared
	ADCDATL &= 0x00;
	P0DIR   |= 0x07; // Set the input channel converted to 0,1,2
	P0      &= 0xF8; // initialize port is low
}
/**************************************************/
//* Read AD conversion result performance function, pip_num save the channel number, returns AD conversion result * /
//* Defined static variables through loop reads 0.1.2 three channels * /
uint8_t readADCtoFIFO (uint8_t num)
{
		//uint16_t res = 0;
		//static uint8_t num = 0;
		ADCCON1 = BIT7 + (num << 2) + BIT0; // set the conversion of the channel, set the reference VDD, and start
		while (!(ADCCON1 & BIT6)); // wait for start
		while ((ADCCON1 & BIT6)); // wait for the completion of the conversion
		return (ADCDATL);
}

void setup(){
	//Iniciar pinos
	//1 é pra entrada
	//0 é pra saida
	P0DIR = 0xB7; //1011 0111
	P1DIR = 0xFF; //1111 1111
	//Configurar o AD
	
	//Configurando rede
	rf_init(ADDR_HOST,
	ADDR_HOST,30,RF_DATA_RATE_250kbps,
	RF_TX_POWER_0dBm);
	LED_VD = 1;//Acende led verde
	delay_ms(500);
	LED_VD = 0;//Apaga led verde
	delay_ms(500);
	LED_VD = 1;//Acende led verde
	delay_ms(500);
	LED_VD = 0;//Apaga led verde
}
void main(void){
	setup();
	while(1){
		//The main Loop
		//Chegou nova mensagem
		if(newPayload){
			newPayload = 0;
			if(rx_buf[0] == 0){
				LED_VM = 0;
			} else {
				LED_VM = 1;
			}
		}
		//Botão
		if(BTN1 == 0){
			//Transmitir mensagem de acender
			tx_buf[0] = 1;
			TX_Mode_NOACK(1);
		}
		//italogsfernandes@gmail.com
		if(BTN2 == 0){
			//Transmitir mensagem de apagar
			tx_buf[0] = 0;
			TX_Mode_NOACK(1);
		}
	}
}