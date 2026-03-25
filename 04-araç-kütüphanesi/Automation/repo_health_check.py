import os
import sys

def check_repo_health(repo_path):
    """
    Checks the directory structure and look for empty directories or missing documentation.
    """
    print(f"[SEARCH] PAISE Repository Health Check starting at: {repo_path}\n")
    
    issues_found = 0
    
    # Check for core directories
    core_dirs = ["01-felsefe-ve-zihniyet", "02-teknik-mufredat", "03-vaka-analizleri", "04-araç-kütüphanesi", "99-sistem-ve-arsiv"]
    for d in core_dirs:
        full_path = os.path.join(repo_path, d)
        if not os.path.exists(full_path):
            print(f"X [MISSING] Core directory not found: {d}")
            issues_found += 1
        else:
            # Check if empty
            if not os.listdir(full_path):
                print(f"! [EMPTY] Directory is empty: {d}")
                issues_found += 1

    # Check for README files in curriculum phases
    curr_path = os.path.join(repo_path, "02-teknik-mufredat")
    if os.path.exists(curr_path):
        for phase in os.listdir(curr_path):
            phase_path = os.path.join(curr_path, phase)
            if os.path.isdir(phase_path) and not any(f.endswith('.md') for f in os.listdir(phase_path)):
                print(f"! [NO_CONTENT] Phase directory has no markdown content: {phase}")
                issues_found += 1

    print(f"\n* Health Check Completed. Total Issues Found: {issues_found}")
    return issues_found

if __name__ == "__main__":
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    check_repo_health(repo_root)
