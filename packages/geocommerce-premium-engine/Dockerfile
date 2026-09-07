FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV GEOCOMMERCE_DB=/data/geocommerce.db
RUN mkdir -p /data
EXPOSE 8080
CMD ["uvicorn","geocommerce.app:app","--host","0.0.0.0","--port","8080"]
