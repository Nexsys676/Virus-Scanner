import re

not_safe_patterns={
    "runtime_exec": r"Runtime\.getRuntime\(\)\.exec\(",
    "process_builder": r"ProcessBuilder\(",
    "file_delete": r"Files\.delete",
}
maybe_patterns={
    "regex_pattern": r"Pattern\.compile",
    "network_socket": r"Socket\("
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

