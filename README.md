# djangoREST

###Задание:
####Необходимо реализовать серверное приложение для работы с БД. 
+ БД реляционная (желательно Postgres)
+ БД представляет собой трекер задач и содержит следующие таблицы:
	-таблица сотрудников (ФИО, должность, ...)
	-таблица задач (наименование, ссылка на родительскую задачу(если есть зависимость), исполнитель, срок, статус, ...)
####Реализовать на Python REST API на основе django со следующими эндпоинтами: 
+ CRUD для сотрудников и задач, для 
+ "Занятые сотрудники": Запрашивает из БД список сотрудников и их задачи, отсортированный по количеству активных задач. 
+ "Важные задачи": Запрашивает из БД задачи не взятые в работу, и от которых зависят другие задачи, взятые в работу. 
	Релизует поиск по сотрудникам, которые могут взять такие задачи (наименее загруженный сотрудник или сотрудник 
	выполняющий родительскую задачу если ему назначенно максимум на 2 задачи больше, чем у наименее загруженного сотрудника).
	Возвращает Список объектов [{Важная задача, Срок, [ФИО сотрудника]}] 

####Также желательно реализовать html-описание данных эндпоинтов



####Установка зависимостей:
- pip install -r Requirements.txt
