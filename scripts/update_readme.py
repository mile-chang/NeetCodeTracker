import os
import yaml
import datetime

ROOT_DIR = "."
README_FILE = "README.md"

# Status Icons mapping
# Visual indicators for the progress of each problem
STATUS_ICONS = {
    "red": "🔴",      # Failed attempt
    "yellow": "🟡",   # Struggled but solved
    "green": "🟢",    # Solved efficiently
    "pending": "⚪",  # Not attempted yet
}

# Difficulty Icons mapping
DIFFICULTY_ICONS = {
    "Easy": "🟢",
    "Medium": "🟠",
    "Hard": "🔴"
}

def get_days_ago(date_str):
    """
    Calculate how many days have passed since the last attempt.
    
    Args:
        date_str (str): Date string in 'YYYY-MM-DD' format.
        
    Returns:
        int: Number of days elapsed, or 999 if the date is invalid.
    """
    if not date_str: return 999
    try:
        last_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        delta = (datetime.date.today() - last_date).days
        return delta
    except:
        return 999

def scan_problems():
    """
    Traverse the directory structure to find all 'meta.yaml' files.
    Parses problem data, tracks history, and extracts the latest notes for flashcards.
    
    Returns:
        tuple: (List of problem dictionaries, total attempts count, green status count)
    """
    problems = []
    total_attempts = 0
    greens = 0
    
    # Iterate over category directories (e.g., '01-Arrays-and-Hashing')
    for category in sorted(os.listdir(ROOT_DIR)):
        cat_path = os.path.join(ROOT_DIR, category)
        
        # Skip non-directory files, hidden folders, and script folders
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
                    latest_note = "" # Stores the note from the most recent attempt
                    
                    # Build history string icons and update status
                    for attempt in attempts:
                        s = attempt.get('status', 'pending')
                        history += STATUS_ICONS.get(s, "⚪") + " "
                        
                        # Update latest date and status
                        last_date = attempt.get('date', "")
                        current_status = s
                        
                        # Capture the note if it exists (Overwrites previous notes)
                        if attempt.get('notes'):
                            latest_note = attempt.get('notes')
                        
                    if current_status == "green":
                        greens += 1
                    if len(attempts) > 0:
                        total_attempts += 1

                    days_ago = get_days_ago(last_date)
                    
                    # Spaced Repetition Logic (SR algorithm)
                    # Green: Review after 14 days
                    # Yellow: Review after 3 days
                    # Red: Retry after 1 day
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
                        "review_flag": review_flag,
                        "latest_note": latest_note # Pass the note to the generator
                    })
                except Exception as e:
                    print(f"Error parsing {meta_file}: {e}")
    return problems, total_attempts, greens

def generate_markdown(problems, total, greens):
    """
    Generates the Markdown content for the README.md file.
    Includes a progress bar, dashboard table, and hidden flashcard notes.
    """
    content = f"# 🚀 NeetCode 150 Progress Tracker\n\n"
    
    # Progress Bar Calculation
    total_problems = 150
    progress_pct = int((greens / total_problems) * 100) if total_problems > 0 else 0
    progress_bar = "█" * (progress_pct // 2) + "░" * ((100 - progress_pct) // 2)
    
    content += f"### Proficiency: {progress_pct}% ({greens}/{total_problems})\n"
    content += f"`{progress_bar}`\n\n"
    content += f"**Last Updated:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    
    # Dashboard Table Header
    # Added 'Note' column for flashcards
    content += "| Category | ID | Problem | Diff | History | Last Practice | Status | Note |\n"
    content += "|---|:---:|---|:---:|---|:---:|---|---|\n"
    
    current_cat = ""
    for p in problems:
        # Group by category: Only display category name when it changes
        cat_display = f"**{p['category']}**" if p['category'] != current_cat else ""
        current_cat = p['category']
        
        diff_icon = DIFFICULTY_ICONS.get(p['difficulty'], "⚪")
        
        # Display 'days ago' only for valid dates
        days_display = f"({p['days_ago']}d ago)" if p['days_ago'] != 999 else ""
        
        # Flashcard Logic:
        # Wrap notes in HTML <details> tags to hide them by default.
        # This encourages active recall rather than passive reading.
        note_display = "-"
        if p['latest_note'] and str(p['latest_note']).strip():
            # Convert newlines to HTML line breaks for table compatibility
            formatted_note = str(p['latest_note']).replace('\n', '<br>')
            note_display = f"<details><summary>🔍 Hint</summary>{formatted_note}</details>"
        
        row = f"| {cat_display} | {p['id']} | [{p['title']}]({p['path']}) | {diff_icon} | {p['history']} | {p['last_date']} {days_display} | {p['review_flag']} | {note_display} |\n"
        content += row
        
    return content

if __name__ == "__main__":
    probs, total, green_count = scan_problems()
    md = generate_markdown(probs, total, green_count)
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(md)
    print("README.md updated successfully!")
