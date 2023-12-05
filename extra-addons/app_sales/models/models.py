from odoo import models, fields

class WorkOrderType(models.Model):
    _name = 'work.order_type'
    _description = 'Work Order Type'

    name = fields.Char(string='Work Order Type', required=True)
    duration = fields.Float(string='Work Order Duration (min)', required=True)
    priority = fields.Selection([
        ('standard', 'Standard'),
        ('urgent', 'Urgent')
    ], string='Priority', default='standard', required=True)
