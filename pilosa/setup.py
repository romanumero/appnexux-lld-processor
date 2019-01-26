import pilosa

client = pilosa.Client()

schema = client.schema()

clientIndex = schema.index("client_a")