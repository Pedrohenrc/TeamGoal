FROM python:3.12-slim as builder

WORKDIR /usr/src/app

# Copiar requirements
COPY requirements.txt .

# Instalar dependências
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.12-slim

WORKDIR /usr/src/app

# Copiar dependências do builder
COPY --from=builder /root/.local /root/.local

# Copiar código da aplicação
COPY . .

# Configurar PATH
ENV PATH=/root/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=TeamGoal.settings \

# Coletar arquivos estáticos
RUN DJANGO_BUILD=1 python manage.py collectstatic --noinput

EXPOSE 8000

# Comando para iniciar o Gunicorn
CMD ["gunicorn", "TeamGoal.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]