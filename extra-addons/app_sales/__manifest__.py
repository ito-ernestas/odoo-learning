{
    'name': 'Sales Extension',
    'category': 'Sales/CRM',
    'version': '1.0',
    'summary': 'Adds extra features to Sales',
     'sequence': 10,
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
