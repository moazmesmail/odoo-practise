from odoo import models,fields,api
from datetime import date

class Student(models.Model):
    _name="openacademy.student"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Student"

    name=fields.Char(required=True , default="Omar",tracking=1)
    birth_date=fields.Date()
    email=fields.Char(default="email@company.com")
    phone=fields.Char()
    age=fields.Integer(compute='calc_age')

    level=fields.Selection([
        ('primary','Primary'),
        ('secondary','Secondary'),
        ('high_school','High school'),
    ],default="primary")
    course_ids=fields.Many2many('openacademy.course')

    exam_ids=fields.One2many('openacademy.exam.submission','student_id')
    #unique name
    _sql_constraints = [
        ('unique_name','unique(name)','Student name must be unique')
    ]

    @api.depends('birth_date')
    def calc_age(self):
        for rec in self:
            if rec.birth_date :
                # print(date.today())
                # print(rec.birth_date)
                # print((date.today() - rec.birth_date).days)
                rec.age=(date.today() - rec.birth_date).days / 365
            else:
                rec.age=0