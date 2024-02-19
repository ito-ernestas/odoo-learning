from odoo import models, fields

class CustomProjectTask(models.Model):
    _inherit = 'project.task'

    unit_of_measure = fields.Selection(
        selection='_get_units_of_measure',
        string='Unit of Measure'
    )
    
    quantity = fields.Float(string='Quantity')

    completed_quantity = fields.Float(string='Completed Quantity (Percentage)')

    def _get_units_of_measure(self):
        # Here, you can fetch and return the standard Odoo UoM, 
        # and add any custom ones required by the client  
        pass
