import hashlib


# this class need to hash passwordsbefire we get they on the table
class Hash:
	def hash_password(self, password):
		return hashlib.sha256(password.encode('utf-8')).hexdigest() 