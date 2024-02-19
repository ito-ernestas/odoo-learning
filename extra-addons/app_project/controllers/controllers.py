# -*- coding: utf-8 -*-
# from odoo import http


# class AppProject(http.Controller):
#     @http.route('/app_project/app_project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/app_project/app_project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('app_project.listing', {
#             'root': '/app_project/app_project',
#             'objects': http.request.env['app_project.app_project'].search([]),
#         })

#     @http.route('/app_project/app_project/objects/<model("app_project.app_project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('app_project.object', {
#             'object': obj
#         })

