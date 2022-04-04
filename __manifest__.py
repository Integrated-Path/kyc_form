# -*- coding: utf-8 -*-
{
    'name': "KYC FORM",


    'summary': """
        Model for know your customer form  """,


    'author': "Integrated Path",

    'website': "https://www.int-path.com",


    'category': 'Customizations',


    'version': '15.1',
    

    'depends': ["base"],


    'data': [
       'views/KYC.xml',
       'security/ir.model.access.csv',
       'report/kyc_form_temp.xml',
       'report/kyc_report.xml',
    ],


}
