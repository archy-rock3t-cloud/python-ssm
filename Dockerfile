FROM python:3.9

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir --upgrade setuptools

WORKDIR /opt/python_ssm

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY pyproject.toml ./
COPY app/ ./app/
COPY tests/ ./tests/
