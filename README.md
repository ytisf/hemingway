#Hemingway

##Introduction
This tool was built to allow simpler campaigns of phishing. It does not try to resolve issues with SMTP relaying or reputation but rather to allow a penetration tester or red team member to create a phishing campaign with a ready made server for the phishing. We also assume that if you are dealing with anti-phishing components you have already mapped their rules. 
Original repository and updates will be available at <https://github.com/ytisf/hemingway>

##Usage
For now, Hemingway will not get a configuration file from the user but will rather work with a template. 
The ***example.conf*** file in the ***confs*** is currently available for example. The configuration file, however, is not the only files required but also the ***sample_conf*** folder which we'll cover in a minute. 

	[server]
	address: 192.168.10.80
	port: 25
	
	[phish]
	addresses_csv: sample_conf/addresses.csv
	html_body: sample_conf/body.html
	txt_body: sample_conf/body.txt
	subject: What are you doing here?
	attachments: sample_conf/body.html, sample_conf/body.txt

This file is pretty straight and forward. It will give Hemingway the information it needs for the phishing campaign. Which files to attach (separated by a ',' which means as much files as you want), subject of the email and HTML and TXT body. 
Now let's have a look at the addresses file ***sample_conf/addresses.csv***:

	Bill Gates <Bill.Gates@microsoft.com>;tisf@mailinator.com
	Roger Waters <rogers@p-floyd.com>;tisf@mailinator.com
	John Cleese <john.c@python.com>;tisf@mailinator.com
	Douglas Adams <adams@hhgttu.org>;tisf@mailinator.com
	Karl Marx <everyone@state.com>;tisf@mailinator.com

As you can see, not much to say here as well. On the left will be the addresses for the spoofed sender and on the right the addresses of the victims. 

**HTML**
When you are creating you HTML body please remember that each image you embed will later be attached to the body and chagned to a CID so the recipients' email clients' will be able to interpret those images. Keep the images in the body of the email for the regex to find and store the images at the same folder as the HTML body is at, aka ***sample_conf***.

##File Structure

###confs
This folder holds the configuration files and in future will hold a few templates. Currently only holding ***example.conf***

###includes
This folders holds the core of Hemingway
* email_modules.py - ***As it says. This module will manage, build and send the emails.***
* when_things_go_south.py - ***Error handler. A big pile of mess. ***
###sample_conf
* addresses.csv - ***the address list as described earlier. ***
* body.html - ***the mail HTML body. this one will be parsed for the images attached. ***
* body.txt - ***the alternative text body ***
* url.jpg - ***an in-body image just for an example ***

##Future Change Log
- [ ] Add support for mail server authentication.
- [ ] Add simpler HTML interface.
- [ ] Comprehensive support for logging and summery.

##License (GPLv3)
Hemingway - A Phishing Campaign Helper
Copyright (C) 2014  Yuval tisf Nativ

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


