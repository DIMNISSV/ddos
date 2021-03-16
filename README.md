# ddos


#### EN:
The script performs a **DDOS** attack on the site, with proxy and multithreading.
Parse proxies using the *proxyscan module* (https://github.com/NIKDISSV-Forever/proxyscan)
Requests are sent using the *urllib* library.

### Installation:
#### Installing proxyscan:
```pkg / apt install git```

```git clone https://github.com/NIKDISSV-Forever/proxyscan.git; cd proxyscan; python setup.py install; cd ..; rm -rf proxyscan```

Or:

```git clone https://github.com/NIKDISSV-Forever/proxyscan/ ../usr/lib/python3.8/site-packages/proxyscan```

#### ***There is already proxyscan.py here to avoid version conflicts, so you can skip these steps.***

#### Install DDOS:
```pkg / apt install git```

```git clone https://github.com/DIMNISSV/ddos/```

### Using:
**Run the *ddos.py*** file
**Enter a link** to the site you want to attack,
necessarily with the protocol (http, https). If you enter without a protocol, requests will be sent from http

Then **enter the number of threads** to use,
simply put, they determine the attack speed and depend on the power of your device
If you are not sure how much your device will pull, enter 1000, most likely it will cope. But if at 1000 it starts to slow down, enter less, if not, enter more - this will increase efficiency.

This completes all the functions.


#### RU:
Скрипт выполняет **DDOS** атаку на сайт, с прокси и многопоточностью.
Прокси парситися с помощью модуля *proxyscan* (https://github.com/NIKDISSV-Forever/proxyscan)
Запросы отправляются с помощью библиотеки *urllib*.

### Установка:
#### Установка proxyscan:
```pkg/apt install git```

```git clone https://github.com/NIKDISSV-Forever/proxyscan.git; cd proxyscan; python setup.py install; cd ..; rm -rf proxyscan```

Или:

```git clone https://github.com/NIKDISSV-Forever/proxyscan/ ../usr/lib/python3.8/site-packages/proxyscan```

#### ***Во избежание конфликта версий здесь уже есть proxyscan.py, так что можете эти шаги пропустить.***

#### Установка DDOS:
```pkg/apt install git```

```git clone https://github.com/DIMNISSV/ddos/```

### Использование:
**Запускаете файл *ddos.py***
**Вводите ссылку на сайт** который хотите атаковать, 
обьязательно с протоколом (http, https). Если ввести без протокола запросы будут отправляться с http

После **вводите число используемых потоков**, 
просто говоря они определяют скорость атаки и зависят от мощности вашего устройства
Если вы не уверены сколько ваше устройство потянет, вводите 1000, скорее всего - справится. Но если при 1000 начинает тормазить, введите по меньше, если нет, вводите по больше - это увеличит эффективность.

*На этом все функции закончены.*
