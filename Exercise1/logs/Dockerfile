FROM python:3.9

# Install cron and nano
RUN apt-get update && apt-get install -y cron nano

# Copy the script into the container
COPY countdown_script.py /app/countdown_script.py

# Set the working directory
WORKDIR /app

# Run the script when the container starts
CMD cron && tail -f /var/log/cron.log
