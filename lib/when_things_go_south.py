import sys


class Error_Handler():
	"""
	This is just a simple and simple error handler
	"""
	def __init__(self):
		pass

	class bcolors:
		HEADER = '\033[95m'
		OKBLUE = '\033[94m'
		OKGREEN = '\033[92m'
		WARNING = '\033[93m'
		FAIL = '\033[91m'
		ENDC = '\033[0m'

	def log_error(self, id, error):
		"""
		:param id: Identifier of error type
		:param error: Error message
		:return: nothing
		"""

		# 0 = info, 1=warning, 2=error, 3=critical

		if id == 0:
			sys.stdout.write(self.bcolors.OKGREEN + "[+] " + self.bcolors.ENDC + error + "\n")

		elif id == 1:
			sys.stderr.write(self.bcolors.WARNING + "[-] " + self.bcolors.ENDC + error + "\n")

		elif id == 2:
			sys.stderr.write(self.bcolors.FAIL + "[!] " + self.bcolors.ENDC + error + "\n")

		elif id == 3:
			sys.stderr.write(self.bcolors.FAIL + "[!] " + self.bcolors.ENDC + error + "\n")
			sys.exit(1)

		else:
			print("Go learn your error handler!!!!")
			sys.exit(1)
