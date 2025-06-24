from odoo import fields,models

class Course(models.Model):
    _name='openacademy.course'
    name = fields.Char(required=True)
    description = fields.Text()

    # unique name
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Instructor name must be unique')
    ]
