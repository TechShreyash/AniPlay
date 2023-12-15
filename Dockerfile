FROM python:3.12

# Copy the app files to the container
COPY . /app

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip install -U -r requirements.txt

# Run the Python app
CMD ["python", "-m","AniPlay"]
