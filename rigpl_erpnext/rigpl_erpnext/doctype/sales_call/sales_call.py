# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt
from frappe.model.document import Document
import json

class PaymentTool(Document):
	def make_communication(self):
		com = frappe.new_doc('Communication')
		com.subject = self.subject
