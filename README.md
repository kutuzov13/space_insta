# Space Instagram

Скрипт для загрузки фотографий с запусков SpaceX, и фотографий сделанных космическим телескопом Hubble.
С возможностью отправкой фотографий в Instagram! 

### Как установить
Для запуска скрипта Python3 должен быть уже установлен.

Клонируйте репозиторий с GitHub.

```git
git clone https://github.com/kutuzov13/space_insta.git
```

Установите зависимости.

```
pip install -r requirements.txt
```
### Библиотеки
- requests==2.25.1 -> Для запросов к API.
- Pillow~=8.1.2 -> Для обработки изображений с последующей отправкой.
- instabot~=0.117.0 -> Для отправки изображений в Инстаграм.
- python-dotenv~=0.15.0 -> Для работы с переменным окружением.

### Переменные окружения
Логин/Пароль Instagram берется из переменного окружения.
- создайте файл ```.env``` рядом с файлом ```upload_insta.py```.
- запишите Логин/Пароль в файл ```.env```:
  
  ```INSTAGRAM_USERNAME='YOU_LOGIN'```.<br/>
  ```INSTAGRAM_PASSWORD='YOU_PASSWORD'```.<br/>
  
  
### Как запустить проект
Если вы хотите получить фотографии с запусков ракет SpaceX.
```
python fetch_spacex.py <ID-запуска> --download_path <path for download images>
```
По умолчанию изображения скачиваются в папку ```images```.
Если вы хотите получить фотографии со спутника Hubble.
```
python fetch_spacex.py <ID-запуска> --download_path <path for download images>
```
По умолчанию изображения скачиваются в папку ```images```.
Для отправки фотографий в инстаграм .
```
python upload_insta.py -p <path to the photos you want to upload to Instagram>
```
По умолчанчию изображения оправляются в Instagram из папки ```images```. 

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков ***[dvmn.org](https://dvmn.org/modules/)***.
