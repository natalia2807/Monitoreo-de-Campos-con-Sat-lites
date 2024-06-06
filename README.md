# Proyecto de Descarga de Imágenes Satelitales

Este proyecto permite descargar imágenes satelitales de la Tierra utilizando la API de la NASA y almacenarlas en Amazon S3.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias usando `pip install -r requirements.txt`.
3. librerias que se usar
`asgiref            3.8.1`
`boto3              1.34.118`
`botocore           1.34.118`
`certifi            2024.6.2`
`cffi               1.16.0`
`charset-normalizer 3.3.2`
`cryptography       42.0.7`
`Django             5.0.6`
`idna               3.7`
`Jinja2             3.1.4`
`jmespath           1.0.1`
`MarkupSafe         2.1.5`
`moto               5.0.9`
`pip                24.0`
`pycparser          2.22`
`python-dateutil    2.9.0.post0`
`PyYAML             6.0.1`
`requests           2.32.3`
`responses          0.25.0`
`s3transfer         0.10.1`
`setuptools         65.5.0`
`six                1.16.0`
`sqlparse           0.5.0`
`tzdata             2024.1`
`urllib3            2.2.1`
`Werkzeug           3.0.3`
`xmltodict          0.13.0`

## Uso

1. Configura las variables de entorno en tu entorno de ejecución.
2. Ejecuta el proceso de descarga de imágenes utilizando el comando adecuado.
3. Verifica que las imágenes se hayan descargado correctamente en tu bucket de Amazon S3.

## Configuración

Antes de ejecutar el proceso, asegúrate de configurar las siguientes variables de entorno:

- `FECHA`: fecha=2014-02-04La fecha para la cual deseas descargar las imágenes.
    s3 = boto3.client(
        's3',
        
        
        region_name='us-east-1'
    )
    

## encontrar todos los campos primeramente con docker
docker build -t tierra .

## poner a correr el docker
docker run -p 8000:8000 tierra

## enlace con el cual descargo las imagenes cuando se pone a correr el programa 
http://127.0.0.1:8000/descargar_imagenes/?fecha=2014-02-04

## docker 
docker run -p 8000:8000 tierra

## Contribuciones

¡Contribuciones son bienvenidas! Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega una nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

