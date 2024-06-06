# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
# Copia el archivo requirements.txt al directorio de trabajo
# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia todo el contenido de la carpeta imagenes al directorio de trabajo
COPY imagenes/ .

# Copia el archivo manage.py al directorio de trabajo
COPY imagenes/manage.py .

# Copia el archivo campos.csv al directorio de trabajo
COPY imagenes/image_satelite/campos.csv /app/image_satelite/

# Define las variables de entorno necesarias


ENV BUCKET_NAME=<satelite-prueba28>
ENV NASA_API_KEY=<N7NPSvGriaQf6GqQCOCGrcPvmhIwrA9BlXzFmBOK>

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
