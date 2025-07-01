from odoo import fields,models

class EnrollStudentWizard(models.TransientModel):
    _name='openacademy.enroll.student.wizard'

    student_id=fields.Many2one('openacademy.student')
    course_id=fields.Many2many("openacademy.course")

    def action_enroll(self):
        for rec in self:
            student = rec.student_id
            for course in rec.course_id:
                course.write({
                    'student_ids': [(4, student.id)]
                })