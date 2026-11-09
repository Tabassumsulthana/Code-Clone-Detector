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
    """Calculate structural similarity percentage and breakdown statistics."""
    processed1 = preprocess_code(code1)
    processed2 = preprocess_code(code2)
    
    if not processed1 or not processed2:
        return 0.0, [], 0, 0
        
    matcher = SequenceMatcher(None, processed1, processed2)
    similarity = matcher.ratio() * 100
    
    # Identify matching line blocks
    matching_blocks = matcher.get_matching_blocks()
    
    # Calculate simple metric ratios for the visualization dashboard
    total_len = len(processed1) + len(processed2)
    matched_len = sum(block.size for block in matching_blocks)
    
    identical_ratio = (matched_len * 2) / total_len if total_len > 0 else 0
    unique_ratio = 1.0 - identical_ratio
    
    return round(similarity, 2), matching_blocks, identical_ratio, unique_ratio
