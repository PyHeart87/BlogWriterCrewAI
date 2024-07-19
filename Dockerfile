# Use the Python 3.11 slim base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . ./

# Install Python dependencies from requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Install Ollama
RUN apt-get update && apt-get install -y curl && \
    curl https://ollama.ai/install.sh | sh

# Expose the port Streamlit runs on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]