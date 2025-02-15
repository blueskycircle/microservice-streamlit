import wikipedia

def scrape(name="Microsoft"):
    result = wikipedia.summary(name)
    return result