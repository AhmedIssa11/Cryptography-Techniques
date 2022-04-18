import math

key = "4312567"

def encryptRT(msg):
	cipher = ""
	key_index = 0

	msg_len = float(len(msg))
	msg_list = list(msg)
	key_list = sorted(list(key))
	col = len(key)
	
	# calculate the row of the matrix
	row = int(math.ceil(msg_len / col))

	# the empty cells of the matix "_"
	fill_null = int((row * col) - msg_len)
	msg_list.extend('_' * fill_null)

	# row-wise
	matrix = [msg_list[i: i + col]
			for i in range(0, len(msg_list), col)]
      
	# column-wise
	for _ in range(col):
		curr_index = key.index(key_list[key_index])
		cipher += ''.join([row[curr_index] for row in matrix])
		key_index += 1

	return cipher

# Decryption
def decryptRT(cipher):
	msg = ""
	k_indx = 0
	msg_indx = 0
	msg_len = float(len(cipher))
	msg_lst = list(cipher)
	col = len(key)
	
	# calculate maximum row of the matrix
	row = int(math.ceil(msg_len / col))
	key_lst = sorted(list(key))

	# create an empty matrix to

	dec_cipher = []
	for _ in range(row):
		dec_cipher += [[None] * col]

	# Arrange the matrix column wise according
	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])

		for j in range(row):
			dec_cipher[j][curr_idx] = msg_lst[msg_indx]
			msg_indx += 1
		k_indx += 1

	msg = ''.join(sum(dec_cipher, []))

	null_count = msg.count('_')

	if null_count > 0:
		return msg[: -null_count]

	return msg

# main
msg = "attackpostponeduntiltwoam"

cipher = encryptRT(msg)
print("Encrypted Message: {}". format(cipher))

print("Decryped Message: {}". format(decryptRT(cipher)))


