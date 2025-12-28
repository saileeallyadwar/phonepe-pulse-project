from git import Repo
import os

repo_url = "https://github.com/PhonePe/pulse.git"
clone_dir = "phonepe_pulse_data"

if not os.path.exists(clone_dir):
    Repo.clone_from(repo_url, clone_dir)
    print("Repository cloned successfully")
else:
    print("Repository already exists")
