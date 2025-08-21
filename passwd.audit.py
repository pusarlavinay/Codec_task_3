# modules/passwd_audit.py
import re
from typing import Dict

def check_strength(password: str) -> Dict:
    """Basic password strength checks (length, char classes)."""
    checks = {
        "length": len(password) >= 12,
        "has_upper": bool(re.search(r"[A-Z]", password)),
        "has_lower": bool(re.search(r"[a-z]", password)),
        "has_digit": bool(re.search(r"\d", password)),
        "has_symbol": bool(re.search(r"[^\w\s]", password)),
    }
    score = sum(checks.values())
    strength = {0: "very weak", 1: "very weak", 2: "weak", 3: "moderate", 4: "strong", 5: "very strong"}[score]
    return {"password": None, "score": score, "strength": strength, "details": checks}

def check_against_list(password: str, breached_list_path: str) -> bool:
    """Check password against a local list of breached passwords (one per line).
       Use only with your own test passwords or approved wordlists."""
    try:
        with open(breached_list_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                if line.strip() == password:
                    return True
    except FileNotFoundError:
        return False
    return False

# Example: use in code only on your passwords or lab accounts
if __name__ == "__main__":
    p = input("Enter password to audit (do not use real passwords): ")
    print(check_strength(p))
