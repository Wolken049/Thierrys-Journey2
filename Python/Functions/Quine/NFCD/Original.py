import os, sys, subprocess

gen = 0
max_gen = 2
branch_factor = 2
node_id = "0"
path = r"Python/Functions/Quine/NFCD"

os.makedirs(path, exist_ok=True)

s = 'import os, sys, subprocess\n\ngen = %d\nmax_gen = %d\nbranch_factor = %d\nnode_id = %r\npath = %r\n\nos.makedirs(path, exist_ok=True)\n\ns = %r\n\nif gen < max_gen:\n    for x in range(branch_factor):\n        child_id = f"{node_id}_{x}"\n        filename = os.path.join(path, f"Clone_{child_id}.py")\n        with open(filename, "w") as f:\n            f.write(s %% (gen + 1, max_gen, branch_factor, child_id, path, s))\n        print(f"Executing Generation {gen+1}: {filename}")\n        subprocess.run([sys.executable, filename])'

if gen < max_gen:
    for x in range(branch_factor):
        child_id = f"{node_id}_{x}"
        filename = os.path.join(path, f"Clone_{child_id}.py")
        with open(filename, "w") as f:
            f.write(s % (gen + 1, max_gen, branch_factor, child_id, path, s))
        print(f"Executing Generation {gen+1}: {filename}")
        subprocess.run([sys.executable, filename])