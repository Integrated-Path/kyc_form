
from odoo import models, fields,api

class KYCForm(models.Model):

       _name = "kyc.form"
       _description = "Know Your Customer Form"
       date_form= fields.Datetime(string='Date', index=True, default=fields.Datetime.now)
       customer_bussiness_name= fields.Char(string="Customer Business Name ")
       customer_locations= fields.Char(string="Customer Address (Location)")
       clinet_bussiness_workflow= fields.Char(string="Client business and workflow/process")
       number_of_locations= fields.Char(string="How many locations (HQ, retails,  office, etc…)")
       number_of_employees= fields.Char(string="Number of employees")
       deps_use_odoo = fields.Char(string="Departments that will use Odoo")
       number_of_users = fields.Integer(string="No. of Users")
       list_apps = fields.Html('List the Apps')
       legacy_system =  fields.Char(string="Legacy system (List what the  client currently using eg. Excel,  Pen and Paper, or any other  software)")
       pain_points = fields.Char(string="What are the pain points faced  by customer")
       change_system_reason = fields.Char(string="Why are they considering changing the system? ")
       gap_odoo_fill = fields.Char(string="Which gaps will Odoo fill and  how will it be used by the customer?")
       name = fields.Char(string="Name ")
       email = fields.Char(string="Email ")
       w_app_number = fields.Integer(string="W.App Phone Number")
       rolll_in_company = fields.Char(string="Roll in the Company")
       agreed= fields.Char(string="Agreed upon implementation  phases of this project ")
       implementation_time = fields.Char(string="Implementation Time Plan (How  long will this project take to go  live)")
       payment_terms = fields.Char(string="Payment terms with customer(Not revenue, only percentages)")
       hosting = fields.Char(string="Hosting (SaaS, Paas(SH), or On premise) ")
       stand_out_modules = fields.Char(string="Standard Out of the box modules ")
  






      
