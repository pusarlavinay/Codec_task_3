# modules/http_info.py
import requests
from typing import Dict

def fetch_http_info(url: str, timeout: float = 5.0) -> Dict:
    """Fetch headers and basic info for a URL (GET)."""
    try:
        resp = requests.get(url, timeout=timeout, allow_redirects=True)
        info = {
            "url": resp.url,
            "status_code": resp.status_code,
            "headers": dict(resp.headers),
            "server": resp.headers.get("Server"),
            "content_length": len(resp.content),
        }
        # Check robots.txt quickly
        try:
            robots = requests.get(f"{resp.url.rstrip('/')}/robots.txt", timeout=3)
            info["robots_exists"] = robots.status_code == 200
        except Exception:
            info["robots_exists"] = False
        return info
    except Exception as e:
        return {"url": url, "error": str(e)}

if __name__ == "__main__":
    import sys, json
    url = sys.argv[1] if len(sys.argv) > 1 else input("Enter URL: ")
    print(json.dumps(fetch_http_info(url), indent=2))
