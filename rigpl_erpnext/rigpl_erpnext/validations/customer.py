# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import msgprint
import frappe.permissions
import re

def on_update(doc,method):
	#Check customer ID, Allowed Characters are 0~9, A~Z, a~z and SPACE
	#Customer ID should not have Single Characters followed by SPACE
	check_name = doc.name
	if not re.match("^[a-zA-Z0-9 ]*$", check_name):
		frappe.throw("Only a-z, A-Z and 0-9 characters are allowed in ID, \
		rename the Customer to Proceed")

	for m in re.finditer(' ', check_name):
		#frappe.msgprint(("Space Found {0} {1}").format(m.start(), m.end()))
		if m.start() < 2 or (m.end() - m.start()) < 2:
			frappe.throw(("Multiple Spaces and Single Characters not allowed \
			before Spaces. Please rename the customer to Proceed. Check Character \
			Number {0}").format(m.start()))

		
	#Sales Person
	allowed_ids = []
	for d in doc.sales_team:
		if d.sales_person:
			s_person = frappe.get_doc("Sales Person", d.sales_person)
			if s_person.employee:
				emp = frappe.get_doc("Employee", s_person.employee)
				if emp.status == "Active":
					if emp.user_id:
						frappe.permissions.add_user_permission("Customer", doc.name, emp.user_id)
						allowed_ids.extend([emp.user_id])
				else:
					frappe.msgprint("Selected Sales Person is Not an Active Employee", \
					raise_exception=1)
	if doc.default_sales_partner:
		s_partner = frappe.get_doc("Sales Partner", doc.default_sales_partner)
		if s_partner.user:
			user = frappe.get_doc("User", s_partner.user)
			if user.enabled == 1:
				frappe.permissions.add_user_permission("Customer", doc.name, s_partner.user)
				allowed_ids.extend([s_partner.user])
	
	query = """SELECT name, parent from `tabDefaultValue` where defkey = 'Customer' AND defvalue = 
	'%s'""" % (doc.name)
	extra_perm = frappe.db.sql(query, as_list=1)
	if extra_perm <> []:
		for i in range(len(extra_perm)):
			if extra_perm[i][1] in allowed_ids:
				pass
			else:
				frappe.permissions.remove_user_permission("Customer", doc.name, extra_perm[i][1])