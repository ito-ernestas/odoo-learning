from odoo import models, fields


class PartnerObjectMixin(models.AbstractModel):
    _name = 'partner.object.mixin'
    _description = 'Mixin for Partner Object fields'

    name = fields.Char(string='Object Name', required=True)
    object_type = fields.Selection([
        ('object', 'Object'),
        ('warehouse', 'Warehouse')
    ], string='Object Type', default='object', required=True)
    vin_number = fields.Char(string='VIN Number', required=True)
    indicator_required = fields.Boolean(string='Indicator Required')
    indicator = fields.Char(string='Indicator')


class PartnerObject(models.Model, PartnerObjectMixin):
    _name = 'partner.object'
    _description = 'Partner Object'

    partner_id = fields.Many2one('res.partner', ondelete='cascade')

class PartnerObjectWizard(models.TransientModel, PartnerObjectMixin):
    _name = 'partner.object.wizard'
    _description = 'Wizard for creating Partner Objects'

    def action_create_partner_object(self):
        self.ensure_one()
        return self.env['partner.object'].create(self._convert_to_write(self._cache))

class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_objects = fields.One2many('partner.object', 'partner_id', string='Objects')
