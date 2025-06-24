from odoo import fields,models

class Instructor(models.Model):
    _name = 'openacademy.instructor'
    name = fields.Char(required=True, default="Moaz")
    bio=fields.Text()
    age = fields.Integer()
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
