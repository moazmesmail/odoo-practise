from odoo import models,fields

class Estate(models.Model):
    _name = "estate"

    name=fields.Char()
    state=fields.Selection([
        ("new","New"),
        ("canceled", "Canceled"),
    ])
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date()
    expected_price=fields.Integer()
    selling_price=fields.Integer()
    bedrooms=fields.Integer()
    living_area=fields.Float()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Float()
    garden_orientation=fields.Selection(
        [
            ("south","South"),
            ("north", "North"),
            ("east", "East"),
            ("west","West"),
        ]
    )



