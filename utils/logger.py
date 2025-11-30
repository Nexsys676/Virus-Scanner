from datetime import datetime
from rich import print

def log_suspicious(line_number,line,patterns):
    print(f"[red][{datetime.now().strftime('%H:%M:%S')}] Suspicious line {line_number}: {line.strip()[:100]} -> {patterns}[/red]")

def log_maybe(line_number,line,patterns):
    print(f"[yellow][{datetime.now().strftime('%H:%M:%S')}] Maybe suspicious line {line_number}: {line.strip()[:100]} -> {patterns}[/yellow]")

