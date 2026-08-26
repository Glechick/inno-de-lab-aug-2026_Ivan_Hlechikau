# Список транзакций, полученных от платежного шлюза
raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10",
"SUCCESS:0", "SUCCESS:250", "ERROR:200"]
# Реализация фильтрации в одну строку с помощью List Comprehension
# Ваш код здесь

# Сделано с помощью одного генератора, разделил транзакцию с помощью split и взял второй элемент, так как это цена
filtred_list = [int(t.split(':')[1]) for t in raw_transactions if t.startswith('SUCCESS') and int(t.split(':')[1]) > 0]

print(f'Очищенные транзакции: {filtred_list}')