import whitespacedata as wsd
testdata = "blehasdfghjklaaaa"
whitespace = wsd.convert_to_whitespace(testdata)
plaintext = wsd.convert_to_plaintext(whitespace)
print(whitespace)
print(plaintext)
