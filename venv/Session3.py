# Textual Data | AlphaNumeric +  Special Symbols

gender = "M"
gender = "Male"

# gender = Female -> error

print("Gender is: ",gender)
print("type of gender is",type(gender)) # str -> string or text

# businessName = 'Johns Coffee Shop'
# businessName = 'John's Coffee Shop' -> error
businessName = "John's Coffee Shop"
print(businessName)

message = "Hello" \
          "This is John" \
          "Thank You"

message = """Hello
This is John
Thank You"""

print(message)