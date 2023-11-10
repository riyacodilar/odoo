from odoo import models, fields


class Employees(models.Model):
    _name = 'employee.recruitment'

    department = fields.Many2many('employee.department', string='Department Name')
    boolean = fields.Boolean(string='department', default=False)




