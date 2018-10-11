import whitespacedata as wsd
testdata = "blehasdfghjkla"
whitespace = wsd.convert_to_whitespace(testdata)
plaintext = wsd.convert_to_plaintext(whitespace)
print(whitespace)
print(plaintext)
