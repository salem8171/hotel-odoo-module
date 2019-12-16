# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Sejour(models.Model):
    _name = 'hotel.sejour'

    date_debut_sejour = fields.Date()
    date_fin_sejour = fields.Date()

    chambre_id = fields.Many2one(comodel_name='hotel.chambre')
    client_id = fields.Many2one(comodel_name='hotel.client')

    def name_get(self):
        result = []
        for sejour in self:
            name = '[ ' + sejour.client_id.nom_client + ' ' + sejour.client_id.prenom_client + ', ' + sejour.chambre_id.intitule_chambre + ' ]'
            result.append((sejour.id, name))
        return result
