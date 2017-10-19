# Libraries
Bibliotecas gerais que eu desenvolvi ao longo dos meus trabalhos.

## Neste Repositório

### Arduino

* **led_rgb**: Biblioteca para utilização de leds rgb em 3 portas pwm do arduino. Facilitando a seleção de cores. (As cores implementadas podem ser encontradas no arquivo cores_rgb.h)
	* Iniciando: led_rgb my_rgb_led(red_pin, green_pin, blue_pin);
	* Setando Portas: my_rgb_led.led_init();
	* Acendendo: my_rgb_led.acender(LED_COLOR_BLUE);

* **nrf24le01**: Biblioteca para utilização do modulo RF nrf24le01 com protocolos de comunicação implementados pelo Sergio e eu, útil para utilizar com o shiel do nrf24le01, que desenvolvi.

### NRF

* **timer0**: Timer.
* **nRF-SPICommands**: Útil para comunicar com outros módulos, mesmo protocolo da biblioteca para arduino.
* mpu_6050_reg: Resgistradores da unidade inercial MPU6050.
* mpu_calirbation: Biblioteca para calibrar o sensor inercial [Nao testada]
* **dmp**: Biblioteca para configuração e leitura do sensor inercial.

## More

Outras bibliotecas úteis:

* Biblioteca para sensor inercial no arduino: [I2C Dev Lib](https://github.com/jrowberg/i2cdevlib).
* Timers no arduino:[Timer.h](https://github.com/JChristensen/Timer) - [SimpleTimer.h](https://github.com/schinken/SimpleTimer) - [DueTimer](https://github.com/ivanseidel/DueTimer).
* Porta Serial em pinos diferentes (Útil para bluetooth): [SoftwareSerial](https://github.com/PaulStoffregen/SoftwareSerial).
* Barramento I2C em pinos diferentes: [SoftI2CMaster](https://github.com/felias-fogg/SoftI2CMaster).
* RFID Arduino RFID Library for MFRC522: [MFRC522](https://github.com/miguelbalboa/rfid).
* Outras bibliotecas para o nrf: [Creating Applications with the Keil C51 C Compiler](https://www.nordicsemi.com/eng/nordic/download_resource/12804/7/11657752/1515).

Códigos Úteis:

* [MPU6050_calibration](https://github.com/italogfernandes/rastreamento-inercial/blob/master/Codigos%20para%20consulta%20e%20referecias/Firmware/Arduino/MPU6050_calibration/MPU6050_calibration.ino).
* [MPU6050 e EMG reader](https://github.com/BIOLAB-UFU-BRAZIL/cobec-competicao/blob/master/SistemaDeAquisicao/Arduino_EMG_INERTIAL_Com_Fio/Arduino_EMG_INERTIAL_Com_Fio.ino)
* [MPU6050 reader](https://github.com/italogfernandes/rastreamento-inercial/blob/master/Codigos%20para%20consulta%20e%20referecias/Firmware/Andrei-pu6050_complete/mpu6050_complete/mpu6050_complete.ino)
* [I2C Scanner](https://playground.arduino.cc/Main/I2cScanner)
* [HC-06 e HC-05 Bluetooth Setup](https://github.com/italogfernandes/projeto-interdisciplinar/blob/master/setup_bluetooth/setup_bluetooth.ino)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

```
"THE BEERWARE LICENSE" (Revision 42):
Italo Fernandes wrote this code. As long as you retain this
notice, you can do whatever you want with this stuff. If we
meet someday, and you think this stuff is worth it, you can
buy me a beer in return.
```

## Authors

**Italo Fernandes** - https://github.com/italogfernandes - italogsfernandes@gmail.com

See also the list of [contributors](https://github.com/italogfernandes/libraries/contributors) who participated in this project.
