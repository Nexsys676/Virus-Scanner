import re

not_safe_patterns={
    "eval": r"eval\(",
    "exec": r"\b(exec|shell_exec|system)\(",
}
maybe_patterns={
    "preg": r"preg_match",
}

def scan_line(line):
    hits=[]
    for k,p in not_safe_patterns.items():
        if re.search(p,line):
            hits.append(k)
    if hits:
        return hits,"not_safe"
    hits=[]
    for k,p in maybe_patterns.items():
        if re.search(p,line):
            hits.append(k)
    if hits:
        return hits,"maybe_safe"
    return [],None

