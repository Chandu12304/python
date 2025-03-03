agencies = {
    "CBI": "Central Bureau of Investigation",
    "FBI": "Foreign Direct Investment",
    "NIA": "National Investigation Agency",
    "SSB": "Service Selection Board",
    "WBA": "Works Progress Administration"
}

print(agencies)
print("*********")

agencies["BSE"]="Bombay Stock Exchange"

print(agencies)
print("*********")

agencies["SSB"]="Social Security Administration"

print(agencies)
print("*********")

agencies.pop("CBI",None)
agencies.pop("WBA",None)

print(agencies)
print("*********")
