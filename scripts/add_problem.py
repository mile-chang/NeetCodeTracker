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

def find_existing_problem(problem_id, preferred_category=None):
    """Searches for an existing problem folder by ID.
    
    Args:
        problem_id: The problem ID to search for
        preferred_category: Optional category folder to prioritize (e.g., "02-Two-Pointers")
    
    Returns:
        Tuple of (full_path, problem_name) or (None, None) if not found
    """
    matches = []
    
    for root, dirs, files in os.walk("."):
        if "scripts" in root or ".git" in root:
            continue
        for d in dirs:
            # Look for folders starting with the problem ID
            # Ex: problem_id = "36" -> "36-Valid-Sudoku"
            # Split by "-" and check if the first part exactly matches the problem_id
            parts = d.split("-", 1)
            if len(parts) >= 2 and parts[0] == str(problem_id):
                full_path = os.path.join(root, d)
                problem_name = parts[1].replace("-", " ")
                matches.append((full_path, problem_name, root))
    
    if not matches:
        return None, None
    
    # If we have a preferred category, try to find a match in that category first
    if preferred_category:
        for full_path, problem_name, root in matches:
            if preferred_category in root:
                return full_path, problem_name
    
    # Otherwise return the first match
    return matches[0][0], matches[0][1]

def get_next_attempt_number(path):
    """Finds the next attempt number based on existing files."""
    attempts = [0]
    for f in os.listdir(path):
        match = re.match(r"attempt_(\d+)\.py", f)
        if match:
            attempts.append(int(match.group(1)))
    return max(attempts) + 1

def create_problem(cat_key, problem_id, problem_name=None):
    # Get category for preferred matching
    category = CATEGORY_MAP.get(str(cat_key))
    
    # Check if problem already exists (prefer matches in the specified category)
    existing_path, existing_name = find_existing_problem(problem_id, category)
    
    if existing_path:
        print(f"Found existing problem: {existing_name} at {existing_path}")
        path = existing_path
        problem_name = existing_name # Use existing name
    else:
        # New problem creation logic
        if not problem_name:
            print("Error: New problem requires a problem name.")
            return
            
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
