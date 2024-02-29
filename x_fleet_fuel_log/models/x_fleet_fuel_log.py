# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError

class FleetVehicleLogFuel(models.Model):
    _name  = 'fleet.vehicle.log.fuel'
    _inherit = ['fleet.vehicle.log.fuel', 'mail.thread', 'mail.activity.mixin']

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
    
    # Overide `odometer` field
    odometer = fields.Float(
        compute="_get_odometer"
        , inverse='_set_odometer'
        , string='Odometer Value'
        , tracking=True
        , help='Odometer measure of the vehicle at the moment of this log')


    def _get_odometer(self):
        self.odometer = 0.0
        for record in self:
            record.odometer = False
            if record.odometer_id:
                record.odometer = record.odometer_id.value

    def _set_odometer(self):
        for record in self:
            if not record.odometer:
                raise UserError(_('Emptying the odometer value of a vehicle is not allowed.'))
            odometer = self.env['fleet.vehicle.odometer'].create({
                'value': record.odometer,
                'date': record.date or fields.Date.context_today(record),
                'vehicle_id': record.vehicle_id.id
            })
            self.odometer_id = odometer

    # Overide original method
    @api.onchange('liter', 'price_per_liter', 'amount')
    def _onchange_liter_price_amount(self):
        liter = float(self.liter)
        price_per_liter = float(self.price_per_liter)
        amount = float(self.amount)
        if amount > 0 and price_per_liter > 0 and round(amount / price_per_liter, 2) != liter:
            self.liter = round(amount / price_per_liter, 2)
