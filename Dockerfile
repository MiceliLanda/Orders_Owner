FROM python:3.8.13-slim

WORKDIR /myapp
RUN apt update -y
RUN apt install git bash -y
RUN git clone https://github.com/MiceliLanda/Orders_Owner.git
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r Orders_Owner/requirements.txt

CMD ["python", "MicroserviceUfood/app.py"]