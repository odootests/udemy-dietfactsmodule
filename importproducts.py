import xmlrpclib, csv
server = 'http://localhost:8069'
database = 'odoo10db'
user = 'user@test.com'
password = 'test1234'
common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' %server)
print common.version()
