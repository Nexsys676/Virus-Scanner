import re

not_safe_patterns={
    "eval": r"eval\(",
    "child_process": r"require\('child_process'\)",
}
maybe_patterns={
    "regex": r"new RegExp",
    "http_request": r"fetch\(",
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

