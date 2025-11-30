import re

not_safe_patterns={
    "system_call": r"system\(",
    "exec_calls": r"execvp\(|fork\(",
    "mmap_usage": r"mmap\(",
}
maybe_patterns={
    "regex_std": r"std::regex",
    "socket_usage": r"socket\("
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

