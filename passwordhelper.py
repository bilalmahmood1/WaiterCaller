import hashlib
import os
import base64

class PasswordHelper:

	def to_bytes(self, bytes_or_str):
		if isinstance(bytes_or_str, str):
			value = bytes_or_str.encode('utf-8')
		else:
			value = bytes_or_str
		return value # Instance of bytes

	def to_str(self, bytes_or_str):
		if isinstance(bytes_or_str, bytes):
			value = bytes_or_str.decode('utf-8')
		else:
			value = bytes_or_str
		return value # Instance of bytes

	def get_hash(self, plain):
		return hashlib.sha512(self.to_bytes(plain)).hexdigest()
	
	def get_salt(self):
		return self.to_str(base64.b64encode(os.urandom(20)))
	
	def validate_password(self, plain, salt, expected):
		return self.get_hash(plain + salt) == expected

