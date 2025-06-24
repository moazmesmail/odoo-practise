from odoo import fields,models

class Instructor(models.Model):
    _name = 'instructor'
    name = fields.Char(required=True, default="Moaz")
    age = fields.Integer(default="30")
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
