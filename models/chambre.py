# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Chambre(models.Model):
    _name = 'hotel.chambre'

    intitule_chambre = fields.Char()
    surface_chambre = fields.Integer()
    prix_sejour_une_nuit = fields.Integer()

    vue_chambre_id = fields.Many2one(comodel_name='hotel.vue_chambre')
    etagechambre_id = fields.Many2one(comodel_name='hotel.etagechambre')
    categorie_id = fields.Many2one(comodel_name='hotel.categorie')
    hotel_id = fields.Many2one(comodel_name='hotel.hotel')
    sejour_ids = fields.One2many(comodel_name='hotel.sejour', inverse_name='chambre_id')
    num_sejours = fields.Integer(string='Nombre de sejours', compute='comp_sejours')

    def comp_sejours(self):
        self.num_sejours = len(self.sejour_ids)
