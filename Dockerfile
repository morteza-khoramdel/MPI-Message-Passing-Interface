FROM python:3.9-slim

RUN apt-get update && apt-get install -y build-essential mpich libmpich-dev 

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["mpiexec", "-n", "1", "python3", "master.py"]
