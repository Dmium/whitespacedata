import bitarray
bit_ws_table = {
    (False, False, False): "  ",
    (False, False, True): " 	",
	(False, True, False): " \n",
	(False, True, True): "	 ",
	(True, False, False): "		",
	(True, False, True): "	\n",
	(True, True, False): "\n ",
	(True, True, True): "\n	"
    }
ws_bit_table = {
    "  ": (False, False, False),
    " 	": (False, False, True),
	" \n": (False, True, False),
	"	 ": (False, True, True),
	"		": (True, False, False),
	"	\n": (True, False, True),
	"\n ": (True, True, False),
	"\n	": (True, True, True)
	}
ba = bitarray.bitarray()

def bits_to_whitespace(bit1, bit2, bit3):
    return bit_ws_table[(bit1, bit2, bit3)]

def convert_to_whitespace(stringdata):
    ba.frombytes(stringdata.encode('utf-8'))
    bitlist = ba.tolist()
    wsdata = ""
    for x in range(0, int(len(bitlist)/3)):
        wsdata += bits_to_whitespace(bitlist[x * 3], bitlist[x * 3 + 1], bitlist[x * 3 + 2])
    if int(len(bitlist) % 3) == 2:
        wsdata += bits_to_whitespace(bitlist[-1], False, False)
    elif int(len(bitlist) % 3) == 1:
        wsdata += bits_to_whitespace(bitlist[-2], bitlist[-1], False)
    return wsdata

def whitespace_to_bits(ws):
	return ws_bit_table[ws]

def convert_to_plaintext(wsdata):
	bitdata = []
	for x in range(0, int(len(wsdata)/2)):
		print(wsdata[x * 2:x * 2 + 1])
		bitdata.extend(whitespace_to_bits(wsdata[x * 2:x * 2 + 2]))
	if (len(bitdata) % 8) != 0:
		print("whoops")
		bitdata = bitdata[0:0-(8-(len(bitdata) % 8))]
	return bitarray.bitarray(bitdata).tobytes().decode('utf-8')
