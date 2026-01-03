import os
import sys
import datetime
import yaml  # Requires pip install PyYAML
import re

# Map simple shortcuts to full category names
CATEGORY_MAP = {
    "1": "01-Arrays-and-Hashing",
    "2": "02-Two-Pointers",
    "3": "03-Stack",
    "4": "04-Binary-Search",
    "5": "05-Sliding-Window",
    "6": "06-Linked-List",
    "7": "07-Trees",
    "8": "08-Tries",
    "9": "09-Backtracking",
    "10": "10-Heap-Priority-Queue",
    "11": "11-Graphs",
    "12": "12-1D-DP",
    "13": "13-Intervals",
    "14": "14-Greedy",
    "15": "15-Advanced-Graphs",
    "16": "16-2D-DP",
    "17": "17-Bit-Manipulation",
    "18": "18-Math-and-Geometry"
}

def find_existing_problem(problem_id):
    """Searches for an existing problem folder by ID."""
    for root, dirs, files in os.walk("."):
        if "scripts" in root or ".git" in root: continue
        for d in dirs:
            # Skip categories and non-matching IDs
            if re.match(r"^\d{2}-", d):
                continue
            #　Ｍatch problem ID
            if d.startswith(f"{problem_id}-"):
                return os.path.join(root, d), d.split("-", 1)[1].replace("-", " ")
    return None, None

def get_next_attempt_number(path):
    """Finds the next attempt number based on existing files."""
    attempts = [0]
    for f in os.listdir(path):
        match = re.match(r"attempt_(\d+)\.py", f)
        if match:
            attempts.append(int(match.group(1)))
    return max(attempts) + 1

def create_problem(cat_key, problem_id, problem_name=None):
    # Check if problem already exists
    existing_path, existing_name = find_existing_problem(problem_id)
    
    if existing_path:
        print(f"Found existing problem: {existing_name} at {existing_path}")
        path = existing_path
        problem_name = existing_name # Use existing name
    else:
        # New problem creation logic
        if not problem_name:
            print("Error: New problem requires a problem name.")
            return
            
        category = CATEGORY_MAP.get(str(cat_key))
        if not category:
            print(f"Error: Invalid category key '{cat_key}'.")
            return

        folder_name = f"{problem_id}-{problem_name.replace(' ', '-')}"
        path = os.path.join(".", category, folder_name)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created directory: {path}")

    # Determine next attempt number
    next_num = get_next_attempt_number(path)
    
    # 1. Create new python file
    new_file = f"attempt_{next_num}.py"
    code_path = os.path.join(path, new_file)
    if not os.path.exists(code_path):
        open(code_path, "w").close()
        print(f"Created new practice file: {code_path}")

    # 2. Update meta.yaml
    meta_path = os.path.join(path, "meta.yaml")
    today = str(datetime.date.today())
    
    if os.path.exists(meta_path):
        # Append to existing yaml
        with open(meta_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Check if the last line has a newline character
        if lines and not lines[-1].endswith('\n'):
            lines[-1] += '\n'
            
        with open(meta_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
            f.write(f"  - date: \"{today}\"\n")
            f.write(f"    status: \"pending\"  # Attempt {next_num}\n")
            f.write(f"    notes: \"\"\n")
        print(f"Updated meta.yaml with Attempt {next_num}")
        
    else:
        # Create new yaml (only happens for brand new problems)
        url_slug = problem_name.lower().replace(' ', '-')
        with open(meta_path, "w", encoding="utf-8") as f:
            f.write(f'''id: {problem_id}
title: "{problem_name}"
difficulty: "Medium"
url: "https://leetcode.com/problems/{url_slug}/"
tags: []
attempts:
  - date: "{today}"
    status: "pending"
    notes: ""
''')
        print(f"Created meta.yaml")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  New Problem:   python scripts/add_problem.py <cat> <id> \"<name>\"")
        print("  Retry Problem: python scripts/add_problem.py 0 <id>") 
        print("Example: python scripts/add_problem.py 0 242")
    else:
        # cat_key can be '0' or anything if we just provide ID for lookup
        create_problem(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
