#str.isdecimal() (Only Decimal Numbers) return true if all character are decimal
print("34".isdecimal())  #True
print("\u00B2")#superscript 2
print("\u00B2".isdecimal())  #False

#str.isdigit() (Decimals, Subscripts, Superscripts) retrun true if all the character all digit

print("34".isdigit()) #True
print("\u00B2")
print("\u00B2".isdigit()) #True

#str.isnumeric() (Digits, Vulgar Fractions, Subscripts, Superscripts, Roman Numerals, Currency Numerators) return true if all character are numeric

print("34".isnumeric()) #True
print("\u00B2")
print("\u00B2".isnumeric()) #True

print("\u00BC")#Quarter numeric
print("\u00BC".isnumeric()) #True