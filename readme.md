# Aplicación Web Ingresos-Gastos

- Programa hecho en python con el framework Flask, App Ingresos Gastos, con motor de base de datos sqlite, y javascript para validar HTML

## En su entorno de python ejecutar el comando

```
pip install -r requirements.txt
```
las libreria utilizada flask https://flask.palletsprojects.com/en/2.2.x/

## Renombrar el archivo .config_template a .config y dentro agregar las siguientes lineas
```
ORIGIN_DATA="url de nuestra base de datos"
```

## Renombrar el archivo .env_template a .env y dentro agregar las siguientes lineas
```
FLASK_APP=main.py
FLASK_DEBUG=true
```
## Ejecución con el .env
```
flask run
```
## Comando para ejecutar el servidor:
```
flask --app hello run
```

## Comando para actualizar el servidor con cambios de codigo en tiempo real

```
flask --app hello --debug run
```

## Comando especial para lanzar el servidor en un puerto diferente
- Esto se utiliza en el caso que el puerto 5000 este ocupado

```
flask --app hello run -p 5001
```

## Comando para lanzar en modo debug y con puerto cambiado
```
flask --app hello --debug run -p 5001
```
## consultas basicas sqlite
```
---para mostrar datos---
SELECT id,date,concept,quantity FROM movements
--para insertar datos--
--INSERT INTO movements(date,concept,quantity) VALUES("2023-01-12","almuerzo","-12.5");
--para modificar datos--
--UPDATE movements SET concept="compra del dia",quantity=15.5 WHERE id=9
--para borrar registros
--DELETE FROM movements WHERE id=9
```
```
consulta de ingresos
SELECT sum(quantity) FROM movements WHERE quantity>0
consulta de egresos
SELECT sum(quantity) FROM movements WHERE quantity<0
```