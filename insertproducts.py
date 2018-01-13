import xmlrpclib, csv

host = 'http://localhost:8069'
database = 'odoo10db'
username = 'user@test.com'
password = 'test1234'

common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' %host)
user_id = common.authenticate(database, username, password, {})

odoo_api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' %host)

filename = "import_data.csv"

reader = csv.reader(open(filename, 'rb'))

for row in reader:
	product_name = row[0]
	product_calorie = row[1]

	filter_byname = [[('name', '=', product_name)]]
	existing_product = odoo_api.execute_kw(database, user_id, password, 'product.template', 'search', filter_byname)
	if existing_product:
		print("Product Exists - ID: %s" %str(existing_product))
	else:
		record = [{'name': product_name, 'calories':product_calorie}]
		odoo_api.execute_kw(database, user_id, password, 'product.template', 'create', record)
		print("Added Product Name: %s and Calories: %s" %(product_name, product_calorie))

