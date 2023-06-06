FROM python:3.9

WORKDIR /Exercise1

# Add source files
ADD src/ex1_0_setup.py .

# Add requirements file
ADD requirements.txt .

# Install required packages
RUN pip install -r requirements.txt

# Specify the command to run when the container starts
CMD ["python", "./src/ex1_0_setup.py"]
