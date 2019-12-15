# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hotel(models.Model):
    _name = 'hotel.sejour'

    numero_chambre = fields.Integer()
    numero_client = fields.Integer()
    date_debut_sejour = fields.Date()
    date_fin_sejour = fields.Date()

#   value2 = fields.Float(compute="_value_pc", store=True)
#   description = fields.Text()

#   @api.depends('value')
#   def _value_pc(self):
#       self.value2 = float(self.value) / 100
