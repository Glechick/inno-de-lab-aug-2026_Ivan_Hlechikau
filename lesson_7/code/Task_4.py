# Список ролей, переданный в запросе на авторизацию (содержит повторы)
requested_roles = ["guest", "developer", "guest", "admin",
"developer", "guest"]

# Набор обязательных ролей для выполнения административных функций
required_admin_roles = {"admin", "security_officer",
"audit_manager"}
# Ваш код здесь

set_requested_roles = set(requested_roles)
print(f'Уникальные запрошенные роли: {set_requested_roles}')

repeated = set_requested_roles & set(required_admin_roles)
print(f'Общие административные роли: {repeated}')

missing = set(required_admin_roles) - set_requested_roles
print(f'Недостающие административные роли: {missing}')

has_security_officer = 'security_officer' in set_requested_roles
print(f'Наличие роли security_officer в запросе: {has_security_officer}')