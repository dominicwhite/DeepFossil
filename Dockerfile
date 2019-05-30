FROM python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /home/deepinfer && mkdir /home/deepinfer/data

WORKDIR "/usr/src"

COPY . .

ENTRYPOINT ["python", "./fit.py"]
