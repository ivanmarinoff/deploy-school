FROM python:3.8.12-slim
ENV APP_HOME=/app
WORKDIR $APP_HOME
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /app/
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY . .
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]