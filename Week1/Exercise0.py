import os

# ==========================================
# Q1. Import Blocklist and Ensure Uniqueness
# ==========================================
print("--- Question 1 ---")

blocklist_filepath = 'blocklist.txt'
# Using a set() is best for blocklists because it automatically handles 
# uniqueness and makes checking if a user exists much faster than a list.
blocked_users = set() 

try:
    # Attempt to open the file
    with open(blocklist_filepath, 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            # .strip() removes whitespace and newlines (\n) from both ends
            username = line.strip() 
            if username: # Ensure we don't add empty lines
                blocked_users.add(username)
                
    print(f"Blocklist imported. Total unique blocked users: {len(blocked_users)}")
    print(f"Usernames: {blocked_users}")

except FileNotFoundError:
    # This block runs only if the file does not exist, satisfying the requirement 
    print(f"Error: The file '{blocklist_filepath}' was not found.")

# ==========================================
# Q2. Process Visitors
# ==========================================
print("\n--- Question 2 ---")

vistors_fp = 'visitors.txt'

if os.path.exists(vistors_fp):
    with open(vistors_fp, 'r') as f:
        lines = f.readlines()
        visitors_today = []
        for line in lines:
            line = line.rstrip()
            if line not in visitors_today:
                visitors_today.append(line)
else:
    raise FileExistsError

print("Access Denied for:")
for visitor in visitors_today:
    # Check if the visitor is in our set of blocked users
    if visitor in blocked_users:
        print(f" -> {visitor}")

# ==========================================
# Q3. Append New Offender
# ==========================================
print("\n--- Question 3 ---")

new_offender = "alice@wonderland.co.uk"

try:
    # Open file in 'a' (append) mode to add to the end without overwriting
    with open(blocklist_filepath, 'a') as f:
        # We add a newline character \n ensuring it starts on a new line
        f.write(f"\n{new_offender}")
    
    print(f"User '{new_offender}' has been added to the blocklist.")

except FileNotFoundError:
    print(f"Error: Could not append to '{blocklist_filepath}' because it does not exist.")