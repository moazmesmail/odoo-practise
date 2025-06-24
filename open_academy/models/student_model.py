from odoo import models,fields

class Student(models.Model):
    _name="student"

    name=fields.Char(required=True , default="Omar")
    age=fields.Integer(default="6")
    stage=fields.Selection([
        ('primary','Primary'),
        ('secondary','Secondary'),
        ('high_school','High school'),
    ],default="primary")

    #unique name
    _sql_constraints = [
        ('unique_name','unique(name)','Student name must be unique')
    ]
