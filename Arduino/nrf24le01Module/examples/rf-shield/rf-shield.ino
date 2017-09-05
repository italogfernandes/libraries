#include "nrf24le01Module.h"
#include "led_rgb.h"

#define BROADCAST_ADDR  0x00

#define UART_BAUDRATE       115200


led_rgb status_led(7, 6, 5); //R_pin,G_pin,B_pin
nrf24le01Module host_nrf(2, 4, 3); //IRQ, CE, CSN

char serialOp;

unsigned long received_millis, timeout_millis, actual_millis;
void setup() {
  Serial.begin(UART_BAUDRATE);
  status_led.init();
  host_nrf.rf_init(host_nrf.ADDR_HOST, host_nrf.ADDR_HOST, 30, RF_DATA_RATE_2Mbps, RF_TX_POWER_0dBm); //RF Communication
  attachInterrupt(digitalPinToInterrupt(host_nrf.RFIRQ), rf_interrupt, FALLING); //Todo: put inside library
  piscas_iniciais_led();
  Serial.println("Host Iniciado.");
}

void loop() {
  actual_millis = millis();
  if (host_nrf.newPayload) {
    received_millis = actual_millis;
    host_nrf.newPayload = 0;
    status_led.acender(LED_COLOR_AQUA);
    Serial.println("**Payload Recebida**");
    Serial.print("Payload Width: "); Serial.println(host_nrf.payloadWidth);
    Serial.print("Payload Data: "); Serial.write(host_nrf.rx_buf, host_nrf.payloadWidth);
    Serial.print("\n");
    Serial.println(host_nrf.rx_buf[0], HEX);
    Serial.print("\n");
  }
  if(actual_millis - received_millis  > 100){
    status_led.apagar();
  }
}

void rf_interrupt(){
 host_nrf.RF_IRQ();
}

void piscas_iniciais_led() {
  status_led.acender(LED_COLOR_RED); delay(500);
  status_led.apagar(); delay(500);
  status_led.acender(LED_COLOR_GREEN); delay(500);
  status_led.apagar(); delay(500);
  status_led.acender(LED_COLOR_BLUE); delay(500);
  status_led.apagar(); delay(500);
}


