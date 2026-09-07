FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir .
ENV Q4RADAR_DB=/data/q4radar.sqlite3 Q4RADAR_CONFIG_DIR=/app/config
VOLUME ["/data"]
EXPOSE 8765
CMD ["q4radar","serve","--host","0.0.0.0","--port","8765"]
