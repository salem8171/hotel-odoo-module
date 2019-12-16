# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Sejour(models.Model):
    _name = 'hotel.sejour'
    _rec_name = 'num_sejour'

    num_sejour = fields.Integer()
    date_debut_sejour = fields.Date()
    date_fin_sejour = fields.Date()

    chambre_id = fields.Many2one(comodel_name='hotel.chambre')
    client_id = fields.Many2one(comodel_name='hotel.client')
