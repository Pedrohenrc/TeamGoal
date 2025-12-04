#!/bin/sh

# 1. Aplica as migrações do banco de dados (Cria a tabela django_site, etc.)
echo "Starting migrations..."
python manage.py migrate --no-input

# 2. Coleta arquivos estáticos (Opcional, mas boa prática em Docker)
# Se você estiver servindo estáticos pelo Gunicorn/Whitenoise.
# echo "Collecting static files..."
# python manage.py collectstatic --no-input

# 3. Inicia o servidor (Substituído 'seu_projeto' por 'TeamGoal')
echo "Starting server..."
exec gunicorn TeamGoal.wsgi:application --bind 0.0.0.0:$PORT