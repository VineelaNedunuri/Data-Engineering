FROM python:3.9

WORKDIR /Exercise1

# Add source files
ADD src/ex1_0_setup.py .

# Install required packages
RUN pip install matplotlib plotly_express pandas numpy dash scikit-learn

# Specify the command to run when the container starts
CMD ["python", "./ex1_0_setup.py"]
