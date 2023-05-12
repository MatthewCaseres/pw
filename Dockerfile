# Use the Playwright-ready Python base image
FROM mcr.microsoft.com/playwright/python:v1.33.0-jammy

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the requirements
RUN pip install -r requirements.txt

# Copy the rest of the code into the container
COPY . .

# Expose the port Streamlit will run on
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
