#!/bin/bash 

# Start the backend
cd ./backend && python3 ./api.py & 


# Start the frontend
cd ./frontend && python3 -m http.server 8080
