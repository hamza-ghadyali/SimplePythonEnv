FROM python:3.12.1-bookworm

WORKDIR /app

COPY requirements.txt .

#RUN apt-get update && apt-get install -y zsh

#SHELL ["/bin/zsh", "-c"]

RUN pip install -r requirements.txt

# Expose port for Jupyter
EXPOSE 8888