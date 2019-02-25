# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)




class CrmTeam(models.Model):
    _inherit = 'crm.team'

    def get_currency(self):
        return self.env.user.company_id.currency_id.id

    team_target = fields.Float(string='Team Target', compute="compute_team_target")
    parent_team = fields.Many2one('crm.team', string='Parent Team', copy=False)
    currency_id = fields.Many2one('res.currency', string='Currency', readonly=True, default=lambda self: self.get_currency())

    @api.multi
    def compute_team_target(self):
        """ Totalize each amount assigned to each vendor belonging to a team """
        total = 0
        childs_team = self.env['crm.target'].search([('sales_team', '=', self.id)])
        _logger.info("""\n\n\n childs_team : %s \n\n\n"""%(childs_team))
        if childs_team:
            for amount in childs_team:
                total += amount.target_amount
            _logger.info("""\n\n\n total : %s \n\n\n"""%(total))
            self.team_target = total


