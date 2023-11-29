{
    'name': 'APP Contacts',
    'category': 'Sales/CRM',
    'sequence': 150,
    'summary': 'Centralize your address book',
    'description': """
This module gives you a quick view of your contacts directory, accessible from your home page.
You can track your vendors, customers and other contacts.
""",
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'license': 'LGPL-3',
    "auto_install": True,
    'installable': True,
    'application': True
}
