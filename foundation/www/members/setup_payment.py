import frappe
import foundation

no_cache = 1
def get_context(context):
	if frappe.session.user != 'Guest':
		context.show_sidebar = True
