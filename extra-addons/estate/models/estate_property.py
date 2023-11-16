from odoo import fields, models

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date of Availability')
    expected_price = fields.Float(string='Expected Price', digits=(6, 2))
    selling_price = fields.Float(string='Selling Price', digits=(6, 2))
    bedrooms = fields.Integer(string='Number of Bedrooms')
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Number of Facades')
    garage = fields.Boolean(string='Has Garage')
    garden = fields.Boolean(string='Has Garden')
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Char(string='Garden Orientation')
