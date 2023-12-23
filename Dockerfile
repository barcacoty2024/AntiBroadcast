Sh neofetch --stdout# Use the official Python image
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
ENV BOT_TOKEN=your_bot_token
ENV CHAT_ID=your_chat_id

# Command to run on container start
CMD ["python", "bot.py"]
