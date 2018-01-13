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

filter_by_categname = [[('name', '=', "Diet Items")]]
product_categ_id = odoo_api.execute_kw(database, user_id, password, 'product.category', 'search', filter_by_categname)

for row in reader:
	product_name = row[0]
	product_calorie = row[1]

	filter_by_name = [[('name', '=', product_name)]]
	existing_product = odoo_api.execute_kw(database, user_id, password, 'product.template', 'search', filter_by_name)
	if existing_product:
		print("Product Exists! ID: %s" %str(existing_product))
		record = {'calories':product_calorie, 'categ_id':product_categ_id[0]}
		odoo_api.execute_kw(database, user_id, password, 'product.template', 'write', [existing_product, record])
		print("Updating Product Info of ID:%s" %str(existing_product))
	else:
		record = [{'name': product_name, 'calories':product_calorie, 'categ_id':product_categ_id[0]}]
		odoo_api.execute_kw(database, user_id, password, 'product.template', 'create', record)
		print("Added Product Name: %s, Calories: %s, Prod-Category" %(product_name, product_calorie, product_categ_id[0]))

