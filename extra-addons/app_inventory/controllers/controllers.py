# -*- coding: utf-8 -*-
# from odoo import http


# class AppInventory(http.Controller):
#     @http.route('/app_inventory/app_inventory', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/app_inventory/app_inventory/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('app_inventory.listing', {
#             'root': '/app_inventory/app_inventory',
#             'objects': http.request.env['app_inventory.app_inventory'].search([]),
#         })

#     @http.route('/app_inventory/app_inventory/objects/<model("app_inventory.app_inventory"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('app_inventory.object', {
#             'object': obj
#         })

