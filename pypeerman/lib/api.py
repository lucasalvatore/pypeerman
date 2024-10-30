import requests

def make_request(base_url, headers, endpoint):
    url = f"{base_url}{endpoint}"
    response = requests.get(url, headers=headers)
    # response = requests.get(**kwargs)
    response.raise_for_status()
    return response.json()

def fetch_all(base_url, headers, endpoint):
    """Handle API pagination"""
    url = f"{base_url}{endpoint}"
    results = []
    prevurl = None
    s = requests.Session()
    while url:
        resp = s.get(url, headers=headers).json()
        results.extend(resp["results"])
        prevurl = url
        url = resp["next"]
        if url == prevurl:
            raise RuntimeError(f"Enountered API pagination loop at {url}")
    return results