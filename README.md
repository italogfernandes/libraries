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
