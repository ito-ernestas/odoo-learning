from odoo import models, fields


class PartnerObject(models.Model):
    _name = 'partner.object'
    _description = 'Partner Object'

    name = fields.Char(string='Object Name', required=True)
    object_type = fields.Selection([
        ('object', 'Object'),
        ('warehouse', 'Warehouse')
    ], string='Object Type', default='object', required=True)
    vin_number = fields.Char(string='VIN Number', required=True)
    indicator_required = fields.Boolean(string='Indicator Required')
    indicator = fields.Char(string='Indicator')
    partner_id = fields.Many2one('res.partner', ondelete='cascade')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_objects = fields.One2many('partner.object', 'partner_id', string='Objects')
