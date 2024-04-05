<h1>Parser Ozon</h1>

<h2>Настройка</h2>
Перед нами стоит задача разработать парсер, который будет собирать информацию о версиях операционных систем в топ-100 смартфонах с самым высоким рейтингом пользователей в каталоге ozon.ru

Для начала установим фреймворк scrapy 

```
pip install Scrapy
```

Следующим шагом запустим scrapy shell


```
scrapy shell
```
В открывшемся окне введите

```
fetch('https://www.ozon.ru/category/smartfony-15502/?sorting=rating') 
```
ссылку мы берём из браузера предварительно зайдя на Ozon.ru и пройдя по пути  “Электроника" -> "Телефоны и смарт-часы” -> "Смартфоны" с сортировкой “Высокий рейтинг”

после чего мы увидим вот такой код

```
>>> fetch('https://www.ozon.ru/category/smartfony-15502/?sorting=rating') 
2024-04-05 13:57:07 [scrapy.core.engine] INFO: Spider opened
2024-04-05 13:57:08 [urllib3.connectionpool] DEBUG: Starting new HTTPS connection (1): publicsuffix.org:443
2024-04-05 13:57:08 [urllib3.connectionpool] DEBUG: https://publicsuffix.org:443 "GET /list/public_suffix_list.dat HTTP/1.1" 200 85177
2024-04-05 13:57:09 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.ozon.ru/category/smartfony-15502/?sorting=rating> (referer: None)
```

Если мы увидим "(200) GET", это означает что scrapy прошёл по ссылке и мы можем продолжать 

Щёлкнув ЛКМ по сайту и выбрав "Посмотреть код", нам нужно найти где храниться ссылка для перехода на смартфон

Далее в консоли scrapy-shell вводим команду:

```
response.css('a.tile-hover-target'): #так выглядит тег и класс в котором хранятся сыкли на смартфоны
```

Если всё хорошо, то мы увидим большой список с ссылками

Тоже самое нужно проделать с ссылкой на самый первый смартфон, чтобы найти элементы (характеристики смартфона) которые нам требуются, в нашей ситуации это ОС

<h2>Запуск</h2>
Находясь в папке 'spiders', в терменале PyCharm запускаем команду:

```
scrapy crawl ozon -o ozon2.csv
```
После выполнения программы в папке появится файл ozon.csv. Далее необходимо запустить файл open_csv.py для агрегации результатов 

Полученный результат:

![image](https://github.com/bgbisdbg/parser_ozon/assets/136889642/b1312b40-f71f-4284-a197-9fb0210e6ceb)


