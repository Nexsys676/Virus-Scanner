import re

not_safe_patterns={
    "os_execute": r"os\.execute",
    "loadstring": r"loadstring\(",
}
maybe_patterns={
    "regex": r"string\.match",
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

