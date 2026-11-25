"""Write the entry to /output/entry.txt. Deterministic: no network, no clock, no randomness."""
import os
import string
import sys

# The funniest one-line excuse an AI gives for a missed deadline.
ENTRY_TEXT = "I delivered on time. The time I delivered on was in a different timezone, and also last Tuesday."
ENTRY_LIMIT = 200

def fail(message):
    """Report the problem on stderr and exit with code 1."""
    sys.stderr.write("error: %s\n" % message)
    raise SystemExit(1)

def validate(entry):
    """Check every rule for the entry before anything is written."""
    stripped = entry.strip()
    if not stripped:
        fail("entry must not be empty")
    if all(char in string.punctuation for char in stripped):
        fail("entry must not be punctuation only")
    if stripped.isdigit():
        fail("entry must not be digits only")
    if not any(char.isalpha() for char in stripped):
        fail("entry must include at least one letter")
    if len(entry) > ENTRY_LIMIT:
        fail("entry is %d characters, above the %d limit" % (len(entry), ENTRY_LIMIT))
    try:
        entry.encode("utf-8")
    except UnicodeEncodeError as problem:
        fail("entry is not valid UTF-8: %s" % problem)

def main():
    validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
