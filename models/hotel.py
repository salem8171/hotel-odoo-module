# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hotel(models.Model):
    _name = 'hotel.hotel'

    numero_hotel = fields.Integer()
    intitule_hotel = fields.Char()
    nombre_etoile = fields.Integer()
    numero_ville = fields.Integer()

#   value2 = fields.Float(compute="_value_pc", store=True)
#   description = fields.Text()

#   @api.depends('value')
#   def _value_pc(self):
#       self.value2 = float(self.value) / 100
