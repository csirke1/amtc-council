#!/usr/bin/env python3
"""Read-only AMTC public website smoke test; no credentials or production changes."""
import sys
import urllib.error
import urllib.request

BASE = "https://federationofeurope.eu"
PATHS = {
    "/": b"ai-negy-torvenye",
    "/ai-negy-torvenye": b"AZ AI",
    "/four-laws-of-ai": b"FOUR LAWS",
    "/constitution.json": b"sections",
    "/challenge.json": b"{",
}

def main():
    failures = []
    for path, marker in PATHS.items():
        url = BASE + path
        try:
            with urllib.request.urlopen(
                urllib.request.Request(url, headers={"User-Agent": "AMTC-public-smoke-test/1.0"}),
                timeout=15,
            ) as response:
                body = response.read(150000)
                status = response.status
            valid = status == 200 and marker.lower() in body.lower()
            print(f"{'PASS' if valid else 'FAIL'} {url} status={status} bytes={len(body)}")
            if not valid:
                failures.append(path)
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            print(f"FAIL {url} error={type(exc).__name__}: {exc}")
            failures.append(path)
    if failures:
        print(f"Failed endpoints: {', '.join(failures)}", file=sys.stderr)
        return 1
    print("All public endpoints responded with expected content.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
