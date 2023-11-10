from odoo import models, fields


class employee(models.Model):
    _inherit = 'hr.employee'
    personal_mail = fields.Char(string="personal mail")