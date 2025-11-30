import re

not_safe_patterns={
    "danger_rm": r"rm\s+-rf",
    "nc_listen": r"\bnc\s+-l",
    "dd_overwrite": r"dd\s+if="
}
maybe_patterns={
    "curl_wget": r"\bcurl\b|\bwget\b",
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

