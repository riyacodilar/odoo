from odoo import models, fields


class EmployeeDepartment(models.Model):
    _name = 'employee.department'

    name = fields.Many2one('employee.details', string='Employee name')
    department = fields.Char(string="Department Name")
    department_centre = fields.Char(string="Department Centre")
    department_no = fields.Integer(string="Department No")
