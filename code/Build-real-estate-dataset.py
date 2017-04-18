import quandl

# Not necessary, I just do this so I do not show my API key.
api_key = open('quandlapikey.txt','r').read()

api_key = api_key.strip()

df = quandl.get("FMAC/HPI_TX", authtoken=api_key)

print(df.head())
