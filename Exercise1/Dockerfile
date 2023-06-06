FROM python:3.9

WORKDIR /Exercise1

COPY requirements.txt .
RUN pip install -r requirements.txt

# host container 
ADD src/ .

CMD ["python", "ex1_0_setup.py"]