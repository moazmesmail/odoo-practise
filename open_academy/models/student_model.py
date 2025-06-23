from odoo import models,fields

class student(models.Model):
    _name="student"

    name=fields.Char(required=1 , defualt="New Student")
    age=fields.Integer(defualt=12)
    stage=fields.Selection([
        ('primary','Primary'),
        ('secondary','Secondary'),
        ('high_school','High school'),
    ])
