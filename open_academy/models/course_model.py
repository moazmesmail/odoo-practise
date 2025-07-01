from odoo import fields,models

class Course(models.Model):
    _name='openacademy.course'
    name = fields.Char(required=True)
    description = fields.Text()
    instructor_id=fields.Many2one('openacademy.instructor')
    student_ids=fields.Many2many('openacademy.student')
    exam_ids=fields.One2many('openacademy.exam','course_id')
    # unique name
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Course name must be unique')
    ]

    def create_exam(self):
        env=self.env
        name=self.name
        id=self.id
        env['openacademy.exam'].create([{
            "name": f"{name} Exam",
            'course_id':id,
        }])