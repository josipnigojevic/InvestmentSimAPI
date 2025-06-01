FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      libpq-dev \
      postgresql \
      postgresql-contrib \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/run/postgresql

WORKDIR /app

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN service postgresql start \
    && su - postgres -c "psql -c \"ALTER USER postgres WITH PASSWORD 'postgres';\"" \
    && su - postgres -c "createdb investment_simulator" \
    && service postgresql stop

EXPOSE 5000

ENTRYPOINT [ "bash", "-c", "\
    service postgresql start && \
    flask db upgrade && \
    python app.py" ]
