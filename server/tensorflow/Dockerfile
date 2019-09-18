FROM python:3

RUN apt update && apt install python3-tk  -y && apt install -f
WORKDIR /usr/src/app

COPY pip_packages.list ./
RUN pip install --no-cache-dir -r pip_packages.list
RUN pip uninstall numpy -y && pip install numpy==1.16.0

COPY . .
CMD [ "python", "./main.py" ]