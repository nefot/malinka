# Потоковое распознавание речи с микрофона с помощью API v3
Чтобы все заработало необходимо сделать следующие вещи:
1. Создать API-ключ
2. Создать Интерфейс командной строки Yandex Cloud. В операционной системе
3. Назначить роль сервисному аккаунту 
4. Задать API-ключ сервисного аккаунта в виде переменной окружения
5. Выполнить созданный файл `python .\speach_recognition.py --secret AQVNyUzOGjKeZLACdq8b96ibAT1WnAUPcRpx5jbX`
## 1. Создание API-ключа

python output/test.py --token ${IAM_TOKEN} --output speech.wav -text Привет, я работаю хорошо

--no-dependencies

1. [В консоли управления]("https://console.cloud.yandex.ru/folders")
перейдите в каталог, которому принадлежит сервисный аккаунт.
2. В верхней части экрана перейдите на вкладку **Сервисные аккаунты**.
3. Выберите сервисный аккаунт и нажмите на строку с его именем.
4. Нажмите кнопку **Создать новый ключ** на верхней панели.
5. Выберите пункт **Создать API-ключ**.
6. Задайте описание ключа, чтобы потом было проще найти его в консоли управления.
7. Сохраните идентификатор и секретный ключ.

## 2. Интерфейс командной строки Yandex Cloud (CLI) 
### Windows:
Необходимо ввести команду в командной строке

`@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://storage.yandexcloud.net/yandexcloud-yc/install.ps1'))" && SET "PATH=%PATH%;%USERPROFILE%\yandex-cloud\bin"`


### Linux 
`curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash`

### Чтобы аутентифицироваться с помощью аккаунта на Яндексе:
1. Перейдите по [ссылке]("https://oauth.yandex.ru/verification_code#access_token=y0_AgAAAABHGDDBAATuwQAAAADusd1bSZvBsJ9eSH2pDw_6yBERArU45a4&token_type=bearer&expires_in=31081818") Если приложение запрашивает доступ к данным, разрешите. Это нужно для получения токена.
2. Скопируйте в буфер обмена или сохраните полученный токен.
3. выполните команду:`yc init` И следовать инструкции
## Назначить роль сервисному аккаунту
чтобы выполнить этот шаг, необходимо ввести следущую команду в командной строке:

`yc resource-manager <категория_ресурса> add-access-binding <идентификатор ресурса> --role <идентификатор_роли> --subject serviceAccount:<идентификатор_сервисного_аккаунта>`

Где
- *<категория_ресурса>* — cloud, чтобы назначить роль на облако, или folder, чтобы назначить роль на каталог.
- *<идентификатор ресурса>* — имя или идентификатор ресурса, на который назначется роль.
- *<идентификатор_роли>* — например viewer.
- *<идентификатор_сервисного_аккаунта>* — идентификатор сервисного аккаунта, которому назначается роль.

либо 

`yc organization-manager organization add-access-binding <техническое_название_организации>|<идентификатор_организации> --role <идентификатор_роли> --subject serviceAccount:<идентификатор_сервисного_аккаунта>`

Где

- *<техническое_название_организации>* — техническое название организации.
- *<идентификатор_организации>* — идентификатор организации.
- *<идентификатор_роли>* — идентификатор роли, например viewer.
- *<идентификатор_сервисного_аккаунта>* — идентификатор сервисного аккаунта, которому назначается роль.

Их можно получить командой:
`yc organization-manager organization list`
*(список доступных вам организаций, чтобы узнать их идентификаторы и технические названия)*
<pre>
+---------------------------------+---------------------------------+----------------------+
|               ID                |              NAME               |        TITLE         |
+---------------------------------+---------------------------------+----------------------+
| bpf1smsil5q0cmlmb...            | hdt5j5uwsw4w3...                | MyOrg                |
+---------------------------------+---------------------------------+----------------------+
</pre>
Техническое название организации находится в столбце `NAME`, идентификатор организации — в столбце `ID`.

## 4. Задайте API-ключ сервисного аккаунта в виде переменной окружения:
Эти команды нужно выполнить в командной строке 
- `export API_KEY=<API-ключ> `в Linux
- `set API_KEY=<API-ключ>` в Windows

## 5. Выполните созданный файл:

`python .\speach_recognition.py --secret AQVNyUzOGjKeZLACdq8b96ibAT1WnAUPcRpx5jbX`