# -*- coding: utf-8 -*-

from odoo import api, fields, models


class FleetVehicleCost(models.Model):
    _inherit = 'fleet.vehicle.cost'

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

    # Override: _set_odometer()
    def _set_odometer(self):
        for record in self:
            if not record.odometer:
                raise UserError(_('Emptying the odometer value of a vehicle is not allowed.'))
            # disable create odometer log
            '''
            odometer = self.env['fleet.vehicle.odometer'].create({
                'value': record.odometer,
                'date': record.date or fields.Date.context_today(record),
                'vehicle_id': record.vehicle_id.id
            })
            '''
            self.odometer_id = odometer
