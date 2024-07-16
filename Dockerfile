FROM python:3.12-slim

ENV HOME=/app
WORKDIR $HOME
ENV PYTHONPATH=$HOME

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.lock ./
RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir -r requirements.lock

COPY src .
CMD ["uvicorn", "py_clean_architecture.main:app", "--host", "0.0.0.0"]
