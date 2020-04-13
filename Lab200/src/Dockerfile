FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/main.py"]

# This code was copied from the kubernets getting started guide, for more please access:
# https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/