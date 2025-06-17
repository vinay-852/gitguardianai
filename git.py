import os
import shutil
import subprocess
import tempfile
import requests

def get_git_show(repo_url):
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Step 2: Clone the repo
        subprocess.run(['git', 'clone', repo_url, temp_dir], check=True)

        # Step 3: Run git show in that repo
        git_show_output = subprocess.check_output(
            ['git', 'show'],
            cwd=temp_dir,
            text=True
        )
        return git_show_output.strip()

    except subprocess.CalledProcessError as e:
        print("Error running subprocess:", e)
    except Exception as ex:
        print("Unexpected error:", ex)
    finally:
        shutil.rmtree(temp_dir)
