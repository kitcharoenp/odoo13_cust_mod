# -*- coding: utf-8 -*-

from odoo import api, fields, models


class FleetVehicleOdometer(models.Model):
    _inherit = 'fleet.vehicle.odometer'

    def _default_driver(self):
        emp_ids = self.env[
            'hr.employee'].search([('user_id', '=', self.env.uid)])
        return emp_ids and emp_ids[0] or False

    x_description = fields.Text(
        string='Description')
    x_driver_id = fields.Many2one(
        'hr.employee',
        string='Driver',
        default=_default_driver,
        help='Driver of the vehicle')
    y_odometer = fields.Float(
        string='Odometer End',
        group_operator="max")
    x_state_id = fields.Many2one(
        "res.country.state",
        string='State')
    x_project_id = fields.Many2one(
        'project.project',
        string='Project')
    x_datetime_start = fields.Datetime(
        string='Start')
    x_datetime_end = fields.Datetime(
        string='End')
    x_source_location = fields.Char(
        string='Source')
    x_destination_location = fields.Char(
        string='Destination')
    x_distance = fields.Float(
        string='Distance Km')
    # TODO: new fields:  period,  fuel consumption

    @api.onchange('vehicle_id')
    def _onchange_vehicle(self):
        super(FleetVehicleOdometer, self)._onchange_vehicle()
        if self.vehicle_id:
            self.value = self.vehicle_id.odometer
