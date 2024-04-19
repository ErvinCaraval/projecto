# Usa una imagen base de Python
FROM python:3.9-alpine3.17

# Configura variables de entorno para Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo en /cod
WORKDIR /code

# Copia todo el contenido del repositorio al directorio de trabajo del contenedor
COPY . /code/

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt /code/

# Instala las dependencias del proyecto especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8000 para que pueda ser accesible desde fuera del contenedor
EXPOSE 8000

# Define el comando para arrancar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
