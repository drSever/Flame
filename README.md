# Проект «Прогнозирование лесных пожаров с помощью ИИ»

**Авторы:**  
- Агапов Константин (Тимлид) ([AgapovKS](https://github.com/AgapovKS))  
- Фадеичев Даниил ([DaniilFad](https://github.com/DaniilFad))  
- Баландина Маргарита ([SuperMBA](https://github.com/SuperMBA))
- Вячин Александр ([bababasbebebe](https://github.com/bababasbebebe))
- Зинкин Сергей ([zinkin-s](https://github.com/zinkin-s))
- Журавлев Александр ([drSever](https://github.com/drSever))

[Ссылка](https://docs.google.com/presentation/d/1HHL5szrB9goM9Vv4D6bgcSpYSFmz8XFH/edit?usp=drive_link&ouid=113726287654873658125&rtpof=true&sd=true) на презентацию.

## О проекте

Ежегодно лесные пожары приносят громадный ущерб природе и экономике. В частности, человеческий фактор играет ключевую роль в возникновении возгораний — от неосторожного обращения с огнём до неконтролируемых сельскохозяйственных палов. Своевременное обнаружение пожара или предсказание его возникновения — важная задача, способная снизить потери и спасти жизни.

Наш проект направлен на применение искусственного интеллекта для автоматической классификации изображений лесных территорий с целью выявления возможных очагов возгорания. В итоге, интеграция этой модели в системы мониторинга и раннего оповещения может оказать существенную помощь в предотвращении катастрофических последствий.

### Основные задачи проекта

- **Предсказание наличия пожара:** Распознавание очагов возгорания по данным аэроснимков и фотографий.
- **Поддержка принятия решений:** Сокращение времени реакции служб МЧС, лесоохранных органов и волонтёров.
- **Сокращение ущерба:** Снижение экономических и экологических потерь за счёт более раннего обнаружения и быстрого реагирования на пожар.

### Актуальность

- **Экономический аспект:** Миллионы рублей уходят на тушение, восстановление лесов и покрытие ущерба от огня.
- **Экологическая значимость:** Леса — это сложные экосистемы, играющие ключевую роль в хранении углерода, регуляции климата и поддержании биоразнообразия.
- **Защита населения:** Своевременное предупреждение о пожарах снижает риски для жизни и здоровья людей.

## Структура репозитория

- [**flask_server/**](./flask_server/):
  - Веб-сервер на Flask для классификации изображений.
  - Возможность загрузки изображения с интерфейсом «drag-and-drop» или выбором файла.
  - Возврат результата классификации: «пожар» или «нет пожара» с соответствующей вероятностью.
  - В директории `models/` хранится обученная модель `.tflite`.

- [**model_train/**](./model_train/):
  - Содержит скрипты и ноутбук `flame_project.ipynb` для обучения модели.
  - Подробное описание используемого датасета [FLAME](https://ieee-dataport.org/open-access/flame-dataset-aerial-imagery-pile-burn-detection-using-drones-uavs).
  - Шаги предобработки данных, анализ, обучение модели и инференс.
  - Итоговые результаты: сохранённые модели (Keras и TFLite).

- [**theme_analysis/**](./theme_analysis/):
  - Jupyter-ноутбук с анализом проблемы лесных пожаров.
  - Статистика по экономическим потерям, ущербу экосистем, сезонности и распределению пожаров по типам и причинам.
  - Визуализация данных, подтверждающая значимость раннего обнаружения и контроля.

## Технологии и инструменты

- **Языки и фреймворки:**  
  - Python 3.8+  
  - Flask (серверная часть)  
  - TensorFlow/Keras (обучение модели)
  
- **Модель:**  
  - Глубокая сверточная нейронная сеть (CNN).
  - Использование архитектуры Xception (см. ноутбук в `model_train` для деталей).
  - Достигнута точность валидации ~0.98, на тестовой выборке результаты варьируются в зависимости от класса (60-90%).

- **Аналитика и визуализация:**  
  - Jupyter Notebook для прототипирования, анализа данных и экспериментов.
  - Matplotlib, Plotly и другие библиотеки для графического представления информации.

- **Управление проектом:**  
  - GitHub для контроля версий.

## Установка и использование

1. Клонируйте репозиторий `Flame`:
   ```bash
   git clone https://github.com/drSever/Flame.git
   cd Flame/flask_server

2. Установите необходимые библиотеки:
   ```bash
   pip install -r requirements.txt
   
3. Запустите Flask-приложение из папки `flask_server`:
   ```bash
   python app.py

4. Перейдите по адресу `http://127.0.0.1:5000`, загрузите изображение и нажмите «Submit» для выполнения классификации.

## Дальнейшее развитие
- Улучшение точности: Добавление дополнительных данных, аугментации и подбор гиперпараметров.
- Прогнозирование риска пожара: Интеграция с метеоданными (температура, влажность, скорость ветра) для предиктивного анализа.
- Расширение функционала: Визуализация результатов на карте, предоставление рекомендаций по профилактике.
- Интеграция с реальными системами: Подключение к дроновым патрулям, ЛЭП-мониторингу и пожарно-наблюдательным станциям.

## Лицензия

Проект распространяется по лицензии MIT. Подробности в файле `LICENSE`.
   

