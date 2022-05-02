# Laboratorio-4-BI

### Integrantes:
- Andres Pinzon
- Santiago Forero
- Juan Jose Rodriguez

# Instrucciones para correr el API
### Recomendaciones:
- Se debe tener instalada una versi{on de Python mayor a 3.6.
- Crear un entorno de desarrollo para la ejecución con el siguiente comando: python -m venv env (Windows), python3 -m venv env (Mac)
- Activar el ambiente anteriormente creado con el siguiente comando: env\Scripts\activate (Windows), source ./env/bin/activate (Mac)

### Pasos:
- 1. Instalar dependencias y librerias necesarias para la correcta ejecuci{on de la aplicación con el siguiente comando: pip install -r requirements.txt (Ambos sistemas operativos)
- 2. Ingresar a la capeta 'api': cd api
- 3. Correr el programa de la aplicación con el siguiente comando: uvicorn --port 5000 --host 127.0.0.1 main:app --reload (Ambos sistemas operativos)
