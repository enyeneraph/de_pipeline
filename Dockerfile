FROM apache/airflow:2.9.1
USER root
RUN apt-get update && apt-get install -y  git
USER airflow
COPY requirements.txt /
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt
ENV PYTHONPATH "/opt/airflow/src/:${PYTHONPATH}"