"""backlink_checker.py — check a list of URLs: HTTP status + whether a target
link/keyword appears in the page HTML. Useful when verifying that a profile
page actually shows your website link.

Usage:
    python backlink_checker.py urls.txt "https://santoledge.com"

urls.txt: one URL per line. Output: CSV rows to stdout.
Only standard library (urllib) — no dependencies to install.
"""
import csv
import sys
import urllib.request
from urllib.error import HTTPError, URLError

TIMEOUT = 20


def check(url, target):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            return resp.status, target in html, ""
    except HTTPError as e:
        return e.code, False, f"HTTPError: {e.code}"
    except URLError as e:
        return -1, False, f"URLError: {e.reason}"
    except Exception as e:  # noqa: BLE001 - report, don't crash
        return -1, False, f"{type(e).__name__}: {e}"


def main():
    if len(sys.argv) != 3:
        print("Usage: python backlink_checker.py urls.txt \"https://example.com\"")
        sys.exit(1)
    urls_file, target = sys.argv[1], sys.argv[2]
    with open(urls_file, encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]
    writer = csv.writer(sys.stdout)
    writer.writerow(["url", "status", "target_found", "error"])
    for url in urls:
        status, found, err = check(url, target)
        writer.writerow([url, status, found, err])


if __name__ == "__main__":
    main()
