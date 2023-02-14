python3 -m http.server --directory frontend 8083 & 

cd ./backend;
python3 ./main.py &  

while true; do sleep 1; done