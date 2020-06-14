# -*- coding: utf-8 -*-

{
    'name': 'xFleet Vehicle Odometer',
    'version': '1.0',
    'license': 'AGPL-3',
    'category': 'Fleet, Vehicle',
    'description': """
xFleet Vehicle Odometer :
-------------
    * Added a description field to Odometer log
    * Added a driver field to Odometer log
    * Rule fleet/user see all Vehicle and Odometer
    * Rule user can only modify own records
        """,
    'depends': ['fleet', 'project'],
    'summary': 'xFleet Vehicle Odometer',
    'data': [
	'views/x_vehicle_odometer_filter_view.xml',
        'actions/x_vehicle_odometer_act_window.xml',
        'views/x_vehicle_odometer_form_view.xml',
        'views/x_vehicle_odometer_tree_view.xml',
        'security/x_vehicle_odometer_security.xml',
    ],
    'installable': True,
}
