# ddos
#### RU:
Скрипт выполняет **DDOS** атаку на сайт, с прокси и многопоточностью.
Прокси парситися с помощью модуля *proxyscan* (https://github.com/NIKDISSV-Forever/proxyscan)
Запросы отправляются с помощью библиотеки *urllib*.

### Установка:
#### Установка proxyscan:
```pkg/apt install git```

```git clone https://github.com/NIKDISSV-Forever/proxyscan.git; cd proxyscan; python setup.py install; cd ..; rm -rf proxyscan```

Или:

```git clone https://github.com/NIKDISSV-Forever/proxyscan/ %AppData%\..\Local\Programs\Python\Lib\site-pakages```

#### ***Во избежание конфликта версий здесь уже есть proxyscan.py, так что можете эти шаги пропустить.***

#### Установка DDOS:
```pkg/apt install git```

```git clone https://github.com/DIMNISSV/ddos/```

### Использование:
**Первый вариант:**
**Запускаете файл *ddos.py***
**Вводите ссылку на сайт** который хотите атаковать, 
обьязательно с протоколом (http, https). Если ввести без протокола запросы будут отправляться с http

После **вводите число используемых потоков**, 
просто говоря они определяют скорость атаки и зависят от мощности вашего устройства
Если вы не уверены сколько ваше устройство потянет, вводите 1000, скорее всего - справится. Но если при 1000 начинает тормазить, введите по меньше, если нет, вводите по больше - это увеличит эффективность.

**Второй вариант:**
**Вводите команду:** ```python ddos.py --url __ --thr __```
Где ```__``` вводите URL, жилательно с протоколом. И кол-во потоков.

*На этом все функции закончены.*
