import re

not_safe_patterns={
    "base64_exec": r"(eval|exec)\(.*base64",
    "os_system": r"os\.system\(",
    "subprocess_exec": r"subprocess\.",
    "pickle_marshal": r"pickle\.|marshal\."
}
maybe_patterns={
    "requests": r"requests\.get",
    "regex_compile": r"re\.compile\("
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

