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

    # Overide original method
    @api.onchange('liter', 'price_per_liter', 'amount')
    def _onchange_liter_price_amount(self):
        liter = float(self.liter)
        price_per_liter = float(self.price_per_liter)
        amount = float(self.amount)
        if amount > 0 and price_per_liter > 0 and round(amount / price_per_liter, 2) != liter:
            self.liter = round(amount / price_per_liter, 2)
