--для создания базы и пользователя. Команды выполнять через DBeaver или консоль под именем Postgres

CREATE DATABASE news_db;
CREATE USER app_news WITH PASSWORD '123';
GRANT ALL PRIVILEGES ON DATABASE news_db to app_news;

--подключиться под именем Postgres к news_db
GRANT USAGE ON SCHEMA public TO app_news
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app_news;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO app_news;
GRANT CREATE ON SCHEMA public TO app_news;

--для проверки того, что пользователь создался
SELECT * FROM  pg_catalog.pg_user

/* для удаления пользователя и базы. Исполнять по отдельности, в разных транзакциях.
Подразумевается, что других прав у пользователя нет, иначе придётся вычищать и их тоже */

REASSIGN OWNED BY app_news TO postgres;
COMMIT;
DROP DATABASE news_db;
COMMIT;
DROP USER app_news;
COMMIT;

--Первичное заполнение таблицы rss_sources
INSERT INTO rss_sources
(name, rss, description, is_active)
VALUES
('lenta_ru', 'https://lenta.ru/rss/last24', 'Новости lenta.ru', true),
('rambler', 'https://news.rambler.ru/rss/world/', 'Новости rambler.ru', true),
('rbc', 'http://static.feed.rbc.ru/rbc/logical/footer/news.rss', 'Новости rbc.ru', true),
 ('iXBT', 'https://www.ixbt.com/export/news.rss', 'Новости iXBT', true)