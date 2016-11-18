#Imports
#import requests
#from app import app
#from flask import render_template
#from flask import request
from qpylib import qpylib

#import json


class WhoisInformation(object):
	"""
	Object model for information returned through the whois api
	"""
	def __init__(self):
		self.network = None
		self.organisation = None
		self.contact = None


class WhoisNetwork(object):
	"""
	Object model representing a network
	"""
	def __init__(self):
		self.registration_date = None
		self.handle = None
		self.net_type = None
		self.last_updated = None
		self.parent = None


class WhoisOrganisation(object):
	"""
	Object model representing an organisation
	"""
	def __init__(self):
		self.name = None
		self.handle = None
		self.street = None
		self.city = None
		self.state = None
		self.postal_code = None
		self.country = None
		self.last_updated = None
		self.start_address = None
		self.cidr_length = None
		self.cidr = None


class WhoisContact(object):
	"""
	Object model for point of contact information
	"""
	def __init__(self):
		self.name = None
		self.handle = None
		self.company = None
		self.street = None
		self.street2 = None
		self.full_street = None
		self.city = None
		self.state = None
		self.postal_code = None
		self.last_updated = None


def parsePopupInfo(information_json):

	"""
	Top level object to hold all information
	"""
	whois_info = WhoisInformation()

	"""
	Object to hold network information
	"""
	whois_network = WhoisNetwork()
	whois_network.registration_date = information_json['ns4:pft']['net']['registrationDate']['$']
	whois_network.handle = information_json['ns4:pft']['net']['handle']['$']
	whois_network.net_type = information_json['ns4:pft']['net']['netBlocks']['netBlock']['description']['$']
#	whois_network.last_updated = information_json['ns4:pft']['net']['comment']['line']['updateDate']['$']
	whois_network.parent = information_json['ns4:pft']['net']['parentNetRef']['@handle']

	log_msg = 'parsePopupInfo: Adding whois network [%s] to whois information' % str(qpylib.to_json_dict(whois_network))
	qpylib.log(log_msg, level='info')

	whois_info.network = whois_network

	"""
	Object to hold organisation information
	"""

	whois_organisation = WhoisOrganisation()
	whois_organisation.name = information_json['ns4:pft']['net']['orgRef']['@name']
#	whois_organisation.handle = information_json['ns4:pft']['orgRef']['@handle']
#	whois_organisation.street = information_json['ns4:pft']['streetAddress']['line']['0']['$']
	whois_organisation.city = information_json['ns4:pft']['org']['city']['$']
	#organisation['state'] = information_json['ns4:pft']['iso3166-2']['$']
	#organisation['postalCode'] = information_json['ns4:pft']['postalCode']['$']
	#organisation['country'] = information_json['ns4:pft']['pocs']['name']['$']
	#organisation['lastUpdated'] = information_json['ns4:pft']['updateDate']['$']
	whois_organisation.startAddress = information_json['ns4:pft']['net']['netBlocks']['netBlock']['startAddress']['$']
	whois_organisation.cidrLength = information_json['ns4:pft']['net']['netBlocks']['netBlock']['cidrLength']['$']
	whois_organisation.cidr = whois_organisation.startAddress + '/' + whois_organisation.cidrLength
	##organisation['cidr'] = organisation['startAddress'] + '/' + organisation['cidrLength'] #format : x.x.x.x/xx

	log_msg = 'parsePopupInfo: Adding whois organisation [%s] to whois information' % str(qpylib.to_json_dict(whois_organisation))
	qpylib.log(log_msg, level='info')

	whois_info.organisation = whois_organisation

	"""
	Object to hold Point Of Contact Information
	"""
#	whois_contact = WhoisContact()
#	whois_contact.name = information_json['ns4:pft']['poc']['companyName']['$']
	##whois_contact.name = information_json['ns4:pft']['poc']['companyName']['$']
	##whois_contact.handle = information_json['ns4:pft']['poc']['-1']['handle']['$']
	##pointOfContact['name'] = information_json['ns4:pft']['poc']['companyName']['$']
	##pointOfContact['handle']= information_json['ns4:pft']['poc']['-1']['handle']['$']
	##pointOfContact['company'] = pointOfContact['name']
	#pointOfContact['street'] = information_json['ns4:pft']['streetAddress']['line']['0']['$']
	#pointOfContact['street2']= information_json['ns4:pft']['streetAddress']['line']['-1']['$']
	##pointOfContact['fullstreet'] = pointOfContact['street'] + pointOfContact['street2']
	##pointOfContact['city'] =information_json['ns4:pft']['poc']['city']['$']
	#pointOfContact['state'] = information_json['ns4:pft']['iso3166-2']['$']
	#pointOfContact['postalCode'] = information_json['ns4:pft']['postalCode']['$']
	#pointOfContact['lastUpdated'] = information_json['ns4:pft']['poc']['updateDate']['$']

#	log_msg = 'parsePopupInfo: Adding whois contact [%s] to whois information' % str(qpylib.to_json_dict(whois_contact))
#	qpylib.log(log_msg, level='info')

#	whois_info.contact = whois_contact

	log_msg = 'parsePopupInfo: Returning whois information [%s].' % str(qpylib.to_json_dict(whois_info))
	qpylib.log(log_msg, level='info')

	return whois_info
