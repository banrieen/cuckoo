Raspberry pi 智能小车
===================================================

硬件和数字电路
---------------------------------------------------

* Raspberry pi B+, 减速电机/步进电机， TB6612 Driver chip

* Power: DC 5V，2A (18650 battery),Power for the motor driver (provided by the Pi's GPIO pins)
* IO: GPIO pin(High/Low)

* Pin Connection::

    ~~~
    STBY = Pin 13 (GPIO #21)

    Motor A:

    PWMA = Pin 7 (GPIO #4)

    AIN2 = Pin 11 (GPIO #17)

    AIN1 = Pin 12 (GPIO #18)

    Motor B:

    BIN1 = Pin 15 (GPIO #22)

    BIN2 = Pin 16 (GPIO #23)

    PWMB = Pin 18 (GPIO #24)
    ~~~


参考资料
--------------------------------------------------

1. [How to control a DC motor (or motors) using your Raspberry Pi](https://howchoo.com/g/mjg5ytzmnjh/controlling-dc-motors-using-your-raspberry-pi)
2. [I turned a Furby into an Amazon Echo. Introducing: Furlexa](https://howchoo.com/g/otewzwmwnzb/amazon-echo-furby-using-raspberry-pi-furlexa)