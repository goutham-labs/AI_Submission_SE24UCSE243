import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mcolors
import numpy as np

districts = [
    "Adilabad", "Bhadradri_Kothagudem", "Hyderabad", "Jagtial", "Jangaon",
    "Jayashankar_Bhupalpally", "Jogulamba_Gadwal", "Kamareddy", "Karimnagar",
    "Khammam", "Komaram_Bheem", "Mahabubabad", "Mahabubnagar", "Mancherial",
    "Medak", "Medchal_Malkajgiri", "Mulugu", "Nagarkurnool", "Nalgonda",
    "Narayanpet", "Nirmal", "Nizamabad", "Peddapalli", "Rajanna_Sircilla",
    "Ranga_Reddy", "Sangareddy", "Siddipet", "Suryapet", "Vikarabad",
    "Wanaparthy", "Warangal_Rural", "Warangal_Urban", "Yadadri_Bhuvanagiri"
]

graph = {
    "Adilabad":                  ["Komaram_Bheem", "Nirmal"],
    "Komaram_Bheem":             ["Adilabad", "Mancherial"],
    "Mancherial":                ["Komaram_Bheem", "Peddapalli", "Nirmal", "Karimnagar"],
    "Nirmal":                    ["Adilabad", "Mancherial", "Nizamabad", "Kamareddy"],
    "Nizamabad":                 ["Nirmal", "Kamareddy", "Jagtial"],
    "Kamareddy":                 ["Nizamabad", "Medak", "Rajanna_Sircilla", "Nirmal", "Sangareddy"],
    "Rajanna_Sircilla":          ["Kamareddy", "Karimnagar", "Siddipet", "Jagtial"],
    "Karimnagar":                ["Rajanna_Sircilla", "Peddapalli", "Jagtial", "Mancherial"],
    "Peddapalli":                ["Karimnagar", "Mancherial", "Jayashankar_Bhupalpally"],
    "Jagtial":                   ["Karimnagar", "Nizamabad", "Rajanna_Sircilla"],
    "Jayashankar_Bhupalpally":   ["Peddapalli", "Mulugu", "Warangal_Rural"],
    "Mulugu":                    ["Jayashankar_Bhupalpally", "Warangal_Rural", "Bhadradri_Kothagudem"],
    "Bhadradri_Kothagudem":      ["Mulugu", "Khammam"],
    "Khammam":                   ["Bhadradri_Kothagudem", "Mahabubabad", "Suryapet"],
    "Mahabubabad":               ["Khammam", "Warangal_Rural", "Warangal_Urban"],
    "Warangal_Rural":            ["Mahabubabad", "Warangal_Urban", "Jangaon", "Mulugu", "Jayashankar_Bhupalpally"],
    "Warangal_Urban":            ["Warangal_Rural", "Jangaon", "Mahabubabad"],
    "Jangaon":                   ["Warangal_Urban", "Siddipet", "Yadadri_Bhuvanagiri", "Warangal_Rural"],
    "Siddipet":                  ["Jangaon", "Medak", "Rajanna_Sircilla", "Kamareddy", "Medchal_Malkajgiri"],
    "Medak":                     ["Kamareddy", "Siddipet", "Sangareddy"],
    "Sangareddy":                ["Medak", "Ranga_Reddy", "Vikarabad", "Kamareddy"],
    "Ranga_Reddy":               ["Hyderabad", "Sangareddy", "Vikarabad", "Medchal_Malkajgiri"],
    "Hyderabad":                 ["Ranga_Reddy", "Medchal_Malkajgiri"],
    "Medchal_Malkajgiri":        ["Ranga_Reddy", "Yadadri_Bhuvanagiri", "Hyderabad", "Siddipet"],
    "Yadadri_Bhuvanagiri":       ["Medchal_Malkajgiri", "Jangaon", "Nalgonda"],
    "Nalgonda":                  ["Yadadri_Bhuvanagiri", "Suryapet", "Nagarkurnool"],
    "Suryapet":                  ["Nalgonda", "Khammam"],
    "Nagarkurnool":              ["Nalgonda", "Mahabubnagar", "Wanaparthy"],
    "Mahabubnagar":              ["Nagarkurnool", "Wanaparthy", "Narayanpet"],
    "Wanaparthy":                ["Nagarkurnool", "Mahabubnagar", "Jogulamba_Gadwal"],
    "Jogulamba_Gadwal":          ["Wanaparthy", "Narayanpet"],
    "Narayanpet":                ["Mahabubnagar", "Jogulamba_Gadwal", "Vikarabad"],
    "Vikarabad":                 ["Sangareddy", "Ranga_Reddy", "Narayanpet"],
}

# CSP Backtracking solver
COLORS = ["#1D9E75", "#BA7517", "#534AB7", "#D85A30"]   # teal / amber / purple / coral
COLOR_NAMES = ["Teal", "Amber", "Purple", "Coral"]

assignment = {}

def is_valid(region, color):
    return all(assignment.get(nb) != color for nb in graph.get(region, []))

def backtrack(index=0):
    if index == len(districts):
        return True
    region = districts[index]
    for color in COLORS:
        if is_valid(region, color):
            assignment[region] = color
            if backtrack(index + 1):
                return True
            del assignment[region]
    return False

solved = backtrack()

if solved:
    print("=" * 45)
    print("   Telangana District Coloring (CSP Result)")
    print("=" * 45)
    for d in districts:
        cname = COLOR_NAMES[COLORS.index(assignment[d])]
        print(f"  {d:<35} →  {cname}")
    print("=" * 45)

    # Constraint verification
    violations = [
        (d, nb)
        for d in districts
        for nb in graph.get(d, [])
        if assignment.get(d) == assignment.get(nb)
    ]
    if violations:
        print(f"\n⚠  {len(violations)//2} constraint violation(s) found!")
    else:
        print("\n✓  All adjacency constraints satisfied — no two neighbors share a color.")
else:
    print("No solution found.")

geo_pos = {
    "Adilabad":                 (3.2, 9.5),
    "Komaram_Bheem":            (4.5, 9.0),
    "Nirmal":                   (2.2, 8.5),
    "Mancherial":               (4.2, 8.2),
    "Nizamabad":                (1.5, 7.5),
    "Jagtial":                  (3.6, 7.8),
    "Kamareddy":                (2.0, 6.8),
    "Rajanna_Sircilla":         (3.2, 7.0),
    "Karimnagar":               (4.2, 7.2),
    "Peddapalli":               (5.0, 7.5),
    "Jayashankar_Bhupalpally":  (5.7, 6.8),
    "Mulugu":                   (6.2, 6.0),
    "Bhadradri_Kothagudem":     (6.8, 5.0),
    "Khammam":                  (6.4, 4.0),
    "Mahabubabad":              (5.7, 5.0),
    "Medak":                    (1.9, 5.8),
    "Siddipet":                 (3.0, 6.0),
    "Warangal_Rural":           (5.0, 5.5),
    "Warangal_Urban":           (4.5, 5.8),
    "Jangaon":                  (4.0, 5.2),
    "Suryapet":                 (5.4, 3.8),
    "Sangareddy":               (1.5, 5.0),
    "Ranga_Reddy":              (1.8, 4.0),
    "Hyderabad":                (2.8, 4.5),
    "Medchal_Malkajgiri":       (3.2, 4.8),
    "Yadadri_Bhuvanagiri":      (3.8, 4.2),
    "Nalgonda":                 (4.2, 3.4),
    "Vikarabad":                (1.2, 3.5),
    "Nagarkurnool":             (2.6, 2.6),
    "Mahabubnagar":             (2.0, 2.0),
    "Wanaparthy":               (2.9, 1.8),
    "Jogulamba_Gadwal":         (2.2, 1.2),
    "Narayanpet":               (1.4, 1.8),
}

# Visualisation
fig, ax = plt.subplots(figsize=(13, 11))
fig.patch.set_facecolor("#F8F7F2")
ax.set_facecolor("#F8F7F2")

BOX_W, BOX_H = 0.85, 0.45

# Drawing adjacency edges first
drawn_edges = set()
for d, neighbors in graph.items():
    if d not in geo_pos:
        continue
    x1, y1 = geo_pos[d]
    cx1, cy1 = x1 + BOX_W / 2, y1 + BOX_H / 2
    for nb in neighbors:
        edge = tuple(sorted([d, nb]))
        if edge in drawn_edges or nb not in geo_pos:
            continue
        drawn_edges.add(edge)
        x2, y2 = geo_pos[nb]
        cx2, cy2 = x2 + BOX_W / 2, y2 + BOX_H / 2
        ax.plot([cx1, cx2], [cy1, cy2],
                color="#BBBBBB", linewidth=0.7, zorder=1, alpha=0.6)

# Drawing district boxes
for d in districts:
    if d not in geo_pos:
        continue
    x, y = geo_pos[d]
    color = assignment.get(d, "#CCCCCC")

    rect = patches.FancyBboxPatch(
        (x, y), BOX_W, BOX_H,
        boxstyle="round,pad=0.04",
        linewidth=1.2, edgecolor="white",
        facecolor=color, zorder=2
    )
    ax.add_patch(rect)

    label = d.replace("_", "\n") if len(d) > 14 else d.replace("_", " ")
    fontsize = 5.5 if "\n" in label else 6.5
    ax.text(x + BOX_W / 2, y + BOX_H / 2, label,
            ha="center", va="center",
            fontsize=fontsize, fontweight="bold",
            color="white", zorder=3,
            multialignment="center")

# Legend
from matplotlib.patches import Patch
color_counts = {c: sum(1 for v in assignment.values() if v == c) for c in COLORS}
legend_handles = [
    Patch(facecolor=c, edgecolor="white", linewidth=1,
          label=f"{COLOR_NAMES[i]}  ({color_counts[c]} districts)")
    for i, c in enumerate(COLORS)
]
ax.legend(handles=legend_handles, loc="lower right",
          framealpha=0.9, fontsize=9, title="Color assignment",
          title_fontsize=9, edgecolor="#CCCCCC")

ax.set_xlim(0, 8.5)
ax.set_ylim(0.5, 10.5)
ax.axis("off")
ax.set_title("Telangana District Map Coloring — CSP Backtracking\n"
             "(4 colors · no two adjacent districts share a color)",
             fontsize=13, fontweight="bold", pad=14, color="#2C2C2A")

plt.tight_layout()
plt.savefig("telangana_map_coloring.png", dpi=180, bbox_inches="tight",
            facecolor=fig.get_facecolor())
plt.show()
