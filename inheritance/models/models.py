# -*- coding: utf-8 -*-
from odoo import models, fields, api



class Inhreitence(models.Model):
    _name = 'inhreitance.inhreitence'
    _description = 'inhreitance.inhreitence'

    name = fields.Char()
    value = fields.Integer()






class Inhreitence2(models.Model):
    _name='inheritance.inheritance2'
    _inherit = 'inhreitance.inhreitence'


    value_from_prototype_inheritance =fields.Char()

class Inhreitence1(models.Model):
    _inherit = 'inhreitance.inhreitence'


    value_from_class_inheritance =fields.Char()
