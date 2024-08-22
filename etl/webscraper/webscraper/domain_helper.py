from urllib.parse import urlparse

class DomainHelper():
    def extract_domain_from_url(self, url: str):
        if url == "":
            raise ValueError("URL is required")
        
        return urlparse(url).netloc
    