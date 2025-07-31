import subprocess

def get_staged_diff():
    result = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True)
    return result.stdout.strip()

def run_git_commit(commit_message):
    subprocess.run(["git", "commit", "-m", commit_message])
