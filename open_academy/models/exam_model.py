from odoo import models, fields

class Exam(models.Model):
    _name='openacademy.exam'

    name=fields.Char(required=True,default="Exam 1")
    date=fields.Datetime()
    # digits = ('0', '2')
    grade=fields.Float()

    # unique name
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Instructor name must be unique')
    ]
