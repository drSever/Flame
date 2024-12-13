# Сервер Flask для классификации изображений.
Сервер позволяет выбирать картинку и выводить результат классификации пожара. 

Для добавления картинки необходимо перетащить файл в область или нажать на область для выбора файла.

Для классификации необходимо нажать на кнопку "Submit". Для удаления картинки необходимо нажать на кнопку "Clear".

# Screenshot:

![image](https://github.com/user-attachments/assets/003f8d31-8f63-4bca-af28-7b109b93c1ce)

# Файлы:
*/models* - расположение обученной модели в формате .tflite.

*/static* и */templates* - фронт сервера. 

*app.py* - основной файл с main. 

# Установка и использование:

### 1. Clone the repo
$ git clone https://github.com/drSever/Flame.git

$ cd Flame/flask_server

### 2. Install Python packages
$ pip install -r requirements.txt

### 3. Run
$ python app.py

### 4. Open http://127.0.0.1:5000


