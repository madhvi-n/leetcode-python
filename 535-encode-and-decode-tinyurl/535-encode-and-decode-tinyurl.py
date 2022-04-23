class Codec:

    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodeMap:
            val = str(len(self.encodeMap))
            self.encodeMap[longUrl] = self.base + val
            self.decodeMap[self.base + val] = longUrl
        
        return self.encodeMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodeMap[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))