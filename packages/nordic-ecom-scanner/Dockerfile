FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir .
ENV ECSCAN_DB=/data/scanner.sqlite
VOLUME ["/data"]
EXPOSE 8080
CMD ["uvicorn", "nordic_arbitrage.api:app", "--host", "0.0.0.0", "--port", "8080"]
