# -*- coding: utf-8 -*-

from odoo import api, fields, models


class FleetVehicleLogFuel(models.Model):
    _inherit = 'fleet.vehicle.log.fuel'

    x_fuel_type = fields.Selection([
        ('gasoline', 'Gasoline'),
        ('diesel', 'Diesel'),
        ('ngv', 'NGV'),
        ('lpg', 'LPG')],
        string='Fuel Type',
        help='Fuel Used by the vehicle')
    x_payment_type = fields.Selection([
        ('fleet_card', 'Fleet Card'),
        ('cash', 'Cash')],
        string='Payment Type',
        help='Payment Type (Cash or Fleet Card)')
