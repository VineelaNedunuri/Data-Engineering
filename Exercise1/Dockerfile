FROM python:3.9


WORKDIR /Exercise1

# host container 
ADD src/  .

ADD requirements.txt .
RUN pip install -r requirements.txt
#scikit-learn 

CMD ["python", "./ex1_0_setup.py"]