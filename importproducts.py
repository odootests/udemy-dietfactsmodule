import xmlrpclib, csv

host = 'http://localhost:8069'
database = 'odoo10db'
username = 'test@user.com'
password = 'test1234'

common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' %host)
print common.version()

user_id = common.authenticate(database, username, password, {})
print("User ID: %s" %user_id)

odoo_api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' %host)
product_count = odoo_api.execute_kw(database, user_id, password, 'product.template', 'search_count', [[]])
user_count = odoo_api.execute_kw(database, user_id, password, 'res.users', 'search_count', [[]])

print('Products: %s' %product_count)
print('Users: %s' %user_count)
