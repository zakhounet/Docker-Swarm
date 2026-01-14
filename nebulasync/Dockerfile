FROM python:3.10-slim
WORKDIR /app
RUN pip install --no-cache-dir requests
COPY pisync.py .
# Mode unbuffered pour les logs en temps réel dans Docker
CMD ["python", "-u", "pisync.py"]