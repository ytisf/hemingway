# coding=utf-8
import re
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

import includes.when_things_go_south


class MailModule():
	def __init__(self, server, port, auth, username, password):
		"""
		Tיhis is the main module that is responsible for all the email handeling
		It parses the CSV and goes even to the sending of the email and the attaching
		of the images to the HTML body.
		:param server: The server address, IP or DNS
		:param port: Port for connection
		:param auth: Boolean of using authentication
		:param username: SMTP username
		:param password: SMTP password
		:return: returns nothing
		"""
		class Object(object):
			"""
			General object class to be used later
			"""
			def __init__(self):
				pass

		self._error_handler = includes.when_things_go_south.Error_Handler()       # Error event handler

		# Build mail server options
		self._mailserver = Object()
		self._mailserver_server = server
		self._mailserver_port = port
		if auth == 1:
			self._mailserver_username = username
			self._mailserver_password = password
			self._mailserver_auth = auth
		self._folder = "sample_conf/"
		self._i = 0                     # counter for retrying
		self._j = 2                     # how many times to try

	def parse_csv(self, filename):
		"""
		:param filename: Location of CSV file with emails
		:return: Array of addresses
		"""
		try:
			listi = []
			f = open(filename, 'rb')
			list = csv.reader(f, delimiter=";")
			self._error_handler.log_error(0, "Parsed CSV file successfully")
			for data in list:
				listi.append(data)
			return listi
		except:
			self._error_handler.log_error(3, "Could not read address file. Please verify location entered.")


	def send_email(self, from_email, rcpt_email, subject, html_body, text_body, attachments, counter, total_len):
		"""
		:param from_email: The email to send from
		:param rcpt_email: Email address to send to
		:param subject: Subject of the mail
		:param html_body: HTML Body as string
		:param text_body: Text body as string
		:return:
		"""

		# Checking for retry counter
		if self._i == self._j:
			self._i = 1
			return 0

		# self._error_handler.log_error(0, "Building mail")
		msg = MIMEMultipart('related')
		msg['Subject'] = subject
		msg['From'] = from_email
		msg['To'] = rcpt_email
		msg.preamble = 'This is a multi-part message in MIME format.'

		msgAlternative = MIMEMultipart('alternative')
		msg.attach(msgAlternative)

		msgText = MIMEText(text_body)
		msgAlternative.attach(msgText)

		# Starting to handle images in file:
		html_body = html_body.replace('<img src="', '<img src="cid:')
		html_body = html_body.replace('<image src="', '<img src="cid:')

		msgText = MIMEText(html_body, 'html')
		msgAlternative.attach(msgText)

		matchObj = re.search(r"<img src=\"cid:(.+)\"", html_body)

		if matchObj:
			for image in matchObj.groups():
				fp = open(self._folder + image, 'rb')
				msgImage = MIMEImage(fp.read())
				fp.close()
				name_of_image = image.split('/')
				name_of_image = name_of_image[:1]
				name_of_image = str(name_of_image)
				name_of_image = name_of_image[2:]
				name_of_image = name_of_image[:-2]
				msgImage.add_header('Content-ID', name_of_image,)
				msg.attach(msgImage)
		else:
			pass

		# Done with the Images

		# Start with attachments:
		if attachments:
			for fi in attachments:
				f = file(fi)
				attachment = MIMEText(f.read())
				attachment.add_header('Content-Disposition', 'attachment', filename=fi)
				msg.attach(attachment)
		# End with Attachments


		# Sending email!
		try:
			s = smtplib.SMTP(str(self._mailserver_server))
			self._error_handler.log_error(0, "Connected to SMTP server successfully")
		except smtplib.SMTPConnectError:
			self._error_handler.log_error(3, "Could not connect to mail server: %s" % self._mailserver_server)


		# Will be checking if AUTH data were given and try to authenticate prior to each mail
		if self._mailserver_auth == 1:
			if self._mailserver_username == "":
				s.helo("Hemmingway")
			else:
				try:
					s.helo("Hemmingway")
					s.login(self._mailserver_username, self._mailserver_password)
				except smtplib.SMTPAuthenticationError:
					self._error_handler.log_error(3, "Credentials provided to SMTP server are invalid")
				except:
					self._error_handler.log_error(3, "Unknown authentication error to server")

		try:
			s.sendmail(from_email, rcpt_email, msg.as_string())
			self._error_handler.log_error(0, "[" + str(counter) + "/" + str(total_len-1) + "] Mail sent from " + from_email + " to " + rcpt_email)
		except:
			self._error_handler.log_error(2, "[" + str(counter) + "/" + str(total_len-1) + "] Mail sending failed from " + from_email + " to " + rcpt_email)
		s.quit()
