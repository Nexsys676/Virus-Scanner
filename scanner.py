import os
import platform
from datetime import datetime
import json
import readchar
from utils.logger import log_suspicious, log_maybe
from utils.fileloader import get_files_by_type
from detectors import python, cpp, shell, go, java, js, ts, rust, php, ruby, csharp, kotlin, swift, lua

input_dir = "input"
base_output_dir = "out"

detector_modules = {
    ".py": python,
    ".cpp": cpp, ".cc": cpp, ".cxx": cpp, ".hpp": cpp, ".h": cpp,
    ".sh": shell,
    ".go": go,
    ".java": java,
    ".js": js,
    ".ts": ts,
    ".rs": rust,
    ".php": php,
    ".rb": ruby,
    ".cs": csharp,
    ".kt": kotlin,
    ".swift": swift,
    ".lua": lua
}

# Cross-platform clear command
clear_cmd = "cls" if os.name == "nt" else "clear"

def is_enter(key):
    return key in ["\n", "\r", "\x0d", readchar.key.ENTER]

def scan_file(path, module):
    logs=[]
    not_safe=False
    try:
        with open(path,"r",encoding="utf-8",errors="ignore") as f:
            for idx,line in enumerate(f,1):
                hits,module_hits=module.scan_line(line)
                if hits:
                    if module_hits=="not_safe":
                        not_safe=True
                        logs.append({"line":idx,"content":line.strip(),"patterns":hits})
                        log_suspicious(idx,line,hits)
                    else:
                        logs.append({"line":idx,"content":line.strip(),"patterns":hits})
                        log_maybe(idx,line,hits)
    except Exception as e:
        logs.append({"line":0,"content":"","error":str(e)})
    category="safe"
    if not_safe:
        category="not_safe"
    elif logs:
        category="maybe_safe"
    return {"file":os.path.basename(path),"category":category,"logs":logs,"timestamp":datetime.utcnow().isoformat()}

def menu_select(options):
    index = 0
    selected = set()
    while True:
        os.system(clear_cmd)
        print(f"=== {platform.system().upper()} SCANNER ===")
        print(f"Detected OS: {platform.system()} {platform.release()}\n")
        print("Select file types to scan (SPACE=toggle, ENTER=start):\n")
        for i,opt in enumerate(options):
            cursor = "-> " if i==index else "   "
            mark = "[x]" if i in selected else "[ ]"
            print(f"{cursor}{mark} {opt}")
        key = readchar.readkey()
        if key==readchar.key.UP:
            index = (index - 1) % len(options)
        elif key==readchar.key.DOWN:
            index = (index + 1) % len(options)
        elif key==" ":
            if index in selected:
                selected.remove(index)
            else:
                selected.add(index)
        elif is_enter(key):
            return [options[i] for i in selected]

def main():
    files=get_files_by_type(input_dir, detector_modules.keys())
    if not files:
        print("No supported files found in input/")
        return
    detected_types=list(set([os.path.splitext(f)[1] for f in files]))
    selected_types=menu_select(detected_types)

    now=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir=os.path.join(base_output_dir,now)
    os.makedirs(output_dir,exist_ok=True)

    for f in files:
        ext=os.path.splitext(f)[1]
        if ext not in selected_types:
            continue
        path=os.path.join(input_dir,f)
        module=detector_modules[ext]
        report=scan_file(path,module)
        cat=report["category"]
        safe_name=f.replace(".","_")
        out_file=os.path.join(output_dir,f"{safe_name}_{cat}.json")
        with open(out_file,"w") as w:
            json.dump(report,w,indent=4)
        print(f"Report saved: {out_file}")

if __name__=="__main__":
    main()

