#!/bin/bash

# BlueHired Development Server Startup Script
echo "🚀 Starting BlueHired Development Environment..."

# Function to handle cleanup on exit
cleanup() {
    echo "🛑 Shutting down servers..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

# Start Django backend
echo "📡 Starting Django Backend Server..."
cd backend
source venv/bin/activate
python manage.py runserver 8001 &
BACKEND_PID=$!
cd ..

# Wait a moment for backend to start
sleep 3

# Start React frontend (when ready)
echo "⚛️  Starting React Frontend Server..."
cd frontend
npm start &
FRONTEND_PID=$!
cd ..

echo "✅ Both servers are starting up!"
echo "🔗 Backend API: http://localhost:8001"
echo "🌐 Frontend App: http://localhost:3000"
echo "🔧 Admin Panel: http://localhost:8001/admin"
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID
