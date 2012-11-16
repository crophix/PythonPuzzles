A = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
translated = ''
for c in A:
	if c.isalpha():
		num = ord(c)
		num+=2
		if num > ord('z'):
			num -= 26
		elif num < ord('a'):
			num += 26
		translated += chr(num)
	else:
		translated += c
print translated