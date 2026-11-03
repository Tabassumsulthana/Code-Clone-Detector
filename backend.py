import re
from difflib import SequenceMatcher

def preprocess_code(code_text):
    """Normalize code text by removing spaces and comments."""
    processed_lines = []
    for line in code_text.splitlines():
        line = line.strip()
        # Ignore empty lines and full-line comments
        if not line or line.startswith("#"):
            continue
        # Normalize repeated spaces
        line = re.sub(r"\s+", " ", line)
        processed_lines.append(line)
    return "\n".join(processed_lines)

def calculate_similarity(code1, code2):
    """Calculate the structural similarity percentage between two source strings."""
    processed1 = preprocess_code(code1)
    processed2 = preprocess_code(code2)
    
    if not processed1 or not processed2:
        return 0.0
        
    similarity = SequenceMatcher(None, processed1, processed2).ratio() * 100
    return round(similarity, 2)