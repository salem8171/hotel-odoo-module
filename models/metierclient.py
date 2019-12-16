# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MetierClient(models.Model):
    _name = 'hotel.metier'
    _rec_name = 'intitule_metier'

    intitule_metier = fields.Char()
    client_ids = fields.One2many(comodel_name='hotel.client', inverse_name='metier_id')
    num_clients = fields.Integer(string='Nombre de clients', compute='comp_clients')

    def comp_clients(self):
        self.num_clients = len(self.client_ids)
