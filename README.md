# Study_Practice

Репозиторий для практикумов

[«Файловый менеджер»](https://github.com/bitcoineazy/Study_Practice/tree/main/Python/FileManager) — написание программы, имитирующей работу файлового менеджера операционной системы.

[«TCP-клиент и эхо-сервер»](https://github.com/bitcoineazy/Study_Practice/tree/main/Python/EchoServer) — создание клиент-серверной архитектуры по принципу эхо-сервера.

[«Создание простого многопоточного сервера»](https://github.com/bitcoineazy/Study_Practice/tree/main/Python/ThreadedServer) — реализация сервера с возможностью многопоточной работы с клиентом.

---

## Контрольные вопросы


### Контрольные вопросы на «Основы работы с СКВ в графическом режиме»
1. Опишите своими словами следующие термины:
   * рабочий каталог
   >*Ответ: папка с файлами проекта*
   * репозиторий
   >*Ответ: папка, в которой отслеживаются изменения проекта*
   * коммит
   >*Ответ: сохраниение изменений в репозитории и коментарий к ним*
   * ветка
   >*Ответ: альтернативная реализация проекта*


### Контрольные вопросы на «Работа с Git в терминале»
1. Что такое удалённый репозиторий?
>*Ответ: это репозиторий, находящийся на удалённом сервере,
> и который выполняет все те же функции, что и репозиторий на локальной машине (в терминале),
> но с возможностью удалённого хранения данных*
2. Где нужно ввести команду git?
>*Ответ: в терминал (или в терминал git Bash), а также в графических оболочках git*
3. Для чего нужны ветки в системе контроля веток?
>*Ответ: для ведения альтернотивного развития проекта,
> а также разделения деятельности между разработчиками и их кооперации, 
> тестирования и добавления новых функций*
4. Как возникают конфликты слияния?
>*Ответ: они обычно возникают, когда два разработчика изменяют одни и те же строки в файле проекта или один удаляет файл, который в это время изменяет другой. Конфликт во время слияния может произойти в двух отдельных точках — при запуске и во время процесса слияния.*

В исходном README.md репозитория лабораторной работы некорректно задан вопрос:

![](img.png)

5. Как разрешать конфликты слияния?
>*Ответ: в случае возникновения ошибки слияния git просит решить программиста конфликт, отредактировав файлы вручную, и делает новый коммит*

### Контрольные вопросы на «Работа с удалёнными репозиториями и GitHub»
1. Зачем нужен облачный хостинг репозиториев?
>*Ответ: для безопасности всех изменений проекта и его истории (защита от потери данных в случае повреждения локального носителя), а также
> для удобства (возможность работать над проектом из разных мест и с разных устройств)*
2. Какими свойствами обладает сайт github.com?
>*Ответ: создание и хранение репозиториев пользователя,
> получение и отправка данных из репозитория на локальный компьютер,
> прямая работа с репозиториями (их создание, реализация коммитов, решение конфликтов слияния и проблем, слияние коммитов, создание новых веток и их слияние и многое другое)*
3. Как организовать командную работу над проектом?
>*Ответ: первый способ — это создать для каждого программиста отдельную ветку, после чего объединять их в основной проект,\
> второй способ — это создание веток для отдельного функционала и (в случае успешной реализации данной разработчикам задачи)
> их объединение с веткой основного проекта или отклонение наработок программиста в ветке (в случае потери необходимости в данном функционале)*


---

### Контрольные вопросы на «TCP-клиент и эхо-сервер»
1. Чем отличаются клиентские и серверные сокеты?
>*Ответ: Их главное отличие в том, что к серверным сокетам могут подключаться несколько клиентов, а клиентские сокеты могут подключаться к своим конкретным серверным сокетам.*
2. Как можно передать через сокеты текстовую информацию?
>*Ответ: Превратить в байт код и передать при помощи функции send() или sendto()*
3. Какие операции с сокетами блокируют выполнение программы?
>*Ответ: Это (на клиенте) получение информации от сервера, (на сервере) получение информации от клиента*
4. Что такое неблокирующие сокеты?
>*Ответ: Это сокеты, которые не блокируют програму ожидая получения или отправки клиентских данных,
а проверяют на наличие этих данных в буфере и в случае если есть - сразу возвращают,а если нет, не преывает работу программы а возврашает 0 байт прочитанного кода или исключение*
5. В чем преимущества и недостатки использования TCP по сравнению с UDP?
>*Ответ:TCP позволяет обеспечить полную и корректную передачу данных но уступает UDP в скорости передачи*
6. Какие вызовы, связанные с сокетами используются только на стороне сервера?
>*Ответ: bind()-Привязывает сокет к адресу address (инициализирует IP-адрес и порт),\
> accept()-Принимает соединение и блокирует приложение в ожидании сообщения от клиента*
7. На каком уровне модели OSI работают сокеты?
>*Ответ: Транспортный 4-й уровень*


---

### Контрольные вопросы на «Создание простого многопоточного сервера»
1. Почему однопоточное приложение не может решить задачу одновременного подключения?
>*Ответ: Ввиду того, что однопоточное приложение будет ждать ответа только одного из пользователей, и в процесе ожидания будут игнорироватся сообщения от других пользователя. Приложение просто не в состоянии одновременно обработать несколько пользовательских запросов*
3. Чем поток отличается от процесса?
>*Ответ:Если рассматривать с точки зрения аппаратной части то процесс будет выполняться на каком-то отдельном процессоре, а поток будет выполняться в каком-то отдельном процессе,
>если с точки зрения доступа к весурсам как апаратным так и информационным то процесс это отдельный экземпляр программы выполняемый в отдельном адресном пространстве
> один процесс не может получить доступ к переменным и структурам данных другого,
> поток-же выполняется в процесе и в случае изменения данных в отдельном потоке 
> все измененные данные будут доступны другим потокам*
4. Как создать новый поток?
>*Ответ: Надо выделить определённый участок кода при помощи функции, после чего создать отдельный поток и запустить в нем функцию, библиотека threading (как вариант на Python)*
5. Как выделить участок кода так, чтобы он выполнялся в другом потоке?
>*Ответ:Выделить код как функцию и из выполняемого потока запустить новый для этой функциию \
> пример кода:\
>new_thread = threading.Thread(target=function, name='name_new_thread')*
6. В чем проблема потокобезопасности?
>*Ответ: Проблема в сложности предсказания момента переключения процесса между выполнением разных потоков,
> и ввиду чего может возникнуть проблема с одновременные попытки подключения разных потоков к одному и томеже месту (допустим, к терминалу),
> что может привести к наклажению отного потока на другой, например, первый поток выводит в терминал строчку 'Привет', а второй 'Пак дела?', в случае если произойдет непредвиденое переключение с первого потока на второй и обратно то в терминал будет выведено 'ПрКак дела?вет', в виду чего произойдет потеря данных*
7. Какие методы обеспечения потокобезопасности существуют?
>*Ответ: блокировка потока - блокирует переключение на другие потоки или переключение на конкретный поток до разблокировки, предотвращает подключение потоков к одному и томуже терминалу как в примере*
