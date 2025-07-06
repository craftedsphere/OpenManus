#!/bin/bash

# CraftedAi Services Startup Script
# This script starts the Python HTTP server and ngrok tunnel

# Set the working directory
cd /Users/Apple/Documents/OpenManus/frontend

# Function to log messages
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> /Users/Apple/Documents/OpenManus/logs/craftedai-services.log
}

# Create logs directory if it doesn't exist
mkdir -p /Users/Apple/Documents/OpenManus/logs

# Log startup
log_message "Starting CraftedAi services..."

# Kill any existing processes on port 8000
lsof -ti:8000 | xargs kill -9 2>/dev/null || true

# Start Python HTTP server in background
log_message "Starting Python HTTP server on port 8000..."
python3 -m http.server 8000 > /Users/Apple/Documents/OpenManus/logs/python-server.log 2>&1 &
PYTHON_PID=$!
echo $PYTHON_PID > /Users/Apple/Documents/OpenManus/logs/python-server.pid
log_message "Python server started with PID: $PYTHON_PID"

# Wait a moment for the server to start
sleep 3

# Check if Python server is running
if kill -0 $PYTHON_PID 2>/dev/null; then
    log_message "Python server is running successfully"
else
    log_message "ERROR: Python server failed to start"
    exit 1
fi

# Start ngrok tunnel
log_message "Starting ngrok tunnel..."
ngrok http --domain=craftedai.ngrok.io 8000 > /Users/Apple/Documents/OpenManus/logs/ngrok.log 2>&1 &
NGROK_PID=$!
echo $NGROK_PID > /Users/Apple/Documents/OpenManus/logs/ngrok.pid
log_message "Ngrok started with PID: $NGROK_PID"

# Wait a moment for ngrok to start
sleep 5

# Check if ngrok is running
if kill -0 $NGROK_PID 2>/dev/null; then
    log_message "Ngrok tunnel is running successfully"
    log_message "Services are ready! Access your platform at: https://craftedai.ngrok.io"
else
    log_message "ERROR: Ngrok failed to start"
    exit 1
fi

# Keep the script running and monitor processes
while true; do
    # Check if Python server is still running
    if ! kill -0 $PYTHON_PID 2>/dev/null; then
        log_message "WARNING: Python server stopped unexpectedly"
        # Restart Python server
        python3 -m http.server 8000 > /Users/Apple/Documents/OpenManus/logs/python-server.log 2>&1 &
        PYTHON_PID=$!
        echo $PYTHON_PID > /Users/Apple/Documents/OpenManus/logs/python-server.pid
        log_message "Python server restarted with PID: $PYTHON_PID"
    fi

    # Check if ngrok is still running
    if ! kill -0 $NGROK_PID 2>/dev/null; then
        log_message "WARNING: Ngrok stopped unexpectedly"
        # Restart ngrok
        ngrok http --domain=craftedai.ngrok.io 8000 > /Users/Apple/Documents/OpenManus/logs/ngrok.log 2>&1 &
        NGROK_PID=$!
        echo $NGROK_PID > /Users/Apple/Documents/OpenManus/logs/ngrok.pid
        log_message "Ngrok restarted with PID: $NGROK_PID"
    fi

    # Sleep for 30 seconds before next check
    sleep 30
done
