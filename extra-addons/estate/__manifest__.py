{
    'name': 'Real Estate',
    'version': '1.0',
    'summary': 'Estate Management',
    'sequence': 10,
    'description': 'Manage your real estate properties',
    'category': 'Real Estate',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    'demo': [
        # Demo data files
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
