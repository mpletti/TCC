# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o script Python para o diretório de trabalho
COPY . .

# Comando para executar o script
CMD ["python3", "main.py"]

