# Lesson31_API

23.08.2024-03:11

## CURL requests
http://127.0.0.1:5000/pets

curl -X POST http://127.0.0.1:5000/pets \
-H "Content-Type:application/json" \
-d '{"key1": "value1" , "key2": "value2"}'

curl -X POST http://127.0.0.1:5000/pets \
-H "Content-Type:application/json" \
-d '{"id":3, "name":"Rexie","age":1,"image":"https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg"}'

## VScode path
PC:
cd "C:\Users\USER\OneDrive\Computer_Science/001-Code/001-Jhon-Bryce/000-GitHub/Lesson31_API"
Laptop:
cd "C:\Users\sergh\OneDrive\Computer_Science/001-Code/001-Jhon-Bryce/000-GitHub/Lesson31_API"


## GIT
git add . 
git status 
git commit -m " " 
git push

git reset HEAD~1
git push -f origin main

python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
pip install flask
pip install flask-cors 
pip freeze 
deactivate

pip freeze > requirements.txt 
pip install -r requirements.txt

http://127.0.0.1:500
http://127.0.0.1:5500 