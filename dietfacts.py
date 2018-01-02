from odoo import models, fields, api

class Dietfacts_product_template(models.Model):
	_name='product.template'
	_inherit='product.template'
	calories = fields.Integer("Calories")
	serving_size = fields.Float("Serving Size")
	last_updated = fields.Date("Last Updated")
	# diet_item = fields.Boolean("Diet Item")
	nutrient_ids = fields.One2many('product.template.nutrient', 'product_id', 'Product Nutrients')

class Dietfacts_drink_template(models.Model):
	_name='product.template'
	_inherit='product.template'
	key_ingredient = fields.Char("Key Ingredient")

class Dietfacts_res_users_meal(models.Model):
	_name='res.users.meal'
	name=fields.Char('Meal Name')
	meal_date = fields.Datetime("Meal Date")
	item_ids = fields.One2many('res.users.mealitem', 'meal_id')
	total_calories = fields.Integer(string='Meal Total-Calories', store=True, compute='_sumcalories')
	user_id = fields.Many2one('res.users', 'Meal Eater')
	notes = fields.Char("Meal Notes")

	@api.one
	@api.depends('item_ids', 'item_ids.servings')
	def _sumcalories(self):
		sum_calories = 0
		for meal_item in self.item_ids:
			sum_calories += (meal_item.item_calories*meal_item.servings)
		self.total_calories = sum_calories

class Dietfacts_res_users_mealitem(models.Model):
	_name='res.users.mealitem'
	meal_id = fields.Many2one('res.users.meal', 'Meal')
	item_id = fields.Many2one('product.template', 'DietProduct')
	item_calories = fields.Integer(related='item_id.calories', string='MealItem Calorie', store='True', readonly='True')
	servings = fields.Float('Servings')
	notes=  fields.Text("Meal Item Notes")

class Dietfacts_product_nutrients(models.Model):
	_name='product.nutrient'
	name = fields.Char("Nutrient Name")
	uom_id = fields.Many2one('product.uom', 'Unit of Measure')
	description = fields.Text("Description")
	def __str__(self):
		return self.name

class Dietfacts_product_single_nutrient(models.Model):
	_name='product.template.nutrient'
	nutrient_id = fields.Many2one('product.nutrient', string="Product Nutrient")
	product_id = fields.Many2one('product.template')
	nutrient_value = fields.Float("Nutrient Value")
	daily_percent = fields.Float("Daily Percentage")

