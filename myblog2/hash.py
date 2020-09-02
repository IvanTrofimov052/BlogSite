import hashlib

class Hash:
	def hash_password(password, z):
		m = hashlib.sha256()
		m.update(str(password).encode('utf-8'))
		return m.digest()