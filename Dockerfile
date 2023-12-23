# Use the official Python image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy only requirements to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Set environment variables
ENV BOT_TOKEN=6551801424:AAEvoJmcTvxbEoVx6_RdfuokyUBrd7qUFS8
ENV CHAT_ID=6588255955

# Command to run on container start
CMD ["python", "bot.py"]
