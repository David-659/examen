from django.shortcuts import render
from .utils import send_email_with_attachment, compress_file_to_zip
import os, time
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')


# Copia de seguridad manual usando la utilidad de envío de correo con adjuntos


def backup(request):
    try:
        # configuración de rutas a comprimir:
        file_to_compress = '/home/manana/Documentos/david/DavidWeb/db.sqlite3'
        zip_archive_name = '/home/manana/Documentos/david/DavidWeb/db.sqlite3.zip'
        compress_file_to_zip(file_to_compress, zip_archive_name)
        print("...")
        time.sleep(2)
        print("Compresión correcta...!")
        print("...")
        
        # envío de correo con .zip adjunto

        subject = "Spa SENA - Backup"
        body = "Copia de Seguridad de la Base de Datos del Proyecto Spa SENA"
        to_emails = ['davidvelasquez659@gmail.com']

        # Ejemplo de un archivo adjunto (podrías leerlo de un archivo real)
        file_path = zip_archive_name
        if os.path.exists(zip_archive_name):
            with open(file_path, 'rb') as f:
                file_content = f.read()
            attachments = [('db.sqlite3.zip', file_content, 'application/zip')]
        else:
            attachments = None

        if send_email_with_attachment(subject, body, to_emails, attachments):
            print("Correo electrónico enviado con éxito.")
            return HttpResponse("Correo electrónico enviado con éxito.")
        else:
            print("Error al enviar el correo electrónico.")
            return HttpResponse("Error al enviar el correo electrónico.")
    except Exception as e:
        print(f"Error: {e}")
