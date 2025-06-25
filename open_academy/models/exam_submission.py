from odoo import fields , models,api
from datetime import datetime
class ExamSubmission(models.Model):
    _name="openacademy.exam.submission"
    student_id=fields.Many2one('openacademy.student')
    exam_id=fields.Many2one('openacademy.exam')
    # submission time
    submission_time=fields.Datetime()

    # grade instructor gives it to me
    grade=fields.Integer()
    # grader
    grader=fields.Many2one('openacademy.instructor')
    # course_id related field
    course_id=fields.Char(related='exam_id.name')
    _sql_constraints = [
        ('unique_student_exam', 'unique(student_id, exam_id)', "you can't submit exam twice.")
    ]

    @api.model_create_multi
    def create(self,vals):
        for v in vals:
            v['submission_time'] = datetime.now()
        return super().create(vals)