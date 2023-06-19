# Тестовое задание на курс «Python» от ЦФТ

## Запуск Docker Compose

```
docker-compose up -d --build
```


## Настройка MySQL
```
docker exec -it salary_viewer-db-1 bash
mysql -uroot -p
root
create database salary_viewer_db;
use salary_viewer_db;
create table users ( user_id int not null, username varchar(255) not null, password varchar(255) not null, primary key (user_id) );
CREATE TABLE salaries ( user_id int not null, salary int not null, FOREIGN KEY (user_id) REFERENCES users(user_id) );
CREATE TABLE next_increases ( user_id int not null, next_increase date not null, FOREIGN KEY (user_id) REFERENCES users(user_id) );
insert into users values (0, 'Eduard_Antonov', '$2b$12$y7XQFcRKpHe5RhABoorJAOtVo/J00UKzdLMHvvD39.2.oGX3SX/RO');
insert into salaries values (0, 43000);
insert into next_increases values (0, '2023-10-13');
insert into users values (1, 'David_Stepanov', '$2b$12$00ULTrreHqCGt3IzaLd2t.PXQOTjiq2JY3B5539nHq7yznIvrPLJm');
insert into salaries values (1, 57000);
insert into next_increases values (1, '2023-9-10');
```


## Как пользоваться
Используя эти данные, вы можете войти в аккаунты двух сотрудников и увидеть их зарплаты и даты следующих повышений:
```
Логин: Eduard_Antonov
Пароль: 81*1&6Nz
```

```
Логин: David_Stepanov
Пароль: 5$8^3XIg
```