##############################################################################
#
# Copyright (c) 2005-2006 TINY SPRL. (http://tiny.be) All Rights Reserved.
#
# $Id: hr.py 7208 2007-08-31 13:02:16Z ced $
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

from mx import DateTime
import time
from osv import fields, osv
import tools

class md_hr_address_street(osv.osv):
    _name = "md.hr.address.street"
    _description = "Street"
    _columns = {
                'name' : fields.char("Street", size=80),
                
                }
md_hr_address_street()

class md_hr_address_zip(osv.osv):
    _name = "md.hr.address.zip"
    _description = "Zip"
    _columns = {
                'name' : fields.char("Zip", size=16),
                
                }
    
md_hr_address_zip()

class md_hr_address_town(osv.osv):
    _name = "md.hr.address.town"
    _description = "Town"
    _columns = {
                'name' : fields.char("Town", size=16),
                
                }
    
md_hr_address_town()

class md_hr_address(osv.osv):
     _name = "md.hr.address"
     _description = "Employee Address"
     _columns = {
                 'employee_id' : fields.many2one("hr.employee", "Employee"), 
                 'type': fields.selection([('default','Default'),('invoice','Invoice'),('contact','Contact')],'Address Type'),
                 'name' : fields.char("Name", size=80),
                 'street_id' : fields.many2one("md.hr.address.street", "Street"),
                 'house_nbr' : fields.char("# House No", size=16),
                 'zip_id' : fields.many2one("md.hr.address.zip", "Zip"),
                 'town_id' : fields.many2one("md.hr.address.town", "Town"),
                 'country_id' : fields.many2one("res.country", "Country"),
                  
                            
                 }
md_hr_address()   

class hr_employee(osv.osv):
         
    _name = "hr.employee"
    _description = "Employee"
    _inherit = "hr.employee"
    
    _columns = {
                'code' : fields.char("Personal Number", size=8),
                'firstname' : fields.char("Surname", size=80),
#                'lasname' : fields.char("Name", size=80,required="True"),
                'prefix' : fields.char("Prefix", size=16),
                'birthdate' : fields.date("Date of Birthday"),   
                'nationality_id' : fields.many2one("res.country", "Nationality",select=True), 
                'gender': fields.selection([('male','Male'),('female','Female')],'Gender'), 
                'addres_id' : fields.many2one("md.hr.address", "Address"), 
                'address_number' : fields.char("Number", size=8), 
                'zip_id' : fields.many2one("md.hr.address.zip", "Zip"),
                'town_id' : fields.many2one("md.hr.address.town", "Town"),
                'country_id' : fields.many2one("res.country", "Country"),
                'phone' : fields.char("Phone Number", size=16),
                'mobile' : fields.char("Mobile Phone Number", size=16),
                'email' : fields.char("Email", size=256), 
                'maiden_name' : fields.char("Maiden Name", size=80), 
                'marital_status': fields.selection([('single','Single'),('married','Married')],'Marital Status'),
                'nbr_of_children' : fields.integer("# of children", size=8),
                'partner_firstname' : fields.char("Partner's surname", size=80),
                'partner_lastname' : fields.char("Partner's name", size=80),
                'partner_prefix' : fields.char("Partner's prefix", size=16), 
                'partner_initials' : fields.char("Partner's initials", size=8), 
                'partner_dob' : fields.date("Partner's DOB"),   
                'partner_gender': fields.selection([('male','Male'),('female','Female')],"Partner's gender"), 
                'nin' : fields.char("National Insurance Number", size=26),
                'education' : fields.char("Education", size=80),
                'field_of_education' : fields.char("Field of education", size=80), 
                'travel_allowance' : fields.boolean("Travel Allowande"), 
                'dist_home_work' : fields.integer("Dist. between home and workplace (km)", size=8),
                'amount_travel_allowance' : fields.float("Travel allowance(per year)"),
                'pension' : fields.boolean("Pension"), 
                'pension_waiver' : fields.boolean("Pension waiver"), 
                'waowiaww' : fields.boolean("Disability/unemployment benefit"),
                'waowiaww_dep_id':fields.many2one('hr.department','If yes, which department'),
                'attachment_earings_order' : fields.boolean("Attachment of earings order"),
                'earings_order_beneficier' : fields.char("In name of", size=80,readonly=True),
                'earings_order_amount' : fields.float("Amount"),
                'earings_order_account' : fields.char("Account Number",size=16),
                'spaarloonregeling' : fields.float("Spaarloonregeling"),
                'spaarloonregeling_account' : fields.char("A/C number spaarloonregeling",size=16),
                'levensloopregeling' : fields.float("Levensloopregeling"),
                'levensloopregeling_account' : fields.char("A/C number levensloonregeling",size=16),
                          
                }
    
    def on_change_nbr_of_children(self,cr, uid, ids, nbr_of_children,context=None):   
        if nbr_of_children < 0:
            raise osv.except_osv(
                        'Please Enter Value > 0!!!!','# of children')
            return {'value':{'nbr_of_children':0}}
        return {}
    
    
       
#    def fields_get(self, cr, uid, fields=None,context=None):
#        res = super(hr_employee, self).fields_get(cr, uid, fields, context)
#        print"::Attachment of earings order::",res['attachment_earings_order']
#        print"::In name of::",res['earings_order_beneficier']['readonly']
#        if res['attachment_earings_order']:
#           res['earings_order_beneficier']['readonly'] = False
#           print"::In name of::",res['earings_order_beneficier']['readonly']
##        field_type_obj = self.pool.get('hr.employee')
##        type_ids = field_type_obj.search(cr, uid, [])
##        types = field_type_obj.browse(cr, uid, type_ids)
##        print"::Field's Type::",types
##        for type in types:
##            print"::attachment_earings_order::",type.attachment_earings_order
##            print"::earings_order_beneficier::",type.earings_order_beneficier
##            
##            type.earings_order_beneficier['readonly'] = [('readonly', type.readonly)]
##            print"type.attachment_earings_order :",type.attachment_earings_order
#        return res
  
    def on_change_attachment_earings_order(self,cr, uid, ids, attachment_earings_order,context=None):   
        if attachment_earings_order == True:
               res = super(hr_employee, self).fields_get(cr, uid,context)
               print"::Attachment of earings order::",res['attachment_earings_order']
               print"::In name of::",res['earings_order_beneficier']
               res['earings_order_beneficier']['readonly'] = False
               print"::In name of::",res['earings_order_beneficier']
               return res
        return {}          
                
hr_employee()








  