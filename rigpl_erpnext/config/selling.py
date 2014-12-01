from frappe import _

def get_data():
	return [
		{
			"label": _("Rohit Reports"),
			"icon": "icon-paper-clip",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Customers with SO",
					"doctype": "Campaign",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Follow Up",
					"doctype": "Customer",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Sales Partner SO Analysis",
					"doctype": "Sales Order",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Trial Tracking",
					"doctype": "Sales Order",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Price List",
					"doctype": "Item Price",
				},
			]
		},
		{
			"label": _("Tools"),
			"icon": "icon-wrench",
			"items": [
				{
					"type": "doctype",
					"name": "Sales Call",
					"description":_("Enter your Sales Calls here"),
				}
			]
		}
	]
