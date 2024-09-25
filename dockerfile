# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any dependencies in the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app will run on (adjust based on the framework)
# Streamlit typically runs on port 8501, Flask runs on 5000
EXPOSE 8501

# For Flask app (if needed, replace the command above):
CMD ["python", "app.py"]