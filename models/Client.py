# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hotel(models.Model):
    _name = 'hotel.client'

    numero_client = fields.Integer()
    nom_client = fields.Char()
    prenom_client = fields.Char()
    tel_client = fields.Integer()
    email_client = fields.Char()
    adresse_client = fields.Char()
    date_naissance_client = fields.Date()
    numero_metier=fields.Integer()



