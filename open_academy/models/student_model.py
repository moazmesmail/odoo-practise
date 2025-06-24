from odoo import models,fields

class Student(models.Model):
    _name="openacademy.student"

    name=fields.Char(required=True , default="Omar")
    birth_date=fields.Date()
    email=fields.Char(default="email@company.com")
    phone=fields.Char()
    age=fields.Integer()

    level=fields.Selection([
        ('primary','Primary'),
        ('secondary','Secondary'),
        ('high_school','High school'),
    ],default="primary")

    #unique name
    _sql_constraints = [
        ('unique_name','unique(name)','Student name must be unique')
    ]
