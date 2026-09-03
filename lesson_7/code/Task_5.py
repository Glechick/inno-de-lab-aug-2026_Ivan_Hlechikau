# Поток данных телеметрии от серверов кластера
system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online")
]
# Реализация конвейера агрегации метрик
# Ваш код здесь
servers_data = []

for node_name, cpu_load, ram_usage, status in system_telemetry:
    servers_data.append({
        "node_name": node_name,
        "cpu_load": cpu_load,
        "ram_usage": ram_usage,
        "status": status
    })
# print(servers_data)

filtred_data = [s for s in servers_data if s['status'] == 'online']
# print(filtred_data)

names_online_servers = [s['node_name'] for s in filtred_data]
print(f'Активные узлы в сети: {names_online_servers}')

avg_CPU = sum(s['cpu_load'] for s in filtred_data) / len(filtred_data)
# print(avg_CPU)

max_RAM = max(s['ram_usage'] for s in filtred_data)
# print(max_RAM)

final_data = {
    'active_nodes_count': len(filtred_data),
    'metrics':{
        'average_cpu': round(avg_CPU, 2),
        'max_ram': max_RAM
    }
}
print(f'Итоговый отчёт телеметрии:\n {final_data}')