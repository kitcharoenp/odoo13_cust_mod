# -*- coding: utf-8 -*-

{
    'name': 'xMaintenance',
    'version': '1.0',
    'license': 'AGPL-3',
    'category': 'Manufacturing/Maintenance',
    'description': """
        Linked a Product Template to a Equipment
        """,
    'depends': ['maintenance'],
    'summary': 'Inherit Maintenance',
    'data': [
        # View
        'views/x_equipment_form_view.xml',
    ],
    'installable': True,
    'application': True,
}
