from django.shortcuts import render
import csv
import os
import requests
import boto3
import zipfile
import io
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

def descargar_imagenes(request):
    fecha = request.GET.get('fecha')
    if not fecha:
        return HttpResponse("Debe proporcionar una fecha en el formato YYYY-MM-DD.", status=400)
    try:
        datetime.strptime(fecha, '%Y-%m-%d')
    except ValueError:
        return HttpResponse("Formato de fecha no válido. Use YYYY-MM-DD.", status=400)

    
    campos_csv = 'image_satelite/campos.csv'

    s3 = boto3.client(
        's3',
        aws_access_key_id='AKIA5FTZFBG4RNI4KYXO',
       
        region_name='us-east-1'
    )
    bucket_name = 'satelite-prueba28'

    # Lista para almacenar los nombres de archivo de las imágenes descargadas
    nombres_archivos = []

    # Leer el archivo CSV y procesar cada campo
    with open(campos_csv, newline='') as csvfile:
        campos_reader = csv.reader(csvfile)
        for row in campos_reader:
            id_del_campo, lat, lon, dim = row

            # Validar los valores de lat y lon
            if not lat or not lon:
                print(f"Coordenadas no válidas para el campo {id_del_campo}.")
                continue

            try:
                lat = float(lat)
                lon = float(lon)
                dim = float(dim) if dim else 0.1  # Dim es opcional, usa un valor por defecto si no se proporciona
            except ValueError:
                print(f"Coordenadas no válidas para el campo {id_del_campo}.")
                continue

            url = f'https://api.nasa.gov/planetary/earth/imagery/?lon={lon}&lat={lat}&date={fecha}&dim={dim}&api_key=${API_KEY}'
            response = requests.get(url)

            # Debugging: Print the response status and URL
            print(f"Request URL: {url}")
            print(f"Response Status: {response.status_code}")

            if response.status_code == 200:
                # Almacenar la imagen en Amazon S3
                image_data = response.content
                file_key = f"{id_del_campo}/{fecha}_imagery.png"
                s3.put_object(Bucket=bucket_name, Key=file_key, Body=image_data)

                # Agregar el nombre de archivo a la lista
                nombres_archivos.append(file_key)
            else:
                print(f"Failed to download image for field {id_del_campo} at {lat}, {lon}. Status: {response.status_code}, Message: {response.text}")

    # Verificar los nombres de archivos descargados
    if not nombres_archivos:
        return HttpResponse("No images were downloaded.", status=500)

    # Crear el archivo ZIP en memoria
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as zip_file:
        # Agregar cada imagen descargada al archivo ZIP
        for nombre_archivo in nombres_archivos:
            try:
                imagen_data = s3.get_object(Bucket=bucket_name, Key=nombre_archivo)
                zip_file.writestr(nombre_archivo, imagen_data['Body'].read())
            except Exception as e:
                print(f"Error adding file {nombre_archivo} to ZIP: {e}")

    # Configurar la respuesta HTTP con el contenido del archivo ZIP
    buffer.seek(0)
    response = HttpResponse(buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename={fecha}_imagenes.zip'
    return response

@csrf_exempt
def obtener_imagenes_zip(request):
    id_del_campo = request.GET.get('id_del_campo')
    imagenes_dir = f'C:\\Users\\natal\\Desktop\\satelite\\imagenes\\imagenes\\{id_del_campo}'  # Directorio donde se almacenan las imágenes

    # Verificar si el directorio de imágenes existe
    if not os.path.exists(imagenes_dir):
        return HttpResponse("ID del campo no válido o no se encontraron imágenes", status=404)

    # Crear un objeto de archivo ZIP en memoria
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as zip_file:
        # Recorrer todas las imágenes en el directorio y agregarlas al archivo ZIP
        for root, dirs, files in os.walk(imagenes_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, imagenes_dir))

    # Configurar la respuesta HTTP con el contenido del archivo ZIP
    buffer.seek(0)
    response = HttpResponse(buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename={id_del_campo}_imagenes.zip'
    return response
