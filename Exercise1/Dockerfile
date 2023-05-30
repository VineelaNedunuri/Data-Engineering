FROM python:3.9


WORKDIR /Exercise1

# host container 
#ADD ex1_0_setup.py .
ADD src/ex1_0_setup.py .

RUN pip install matplotlib plotly_express pandas numpy dash sklearn

CMD ["python", "./ex1_0_setup.py"]