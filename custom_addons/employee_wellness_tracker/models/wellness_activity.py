from odoo import api, fields, models
from odoo.exceptions import ValidationError


class WellnessActivity(models.Model):
    _name = 'wellness.activity'
    _description = 'Wellness Activity'

    name = fields.Char(string='Activity', required=True)
    duration = fields.Integer(string='Duration', required=True, default=0)
    employee = fields.Many2one('hr.employee', string='Employee', required=True)

    @api.constrains('duration')
    def _check_duration(self):
        for record in self:
            if record.duration < 0:
                raise ValidationError("The duration must be greater than 0.")
