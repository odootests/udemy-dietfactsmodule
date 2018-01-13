import xmlrpclib, csv

host = 'http://localhost:8069'
database = 'odoo10db'
username = 'user@test.com'
password = 'test1234'

common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' %host)
print common.version()

user_id = common.authenticate(database, username, password, {})
print("User ID: %s" %user_id)

diet_prod_filter = [[('categ_id', '=', 'Diet Items')]]
large_meal_filter = [[('large_meal', '=', 'True')]]

odoo_api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' %host)

product_count = odoo_api.execute_kw(database, user_id, password, 'product.template', 'search_count', [[]])
product_count_v2 = odoo_api.execute_kw(database, user_id, password, 'product.template', 'search_count', diet_prod_filter)
large_meal_count = odoo_api.execute_kw(database, user_id, password, 'res.users.meal', 'search_count', large_meal_filter)
user_count = odoo_api.execute_kw(database, user_id, password, 'res.users', 'search_count', [[]])

print('Products: %s' %product_count)
print('Users: %s' %user_count)
print('Diet Products: %s' %product_count_v2)
print('Large Meals :%s' %large_meal_count)