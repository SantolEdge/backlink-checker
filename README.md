# backlink-checker

A tiny zero-dependency Python script that checks a list of URLs and reports,
for each one, the HTTP status plus whether a target link (e.g. your website)
actually appears in the page HTML.

## Why

When you build profile backlinks across many directories, you need to verify
the link is really on the public page — not just that the profile exists.
This script automates that check.

## Usage

1. Put one URL per line in `urls.txt`.
2. Run:

```bash
python backlink_checker.py urls.txt "https://santoledge.com"
```

3. Read the CSV output (`url,status,target_found,error`).

Only the standard library is used (`urllib`), so there is nothing to install.
