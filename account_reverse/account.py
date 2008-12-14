from osv import fields, osv

class account_move(osv.osv):
	_name = 'account.move'
	_inherit = 'account.move'
	# Date has been included in account.move
	#_columns = {
	#	'date': fields.related('line_id', 'date', type='date', string='Date'),
	#}

	def revert_move(self, cr, uid, ids, journal, period, date, reconcile=True, context={}):
		for move in self.browse(cr, uid, ids):
			if not journal:
				journal = move.journal_id.id
			if not period:
				period = move.period_id.id
			original_state = move.state
			self.write(cr, uid, [move.id], {'state':'draft'})
 			copy_id = self.copy(cr, uid, move.id)
			j_obj = self.pool.get('account.journal').browse(cr, uid, journal)
			if j_obj.sequence_id:
				name = self.pool.get('ir.sequence').get(cr, uid, j_obj.sequence_id.code)
			self.write(cr, uid, [copy_id], {'journal_id': journal, 'period_id': period, 'name':name, 'date': date})
			copy_move = self.browse(cr, uid, copy_id)
			for line in copy_move.line_id:
				line.write({'credit': line.debit, 'debit': line.credit})
			if original_state <> 'draft':
				self.post(cr,uid, [move.id, copy_move.id])
			if reconcile:
				reconcile_lines = self.pool.get('account.move.line').search(cr, uid, [('account_id.reconcile','=','True'),('move_id','in',[move.id, copy_id])])
				r_id = self.pool.get('account.move.reconcile').create(cr, uid, {
					'type': 'manual',
					'line_id': map(lambda x: (4,x,False), reconcile_lines),
					'line_partial_ids': map(lambda x: (3,x,False), reconcile_lines)})

account_move()
