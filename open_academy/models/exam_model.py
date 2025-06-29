from odoo import models, fields

class Exam(models.Model):
    _name='openacademy.exam'

    name=fields.Char(required=True,default="Exam 1")
    date=fields.Datetime()
    course_id=fields.Many2one('openacademy.course')

    state=fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
        ('submitted','Submitted'),
        ('closed','Closed'),
    ])

    # unique name
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Exam name must be unique')
    ]

    def action_draft(self):
        for r in self:
            r.state='draft'
    def action_pending(self):
        for r in self:
            r.state='pending'
    def action_submitted(self):
        for r in self:
            r.state='submitted'
    def action_closed(self):
        for r in self:
            r.state='closed'