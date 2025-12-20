import os
import yaml
import datetime

ROOT_DIR = "."
README_FILE = "README.md"

# Status Icons mapping
STATUS_ICONS = {
    "red": "🔴",
    "yellow": "🟡",
    "green": "🟢",
    "pending": "⚪"
}

# Difficulty Icons mapping
DIFFICULTY_ICONS = {
    "Easy": "🟢",
    "Medium": "🟡",
    "Hard": "🔴"
}

def get_days_ago(date_str):
    """Calculate how many days have passed since the last attempt."""
    if not date_str: return 999
    try:
        last_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        delta = (datetime.date.today() - last_date).days
        return delta
    except:
        return 999

def scan_problems():
    """
    Traverse the directory structure to find all meta.yaml files.
    Returns a list of problem data, total count, and green count.
    """
    problems = []
    total_attempts = 0
    greens = 0
    
    # Iterate over category directories
    for category in sorted(os.listdir(ROOT_DIR)):
        cat_path = os.path.join(ROOT_DIR, category)
        # Skip non-directory files and hidden/system folders
        if not os.path.isdir(cat_path) or category.startswith(".") or category == "scripts":
            continue
            
        # Iterate over problem directories within a category
        for problem_dir in sorted(os.listdir(cat_path)):
            p_path = os.path.join(cat_path, problem_dir)
            meta_file = os.path.join(p_path, "meta.yaml")
            
            if os.path.exists(meta_file):
                try:
                    with open(meta_file, 'r', encoding='utf-8') as f:
                        data = yaml.safe_load(f)
                        
                    attempts = data.get('attempts', [])
                    history = ""
                    last_date = ""
                    current_status = "pending"
                    
                    # Build history string icons
                    for attempt in attempts:
                        s = attempt.get('status', 'pending')
                        history += STATUS_ICONS.get(s, "⚪") + " "
                        last_date = attempt.get('date', "")
                        current_status = s
                        
                    if current_status == "green":
                        greens += 1
                    if len(attempts) > 0:
                        total_attempts += 1

                    days_ago = get_days_ago(last_date)
                    
                    # Spaced Repetition Logic
                    # Rules: 
                    # - Green: Review after 14 days
                    # - Yellow: Review after 3 days
                    # - Red: Retry after 1 day
                    review_flag = ""
                    if current_status == "green" and days_ago > 14: review_flag = "🔔 Review"
                    elif current_status == "yellow" and days_ago > 3: review_flag = "🔔 Review"
                    elif current_status == "red" and days_ago > 1: review_flag = "🔥 Retry"

                    problems.append({
                        "category": category,
                        "id": data.get('id', '0'),
                        "title": data.get('title', problem_dir),
                        "difficulty": data.get('difficulty', 'Medium'),
                        "path": f"./{category}/{problem_dir}",
                        "history": history,
                        "last_date": last_date,
                        "days_ago": days_ago,
                        "review_flag": review_flag
                    })
                except Exception as e:
                    print(f"Error parsing {meta_file}: {e}")
    return problems, total_attempts, greens

def generate_markdown(problems, total, greens):
    """Generates the content for the README.md file."""
    content = f"# 🚀 NeetCode 150 Progress Tracker\n\n"
    
    # Progress Bar Logic
    total_problems = 150
    # Avoid division by zero
    progress_pct = int((greens / total_problems) * 100) if total_problems > 0 else 0
    progress_bar = "█" * (progress_pct // 2) + "░" * ((100 - progress_pct) // 2)
    
    content += f"### Proficiency: {progress_pct}% ({greens}/{total_problems})\n"
    content += f"`{progress_bar}`\n\n"
    content += f"**Last Updated:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    
    # Dashboard Table Header
    content += "| Category | ID | Problem | Diff | History (Attempts) | Last Practice | Status |\n"
    content += "|---|:---:|---|:---:|---|:---:|---|\n"
    
    current_cat = ""
    for p in problems:
        # Only display category name when it changes for a cleaner look
        cat_display = f"**{p['category']}**" if p['category'] != current_cat else ""
        current_cat = p['category']
        
        diff_icon = DIFFICULTY_ICONS.get(p['difficulty'], "⚪")
        
        # Format the table row
        # days_ago is only shown if it's a valid number (not 999 for new problems)
        days_display = f"({p['days_ago']}d ago)" if p['days_ago'] != 999 else ""
        
        row = f"| {cat_display} | {p['id']} | [{p['title']}]({p['path']}) | {diff_icon} | {p['history']} | {p['last_date']} {days_display} | {p['review_flag']} |\n"
        content += row
        
    return content

if __name__ == "__main__":
    probs, total, green_count = scan_problems()
    md = generate_markdown(probs, total, green_count)
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(md)
    print("README.md updated successfully!")