FROM python:3.9

# Crear un entorno virtual
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Instalar dependencias
COPY requirements.txt /opt/venv/
RUN pip install -r /opt/venv/requirements.txt

# Copiar la aplicación Flask
COPY . /app
WORKDIR /app

# Exponer puerto y ejecutar la aplicación
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
