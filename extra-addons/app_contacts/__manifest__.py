{
    'name': 'Contacts Extension',
    'category': 'Sales/CRM',
    'version': '1.0',
    'summary': 'Adds extra features to Contacts',
     'sequence': 10,
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
