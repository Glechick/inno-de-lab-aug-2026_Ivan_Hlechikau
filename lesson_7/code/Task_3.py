# Конфигурационный словарь, полученный от сервиса инициализации
db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}
# Ваш код здесь

# Посмотрел как получить вложенное значение, удобно записать в переменную и не прописывать get каждый раз
connection = db_config.get('connection', {})
host = connection.get('host', 'defoult_host')
port = connection.get('port', 'defoult_port')

# Проверка вложенного ключа который "Есть"
ssl_mode = connection.get('ssl_settings', {}).get('ssl_mode', 'verify-full')

print(f'SSL Mode: {ssl_mode}')

connection['user'] = 'admin'

# print(db_config)

connection['max_connections'] = 100

# print(db_config)

print('Параметры соединения:')
for k, v in db_config['connection'].items():
    print(f'* {k}: {v}')
    




