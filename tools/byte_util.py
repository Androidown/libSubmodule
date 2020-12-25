

def to_int(bytes):
	print(f"got bytes {bytes}")
	print(f"got another update.")
	return int.from_bytes(bytes, 'little')
