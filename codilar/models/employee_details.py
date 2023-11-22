from odoo import models, fields, api


class EmployeeDetails(models.Model):
    _name = 'employee.details'

    name = fields.Char(string="Employee name")
    age = fields.Integer(string="age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    company = fields.Many2one('res.company')
    email = fields.Char(String="Email")
    address = fields.Char(String='Address')
    state = fields.Char(String='State')
    district = fields.Char(String='District')
    description = fields.Text(String='description')

    def action_send_email(self):
        for rec in self:
            rec.env.ref('codilar.email_template_name').send_mail(rec.id, force_send=True)




