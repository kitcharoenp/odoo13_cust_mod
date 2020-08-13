# -*- coding: utf-8 -*-

{
    'name': 'xFleet Fuel Log',
    'version': '1.0',
    'license': 'AGPL-3',
    'category': 'Fleet',
    'description': """ """,
    'depends': ['fleet'],
    'summary': 'Inherit fleet fuel log',
    'data': [
        # View
        'views/x_fleet_fuel_log_form_view.xml',
        'security/x_fleet_fuel_log_security.xml',
    ],
    'installable': True,
    'auto-install': False,
}
