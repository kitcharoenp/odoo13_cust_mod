# -*- coding: utf-8 -*-

from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    x_driver_id1 = fields.Many2one(
        'hr.employee',
        string='First Driver',
        help='Driver of the vehicle')
    x_driver_id2 = fields.Many2one(
        'hr.employee',
        string='Second Driver')
    x_administrator_id = fields.Many2one(
        'hr.employee',
        string='Administrator')
    x_fleet_card_no = fields.Char(string='Fleet Card No.', copy=False)
    x_fleet_card_password = fields.Char(string='Fleet Card Password', copy=False)
    x_vehicle_gps_id = fields.Char(string='GPS Vehicle ID')

    @api.onchange('x_driver_id1')
    def _onchange_x_driver(self):
        if self.x_driver_id1:
            self.driver_id = self.x_driver_id1.user_id.partner_id
