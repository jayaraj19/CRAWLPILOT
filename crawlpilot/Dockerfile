FROM python:3.9-slim

# Install necessary packages including curl and gcc for building
RUN apt-get update && apt-get install -y curl gcc build-essential

# Update pip
RUN pip install --upgrade pip

WORKDIR /app

# Copy requirements file and install dependencies
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 -m load_model
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
