# Use the official Python image as a base
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your server will run on
EXPOSE 5000

# Run the server
CMD ["python", "-m", "run"]
