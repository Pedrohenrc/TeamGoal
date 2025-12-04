#!/bin/sh

# 1. Aplica as migrações do banco de dados
echo "Starting migrations..."
python manage.py migrate --no-input

# 2. Cria superusuário automaticamente se não existir
echo "Checking for superuser..."

python manage.py shell << EOF
from django.contrib.auth import get_user_model

User = get_user_model()

username = "Pedro"
email = "pedro@admin.com"
password = "qwe##124"

if not User.objects.filter(username=username).exists():
    print("Creating superuser...")
    User.objects.create_superuser(username, email, password)
else:
    print("Superuser already exists.")
EOF

# 3. Inicia o servidor
echo "Starting server..."
exec gunicorn TeamGoal.wsgi:application --bind 0.0.0.0:\$PORT
