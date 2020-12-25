

def to_int(bytes):
	print(f"got bytes {bytes}")
	return int.from_bytes(bytes, 'little')
