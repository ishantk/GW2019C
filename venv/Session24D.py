import re # RegularExpressions

quote = "Search the candle rather than cursing the darkness"
# result = re.match("Search", quote)
# result = re.match("candle", quote)
result = re.match("Sea", quote)
print(result)
print(result.start())
print(result.end())

print()

result = re.search("the", quote)
print(result)

print()
result = re.findall("the", quote)
print(result)

print()
result = re.split("the", quote)
print(result)

print()
result = re.sub("the","a", quote)
print(result)
print(quote)

print("==========")

newQuote = "Work Hard and Get Luckier"
result = re.findall(".", newQuote)
print(result)

print()

result = re.findall("\w", newQuote)
print(result)

print()

result = re.findall("\w*", newQuote)
print(result)

print()

result = re.findall("\w+", newQuote)
print(result)

# Task : Vehicle Number : PB10AL1010
# With Regular Expressions tell if the entered number is correct or incorrect
# 1. Alphabets, 2. Numeric (AlphaNumeric)
# Validate Email : john@example.com
