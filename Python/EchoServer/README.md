## Работа Эхо-сервера и клиента
![alt text](https://github.com/bitcoineazy/Study_Practice/blob/main/images/echo_server_1.jpg)

### Контрольные вопросы на «TCP-клиент и эхо-сервер»
1. Чем отличаются клиентские и серверные сокеты?
>*Ответ: их главное отличие в том, что к серверным сокетам могут подключаться несколько клиентов, а клиентские сокеты могут подключаться к своим конкретным серверным сокетам.*
2. Как можно передать через сокеты текстовую информацию?
>*Ответ: превратить в байт код и передать информацию при помощи функций send() или sendto()*
3. Какие операции с сокетами блокируют выполнение программы?
>*Ответ: (на клиенте) получение информации от сервера, (на сервере) получение информации от клиента*
4. Что такое неблокирующие сокеты?
>*Ответ: это сокеты, которые не блокируют програму, ожидая получения или отправки клиентских данных,
а проверяют на наличие этих данных в буфере и сразу возвращают (в случае, если они есть), а если нет, то не прерывает работу программы, а возвращает 0 байт прочитанного кода*
5. В чём преимущества и недостатки использования TCP по сравнению с UDP?
>*Ответ: TCP позволяет обеспечить полную и корректную передачу данных, но уступает UDP в скорости передачи*
6. Какие вызовы, связанные с сокетами, используются только на стороне сервера?
>*Ответ: bind() — привязывает сокет к адресу address (инициализирует IP-адрес и порт),
> accept() — принимает соединение и блокирует приложение в ожидании сообщения от клиента*
7. На каком уровне модели OSI работают сокеты?
>*Ответ: транспортный 4-й уровень*