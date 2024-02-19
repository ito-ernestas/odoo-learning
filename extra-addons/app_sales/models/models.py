from odoo import models, fields, api
from odoo.exceptions import ValidationError


class WorkOrderType(models.Model):
    _name = 'work_order_type'
    _description = 'Work Order Type'

    name = fields.Char(string='Work Order Type', required=True)
    duration = fields.Float(string='Work Order Duration (min)', required=True)
    priority = fields.Selection([
        ('standard', 'Standard'),
        ('urgent', 'Urgent')
    ], string='Priority', default='standard', required=True)

    active = fields.Boolean(string='Active', default=True)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_object_id = fields.Many2one(
        'partner.object', 
        string='Object', 
        # domain="[('partner_id', '=', partner_id)]",  # Dynamic domain based on partner_id
        required=False
    )

    work_order_type_id = fields.Many2one(
        'work_order_type', string='Work Order Type', required=False
    )

    @api.constrains('state')
    def check_work_order_type(self):
        for record in self:
            if record.state == 'sale' and not record.work_order_type_id:
                raise ValidationError("Work Order Type is required to confirm the order.")
