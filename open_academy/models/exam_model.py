from odoo import models, fields

class Exam(models.Model):
    _name='openacademy.exam'

    name=fields.Char(required=True,default="Exam 1")
    date=fields.Datetime()
    course_id=fields.Many2one('openacademy.course')
    # unique name
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Exam name must be unique')
    ]
