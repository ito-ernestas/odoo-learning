# -*- coding: utf-8 -*-
# from odoo import http


# class AppSales(http.Controller):
#     @http.route('/app_sales/app_sales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/app_sales/app_sales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('app_sales.listing', {
#             'root': '/app_sales/app_sales',
#             'objects': http.request.env['app_sales.app_sales'].search([]),
#         })

#     @http.route('/app_sales/app_sales/objects/<model("app_sales.app_sales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('app_sales.object', {
#             'object': obj
#         })

