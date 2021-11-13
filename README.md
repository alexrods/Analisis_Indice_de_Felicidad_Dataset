# Analisis Indice de Felicidad Dataset

## Descripción del proyecto

En este proyecto **predice** la calificación de la felicidad del "Reporte Mundia de Felicidad".

Usando las *features*  proporcionadas en el dataset, se utilizó el método **GridSearchCV** de **Scikit-Learn** para evaluar distintos parámetros en los modelos de **Regresión Lineal** de **Suport Vector Regressor (SVR)** y **GradientBoostingRegressor** igualmente de **Scikit-Learn.**

El mejor modelo se importa para alimetar una **API** desarrollada en **Flask** la cual recibe los parámetros a evaluar y ésta regresa la predicción.

----
## Acerca del Dataset

Con datos extraidos del [World Happiness Report](https://worldhappiness.report/) éste modelo busca predecir con métodos de regresión lineal el "*score*" de felicidad de un país dados la siguiente información:

**High**: Se refiere al valor de *score* más alto obtenido historicamente.
**Low**: Se refiere al valor de *score* más bajo obtenido historicamente.
**GDP**: (Gross domestic product) o  producto interno bruto
**Family**: Se refiere a la percepción de que tan fuertes son los lazos familiares.
**LifExp**: Se refiere al promedio de la expectativa de vida.
**Freedom**: Se refiere a la percepción de libertad individual.
**Generosity**: Se refiere a la percepción de generosidad del país.
**Corruption**: Se refiere al nivel de corrupción del país.
**Distopía**: Dado un país hipotético con la gente menos feliz del mundo, esta medición indica que tan alejado está un país, de éste país hipotético.


Fuente: [Reporte Mundial de la Felicidad](https://worldhappiness.report/faq/)

----

## Instrucciones de uso

- Descargar o Clonar repositorio

- Instalar entorno Virtual en la carpeta donde se descargo el repositorio

		python -m venv venv

- Activar entorno vitual
		
		./venv/Scripts/activate # para windows

		source /venv/bin/activate # para linux

- Instalar los paquetes de requirements.txt

		pip install -r requirements.txt

- Ejecutar el script server.py

		python server.py

- Este correra en un servidor local en el puerto 8080
		
		localhost:8080

