import re

not_safe_patterns={
    "unsafe": r"\bunsafe\.",
    "exec_cmd": r"exec\.Command",
}
maybe_patterns={
    "reflect": r"\breflect\.",
    "network": r"net\.Dial",
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

