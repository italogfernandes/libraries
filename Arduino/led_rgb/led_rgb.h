#ifndef LED_RGB_H
#define LED_RGB_H

#include <Arduino.h>
#include <cores_rgb.h>

class led_rgb{
public:
  led_rgb(uint8_t red_pin, uint8_t green_pin, uint8_t blue_pin); //constructor
  bool led_status; //Acesso ou apagado
  uint8_t RED_PIN;  //Pino do arduino conectado ao led vermelho
  uint8_t GREEN_PIN;  //Pino do arduino conectado ao led verde
  uint8_t BLUE_PIN;  //Pino do arduino conectado ao led azul
  void led_init();
  void acender(uint8_t *color_vec);
  void apagar();
private:
  unsigned long tempo, tempoAtual;
};

#endif
