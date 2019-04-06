 """
The encode() method returns an encoded version of the string(byte string). Default encoding is the current default string encoding. The errors may be given to set a different error handling scheme.

The decode() method decodes the string (byte string) using the codec registered for encoding. It defaults to the defaultstring encoding.
str.encode(encoding = 'UTF-8',errors = 'strict')
Str.decode(encoding = 'UTF-8',errors = 'strict')

Parameters

    encoding − This is the encodings to be used. For a list of all encoding schemes please visit − Standard Encodings.

    errors − This may be given to set a different error handling scheme. The default for errors is 'strict', meaning that encoding errors raise a UnicodeError. Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' and any other name registered via codecs.register_error().

Str = "this is string example....wow!!!";
Str = Str.encode('base64','strict');

print "Encoded String: " + Str
print "Decoded String: " + Str.decode('base64','strict')

Encoded String: b'dGhpcyBpcyBzdHJpbmcgZXhhbXBsZS4uLi53b3chISE='

Decoded String: this is string example....wow!!!
"""