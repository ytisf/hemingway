#!/usr/bin/python

import sys
import getopt
import threading
import ConfigParser

import includes.email_modules
import includes.when_things_go_south

__author__ = "Yuval tisf Nativ"
__license__ = "GPLv3"
__app_name__ = "Hemingway"
__version__ = 1.0

def print_me():
	print("\n\n............................~NN.....................................................................")
	print("..............................8MD...................................................................")
	print("................................NND:................................................................")
	print(".................................NOO8...............................................................")
	print(".................................,D7Z8..............................................................")
	print("..................................NDI$8$............................................................")
	print("...................................NZ7OO.,..........................................................")
	print("...................................ND$$$8,..........................................................")
	print("...................................DDNZ8ZN..........................................................")
	print("..................................IMMNDODN..........................................................")
	print("..................................MNMMND8N:.........................................................")
	print("..............................,,$MMMMMMNNNN.........................................................")
	print("............................7NMMMMMMMMMMMMN.........................................................")
	print("...................,.OMMND8888OOOOZO8NNMMMM,........................................................")
	print("................MNMN88ZZ$$$$$$OOOOO8888888DMN.......................................................")
	print("...........,IMMNDOZ$$$$$$$ZOOOOOZZZZOZZZO8ZZZON?....................................................")
	print("..........DND8OOOZZZZZZZZZZZZZZOOZZZ$$$$$$$OOZ$ZN...................................................")
	print("........MD8OOMMM?????IIIIIIII?????$$OZ8ZOOOZZ8DZOZ8 ................................................")
	print("......N8O$77III+NDNM=~::~:~~~~=+IIZ$,7:.$OZ$I+DDNOZ8,...............................................")
	print("....$O8$7I?=~:::~=NDZ8ON~~===~~===+$:,,$.......IODMO7IDO............................................")
	print("...N8$$?~:::=???????$Z$ZZZDO??+==~I$:~I......,=,.I$D8NOZ$7$8DN$+....................................")
	print("..MO7I~::?II??+=~~~=~~O8D888DN=???O,~:,.....,+..O8ND,..INMND88OOOZZ$7777I$ZOOODNDZ?:.....,..... ....")
	print(".:O7?:~I?+=+?I7$$$Z$$7I7N8DD88DMZ?7:~~+.....:~:..,,,.,,~~~MMMMNDN~.......,:+I$NNNNDDDDD8OOOOOOOOOOO8")
	print(".N7=:I?=I$$ZZ$?=:~~~=+?II7NN8D8DN$7=~~?+,..,:=7:~?I~:DMMMMM7? ......................................")
	print("N$=:?+$Z7,,::,,,,,,,,,,,,,:ND++??$$Z+::?++==?III+NMMMMMM=M..........................................")
	print("87:+$$.:~+??~:,,..........====+,,,:,=O~I$I7ZO8DDD=.,:8NM,...........................................")
	print("$,+7:~II::,~=?I7$I??++++=?+++:,,,....,D$ZZOZZZ8N~? ~~::,.,=D........................................")
	print("7?7:7I+:=IZ=.,.......... ...+ND?+?++==M$:~I+O8I~7O$87II??++=,+M.....................................")
	print(":7~I?=O=?7I,.=.....................,MMNNN$=:+:?8~~Z?..,::,....MZ~...................................")
	print("I7?=:N~+?$I..7.....................,NN8N............................................................")
	print("$7=:OO:??$I..7......................8N8D............................................................")
	print("OI:8D?=??$7,.:.......................NO8............................................................")
	print(".?MN8I=??7$..,.......................DOD............................................................")
	print(".DDD~7~+??$:.,O......................ON.............................................................")
	print("..NZ:I==??$Z..I..... ...............O8..............................................................")
	print(".NN+:?I=I?$$:.,MND8,...............,$...............................................................")
	print("IM..+~7+=??$$,,:MNI.................................................................................")
	print("MM,.7?=7==II$7.=NND.................................................................................")
	print("NN....?+I=?II$7.?8I...........................:ONNNNMNNN............................................")
	print("~N....,Z?I=~II7Z:O8Z....................NZ7OOO88NNMNO...............................................")
	print(".N....?MMZ==~+II$DZZO..............777III$ZZZZD.....................................................")
	print("..,...NDNMM7~:=++Z8ZZN.........?8OOZ7OZZZ8::,.......................................................")
	print("......D.....M7=++I88OZONMMMMNNNNNNNDDD:.............................................................")
	print("..............,M?=8888OZONMMMMMMMMN.................................................................")
	print("................:IDD8888ZZONMMMMN...................................................................")
	print("..................NNDD8888OOMMM.....................................................................")
	print("...................MMMNNDD88NMD.....................................................................")
	print("...................NMMMMMMMMN.,.....................................................................")
	print("...................MMMMMMMMM........................................................................")
	print("...................NNMMMMMMM........................................................................")
	print("...................8DDDNDNN.........................................................................")
	print("..................$8Z8OOD...........................................................................")
	print("..................O$OOZ$............................................................................")
	print(".................,OOO8ZN............................................................................")
	print(".................7O8O8O.............................................................................")
	print(".................NDDDD..............................................................................")
	print(".................DNDNZ..............................................................................")
	print(".................MDND...............................................................................")
	print(".................MNM................................................................................")
	print(".................MMM................................................................................")
	print("..................M?................................................................................")
	print("..................$.................................................................................")
	print("\t\tby " + __author__ + " to asnorth\n\n")


def main(argv):

	server_auth = 0

	try:
		opts, args = getopt.getopt(argv, "h:v", ["help", "version"])
	except getopt.GetoptError:
		print("Go read the README.md!")
		sys.exit(1)

	for opt, args in opts:
		if opt in ("-v", "--version"):
			print_me()
			sys.exit(0)
		elif opt in ("-h", "--help"):
			print("Go read the README.md!")
			sys.exit(1)

	error_handler = includes.when_things_go_south.Error_Handler()       # Error event handler

	# Change default location of conf file!
	conf_file = "confs/example.conf"

	''' Start parsing configuration file '''
	try:
		config = ConfigParser.ConfigParser()
		config.read(conf_file)
	except ConfigParser, e:
		error_handler.log_error(3, "Could not access configuration file.\nTechnical Log:\n" + str(e))
	try:
		server_name = config.get('server', 'address')
		server_port = config.getint('server', 'port')
		address_list_file = config.get('phish', 'addresses_csv')
		htmlbody_file = config.get('phish', 'html_body')
		txtbody_file = config.get('phish', 'txt_body')
		subject = config.get('phish', 'subject')
		attachment_list = config.get('phish', 'attachments')
	except ConfigParser, e:
		error_handler.log_error(3, "Something is wrong when parsing configuration file.\nTechnical Log:\n " + str(e))

	# Try to import server authentication, if there are configurations for that
	try:
		SMTPusername = config.get('server', 'username')
		SMTPpassword = config.get('server', 'password')
		server_auth = 1
	except:
		SMTPusername = ""
		SMTPpassword = ""
		server_auth = 0
	''' Finished Parsing Conf File '''

	mail_handler = includes.email_modules.MailModule(server_name, server_port, server_auth, SMTPusername, SMTPpassword)            # Mail Handler

	address_array = mail_handler.parse_csv(address_list_file)

	html_file_handler = open(htmlbody_file, 'rb')
	html_body = html_file_handler.read()

	txt_file_handler = open(txtbody_file, 'rb')
	txt_body = txt_file_handler.read()

	attachment_list = attachment_list.split(', ')
	if len(attachment_list) is 0:
		attachment_list = []

	amount_to_send = len(address_array)
	i = 0
	for from_mail, to_mail in address_array:
		mail_handler.send_email(from_mail, to_mail, subject, html_body, txt_body, attachment_list, i, amount_to_send)
		i += 1

if __name__ == "__main__":
	main(sys.argv[1:])
