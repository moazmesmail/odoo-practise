from odoo import fields,models,api
from datetime import date
class Instructor(models.Model):
    _name = 'openacademy.instructor'
    name = fields.Char(required=True, default="Moaz")
    bio=fields.Text()
    age = fields.Integer(compute='calc_age')
    birth_date = fields.Date()
    email = fields.Char(default="email@company.com")
    phone = fields.Char()
    spicalization = fields.Selection([
        ('programming', 'Programming'),
        ('maths', 'Maths'),
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
    ], default="programming")

    # unique name
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Instructor name must be unique')
    ]

    @api.depends('birth_date')
    def calc_age(self):
        for rec in self:
            if rec.birth_date:
                # print(date.today())
                # print(rec.birth_date)
                # print((date.today() - rec.birth_date).days)
                rec.age = (date.today() - rec.birth_date).days / 365
            else:
                rec.age = 0