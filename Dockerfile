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
    DJANGO_SETTINGS_MODULE=TeamGoal.settings

ARG SECRET_KEY
ENV SECRET_KEY=${SECRET_KEY}

# Coletar arquivos estáticos
RUN DJANGO_BUILD=1 python manage.py collectstatic --noinput

# Adiciona o script de inicialização e garante que ele seja executável
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 8000

# Comando para iniciar o Gunicorn
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]