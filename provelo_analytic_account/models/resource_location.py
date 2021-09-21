# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class ResourceLocation(models.Model):
    _inherit = "resource.location"

    bob_code = fields.Char(string="Bob Code")
    journal_id = fields.Many2one(
        comodel_name="account.journal",
        string="Default Sale Journal",
        required=False,
    )
