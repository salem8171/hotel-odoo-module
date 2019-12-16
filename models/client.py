# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Client(models.Model):
    _name = 'hotel.client'
    _rec_name = 'nom_client'

    nom_client = fields.Char()
    prenom_client = fields.Char()
    tel_client = fields.Integer()
    email_client = fields.Char()
    adresse_client = fields.Char()
    date_naissance_client = fields.Date()

    metier_id = fields.Many2one(comodel_name='hotel.metier')
    sejour_ids = fields.One2many(comodel_name='hotel.sejour', inverse_name='client_id')
    num_sejours = fields.Integer(string='Nombre de sejours', compute='comp_sejours')

    def comp_sejours(self):
        self.num_sejours = len(self.sejour_ids)
