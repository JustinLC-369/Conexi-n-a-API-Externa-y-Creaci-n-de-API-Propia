# Proyecto: API de Perros 🐶

Este proyecto contiene una API desarrollada con FastAPI (Python) para gestionar información de perros y una interfaz web sencilla como frontend.

##Estructura del Proyecto


```text
.
├── Backend
│   ├── app.py
│   ├── crud.py
│   ├── database.py
│   ├── dogs.db
│   ├── models.py
│   ├── schemas.py
│   └── requirements.txt
├── Frontend
│   ├── index.html
│   ├── main.js
│   └── style.css
└── venv/

##Tecnologías usadas

- *Python 3.10+*
- *FastAPI*
- *SQLite (dogs.db)*
- *Uvicorn*
- *JavaScript, HTML, CSS*

##Requisitos previos

- Tener Python 3.10 o superior instalado.
- (Opcional) Tener Git para clonar el repositorio.

##Instalación y ejecución

###1. Clona el repositorio o descarga los archivos

bash
https://github.com/JustinLC-369/Trabajo-Grupal--3.git


###2. Crea y activa el entorno virtual

####En Mac/Linux:
bash
python3 -m venv venv
source venv/bin/activate


####En Windows:
bash
python -m venv venv
venv\Scripts\activate


###3. Instala las dependencias

bash
pip install -r Backend/requirements.txt


###4. Ejecuta el servidor FastAPI

Desde la carpeta raíz del proyecto (donde estás), corre:

bash
cd Backend
uvicorn app:app --reload


Esto levantará la API en:  
📍 http://127.0.0.1:8000  

## Notas adicionales
- El frontend se encuentra en la carpeta Frontend y puedes abrir index.html directamente en el navegador.


## Autor

Justin Lopez
Carlos Sandoval
Andres Torres
Julio 2025
