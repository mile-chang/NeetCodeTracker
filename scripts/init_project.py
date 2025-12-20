import os

# NeetCode 150 Categories based on the official roadmap
CATEGORIES = [
    "01-Arrays-and-Hashing",
    "02-Two-Pointers",
    "03-Stack",
    "04-Binary-Search",
    "05-Sliding-Window",
    "06-Linked-List",
    "07-Trees",
    "08-Tries",
    "09-Backtracking",
    "10-Heap-Priority-Queue",
    "11-Graphs",
    "12-1D-DP",
    "13-Intervals",
    "14-Greedy",
    "15-Advanced-Graphs",
    "16-2D-DP",
    "17-Bit-Manipulation",
    "18-Math-and-Geometry"
]

def create_structure():
    base_path = "."
    
    # Create category directories
    for cat in CATEGORIES:
        path = os.path.join(base_path, cat)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created: {path}")

    # Create scripts directory if it doesn't exist
    if not os.path.exists("scripts"):
        os.makedirs("scripts")

    # Create an example problem: Contains Duplicate
    # This serves as a template for your workflow
    example_path = os.path.join(base_path, "01-Arrays-and-Hashing", "217-Contains-Duplicate")
    if not os.path.exists(example_path):
        os.makedirs(example_path)
        
        # Create example meta.yaml
        meta_content = """id: 217
title: "Contains Duplicate"
difficulty: "Easy"
url: "https://leetcode.com/problems/contains-duplicate/"
tags: ["Array", "Hash Table"]
attempts:
  - date: "2025-01-01"
    status: "red"   # Options: red, yellow, green
    notes: "Time Limit Exceeded with brute force. Forgot to use Set."
  - date: "2025-01-05"
    status: "green"
    notes: "Used HashSet for O(n) time complexity."
"""
        with open(os.path.join(example_path, "meta.yaml"), "w", encoding="utf-8") as f:
            f.write(meta_content)
            
        # Create an empty python file for code
        open(os.path.join(example_path, "attempt_1.py"), "w").close()
        print(f"Created Example: {example_path}")

if __name__ == "__main__":
    create_structure()
