import matplotlib.pyplot as plt
import matplotlib.patches as patches

# List of Telangana districts (33)
regions = [
    "Adilabad", "Bhadradri_Kothagudem", "Hyderabad", "Jagtial", "Jangaon",
    "Jayashankar_Bhupalpally", "Jogulamba_Gadwal", "Kamareddy", "Karimnagar",
    "Khammam", "Komaram_Bheem", "Mahabubabad", "Mahabubnagar", "Mancherial",
    "Medak", "Medchal_Malkajgiri", "Mulugu", "Nagarkurnool", "Nalgonda",
    "Narayanpet", "Nirmal", "Nizamabad", "Peddapalli", "Rajanna_Sircilla",
    "Ranga_Reddy", "Sangareddy", "Siddipet", "Suryapet", "Vikarabad",
    "Wanaparthy", "Warangal_Rural", "Warangal_Urban", "Yadadri_Bhuvanagiri"
]

# Adjacency list
graph = {

    "Adilabad": ["Komaram_Bheem", "Nirmal"],
    "Komaram_Bheem": ["Adilabad", "Mancherial"],
    "Mancherial": ["Komaram_Bheem", "Peddapalli", "Nirmal"],
    "Nirmal": ["Adilabad", "Mancherial", "Nizamabad"],
    "Nizamabad": ["Nirmal", "Kamareddy"],
    "Kamareddy": ["Nizamabad", "Medak", "Rajanna_Sircilla"],
    
    "Rajanna_Sircilla": ["Kamareddy", "Karimnagar", "Siddipet"],
    "Karimnagar": ["Rajanna_Sircilla", "Peddapalli", "Jagtial"],
    "Peddapalli": ["Karimnagar", "Mancherial", "Jayashankar_Bhupalpally"],
    "Jagtial": ["Karimnagar", "Nizamabad"],
    
    "Jayashankar_Bhupalpally": ["Peddapalli", "Mulugu", "Warangal_Rural"],
    "Mulugu": ["Jayashankar_Bhupalpally", "Warangal_Rural", "Bhadradri_Kothagudem"],
    
    "Bhadradri_Kothagudem": ["Mulugu", "Khammam"],
    "Khammam": ["Bhadradri_Kothagudem", "Mahabubabad", "Suryapet"],
    
    "Mahabubabad": ["Khammam", "Warangal_Rural"],
    "Warangal_Rural": ["Mahabubabad", "Warangal_Urban", "Jangaon", "Mulugu"],
    "Warangal_Urban": ["Warangal_Rural", "Jangaon"],
    
    "Jangaon": ["Warangal_Urban", "Siddipet", "Yadadri_Bhuvanagiri"],
    "Siddipet": ["Jangaon", "Medak", "Rajanna_Sircilla"],
    
    "Medak": ["Kamareddy", "Siddipet", "Sangareddy"],
    "Sangareddy": ["Medak", "Ranga_Reddy", "Vikarabad"],
    
    "Ranga_Reddy": ["Hyderabad", "Sangareddy", "Vikarabad", "Medchal_Malkajgiri"],
    "Hyderabad": ["Ranga_Reddy"], 
    
    "Medchal_Malkajgiri": ["Ranga_Reddy", "Yadadri_Bhuvanagiri"],
    
    "Yadadri_Bhuvanagiri": ["Medchal_Malkajgiri", "Jangaon", "Nalgonda"],
    "Nalgonda": ["Yadadri_Bhuvanagiri", "Suryapet", "Nagarkurnool"],
    
    "Suryapet": ["Nalgonda", "Khammam"],
    
    "Nagarkurnool": ["Nalgonda", "Mahabubnagar", "Wanaparthy"],
    "Mahabubnagar": ["Nagarkurnool", "Wanaparthy", "Narayanpet"],
    "Wanaparthy": ["Nagarkurnool", "Mahabubnagar", "Jogulamba_Gadwal"],
    
    "Jogulamba_Gadwal": ["Wanaparthy", "Narayanpet"],
    "Narayanpet": ["Mahabubnagar", "Jogulamba_Gadwal", "Vikarabad"],
    
    "Vikarabad": ["Sangareddy", "Ranga_Reddy", "Narayanpet"]
}

# Colors (domain)
domain = ["Red", "Green", "Blue", "Pink"]

# Assignment
assignment = {}

# Constraint check
def is_valid(region, color):
    for neighbor in graph.get(region, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking
def backtrack(index):
    if index == len(regions):
        return True

    region = regions[index]

    for color in domain:
        if is_valid(region, color):
            assignment[region] = color
            if backtrack(index + 1):
                return True
            del assignment[region]

    return False

# Solve CSP
if backtrack(0):
    print("District Coloring:\n")
    for r in regions:
        print(f"{r} --> {assignment[r]}")
else:
    print("No solution found")

# Visualization
cols = 6
rows = 6

fig, ax = plt.subplots(figsize=(8, 8))

positions = {}
i = 0
for r in range(rows):
    for c in range(cols):
        if i < len(regions):
            positions[regions[i]] = (c, rows - r - 1)
            i += 1

for region, (x, y) in positions.items():
    color = assignment[region].lower()
    
    rect = patches.Rectangle((x, y), 1, 1, edgecolor='black', facecolor=color)
    ax.add_patch(rect)
    
    ax.text(x + 0.5, y + 0.5, region[:5],
            ha='center', va='center', fontsize=6, color='white')

ax.set_xlim(0, cols)
ax.set_ylim(0, rows)
ax.axis('off')

plt.title("Telangana District Map Coloring (CSP)")
plt.show()
