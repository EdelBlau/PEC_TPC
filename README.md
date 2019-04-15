## Descripción

En esta práctica de la asignatura Tipología y Ciclo de Vida de los Datos, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya, se elabora un caso práctico orientado a aprender a identificar los datos relevantes para un proyecto analítico y usar las herramientas de extracción de datos. Dicho caso, aplica técnicas de _web scraping_ mediante el lenguaje de programación Python para extraer datos de los portales inmobiliarios **Fotocasa.es** y **Pisos.com** y generar un dataset con pisos puestos a la venta. Actualmente se extraen datos de Madrid y Barcelona.

Para ejecutar los spiders, en primer lugar debe crearse un virtual enviroment de Python y activarlo. Después, se instala Scrapy mediante pip
```
pip install scrapy
```

o bien 

```
 pip install -r requirements.txt 
```

Los spiders se ejecutan desde la raíz del proyecto de la siguiente forma

```
scrapy crawl nombre-spider -t csv -o nombre-fichero.csv --loglevel=INFO -a ciudad=nombre-ciudad
```
Siendo **nombre-spider** fotocasa o pisos, dependiendo de la web de la cual quieran extraerse los datos, y **nombre-fichero** el nombre del fichero csv que contendrá los datos extraídos. También será posible indicar la ciudad de la cual se quieren extraer los inmuebles, mediante el argumento **nombre-ciudad**. Este atributo deberá ir en minúsculas y los espacios con giones. Se recomienda comprobar que la ciudad exista en la web a parsear antes de indicarlo. Se extraerán las 20 primeras páginas de los pisos más recientes en Madrid y Barcelona para el dataset a entregar. En estos casos, el valor de **nombre-ciudad** sera "madrid" y "barcelona" respectivamente. 


## Miembros del equipo

La práctica ha sido realizada de manera conjunta por: 

* Irene Fernández Molina
* Héctor Hernández Membiela

## Ficheros de código fuente

* fotocasa/spiders/\_\_init\_\_.py --> por defecto
* fotocasa/spiders/fotocasa.py --> spider para wen Fotocasa.es
* fotocasa/spiders/pisos.py --> spider para web Pisos.com
* fotocasa/\_\_init\_\_.py --> por defecto
* fotocasa/items.py --> modelo del objeto InmuebleItem
* fotocasa/middlewares.py --> por defecto
* fotocasa/pipelines.py --> por defecto
* fotocasa/settings.py --> indicacion de user-agent

## Recursos

* Subirats, L., Calvo, M. (2019). Web Scraping. Editorial UOC.
* Masip, D. (2010). El lenguaje Python. Editorial UOC
* Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
* Simon Munzert, Christian Rubba, Peter Meißner, Dominic Nyhuis. (2015). Automated Data Collection with R: A Practical Guide to Web Scraping and Text Mining. John Wiley & Sons.
* Tutorial de Github https://guides.github.com/activities/hello-world.
