from odoo import models, fields


class Employee(models.Model):
    _name = 'employee.details'
    name = fields.Char(string="Emp name")
    age = fields.Integer(string ="age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    company = fields.Many2one('res.company')


