#include "led_rbg.h"


led_rgb::led_rgb(uint8_t red_pin, uint8_t green_pin, uint8_t blue_pin){
  RED_PIN = red_pin;
  GREEN_PIN = green_pin;
  BLUE_PIN = blue_pin;
}

void led_rgb::apagar(){
    digitalWrite(RED_PIN,LOW); digitalWrite(GREEN_PIN,LOW); digitalWrite(BLUE_PIN,LOW);
}

void led_rgb::acender(uint8_t *color_vec){
    analogWrite(RED_PIN, color_vec[0]);
    analogWrite(GREEN_PIN, color_vec[1]);
    analogWrite(BLUE_PIN, color_vec[2]);
}

void led_rbg::led_init(){
    pinMode(RED_PIN,OUTPUT); pinMode(GREEN_PIN,OUTPUT); pinMode(BLUE_PIN,OUTPUT);
    apagar();
}


class led_rgb{
public:
  led_rgb(uint8_t red_pin, uint8_t green_pin, uint8_t blue_pin); //constructor
  bool led_status; //Acesso ou apagado
  uint8_t RED_PIN;  //Pino do arduino conectado ao led vermelho
  uint8_t GREEN_PIN;  //Pino do arduino conectado ao led verde
  uint8_t BLUE_PIN;  //Pino do arduino conectado ao led azul
  void acender(uint8_t *cor);
  void apagar();
private:
  unsigned long tempo, tempoAtual;
};

#endif
