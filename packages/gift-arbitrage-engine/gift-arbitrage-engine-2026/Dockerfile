FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir .
ENV GIFT_RADAR_ROOT=/app
CMD ["uvicorn","giftradar.api:app","--host","0.0.0.0","--port","8000"]
