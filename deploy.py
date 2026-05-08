#!/usr/bin/env python3
"""
deploy.py — One-command GitHub Pages portfolio deployer
Usage: python deploy.py
"""

import os
import shutil
import subprocess
import sys

# ─── CONFIG ───────────────────────────────────────────────────────────────────
GITHUB_USERNAME = "Alexxgutierrez"   
REPO_NAME       = "portfolio"            
# ──────────────────────────────────────────────────────────────────────────────

REPO_URL = f"https://github.com/Alexxgutierrez/portfolio.git"

def run(cmd, check=True):
    print(f"  » {cmd}")
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.returncode != 0 and check:
        print(f"\n❌ Error: {result.stderr.strip()}")
        sys.exit(1)
    return result

def check_git():
    r = run("git --version", check=False)
    if r.returncode != 0:
        print("❌ Git is not installed. Please install it from https://git-scm.com")
        sys.exit(1)

def main():
    print("\n🚀 Portfolio GitHub Pages Deployer")
    print("=" * 40)

    check_git()

    # 1. Copy portfolio files to a temp deploy directory
    deploy_dir = "/tmp/portfolio_deploy"
    if os.path.exists(deploy_dir):
        shutil.rmtree(deploy_dir)
    shutil.copytree(".", deploy_dir, ignore=shutil.ignore_patterns(".git", "deploy.py", "__pycache__"))
    print(f"\n✅ Portfolio files staged at {deploy_dir}")

    os.chdir(deploy_dir)

    # 2. Git init
    print("\n📁 Initializing git repository...")
    run("git init")
    run(f"git checkout -b {BRANCH}")

    # 3. Configure git user (if not already set)
    name_result  = run("git config user.name", check=False)
    email_result = run("git config user.email", check=False)
    if not name_result.stdout.strip():
        run(f'git config user.name "{GITHUB_USERNAME}"')
    if not email_result.stdout.strip():
        run(f'git config user.email "{GITHUB_USERNAME}@users.noreply.github.com"')

    # 4. Add remote
    print(f"\n🔗 Setting remote to {REPO_URL}")
    run(f"git remote add origin {REPO_URL}", check=False)

    # 5. Stage and commit
    print("\n📝 Committing files...")
    run("git add -A")
    run('git commit -m "Deploy portfolio to GitHub Pages"')

    # 6. Push
    print(f"\n📤 Pushing to GitHub ({REPO_URL})...")
    result = run(f"git push -u origin {BRANCH} --force", check=False)
    if result.returncode != 0:
        print("\n⚠️  Push failed. Common reasons:")
        print("   • Repository doesn't exist — create it at https://github.com/new")
        print("   • Authentication error — use a GitHub Personal Access Token")
        print("   • Try: git push with HTTPS + token or set up SSH keys")
        sys.exit(1)

    print("\n" + "=" * 40)
    print("✅ Deployed successfully!")
    print(f"\n🌐 Your portfolio will be live at:")
    print(f"   https://{GITHUB_USERNAME}.github.io/{REPO_NAME}/")
    print("\n💡 Enable GitHub Pages:")
    print(f"   → Go to https://github.com/{GITHUB_USERNAME}/{REPO_NAME}/settings/pages")
    print(f"   → Source: Deploy from branch → {BRANCH} → / (root)")
    print("=" * 40 + "\n")

if __name__ == "__main__":
    main()
