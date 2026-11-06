#!/usr/bin/env bash
# ==============================================================================
# ITC Hotels Analytics Project — Automated GitHub Multi-Repo Push Script
# Usage: ./push_all_to_github.sh <YOUR_GITHUB_USERNAME>
# ==============================================================================

set -e

if [ -z "$1" ]; then
    echo "Usage: ./push_all_to_github.sh <YOUR_GITHUB_USERNAME>"
    echo "Example: ./push_all_to_github.sh avisingh4121"
    exit 1
fi

GITHUB_USER="$1"
BASE_DIR="/home/goku/ITC_Hotels_Project"

MODULES=(
    "ITC-Room-Analytics"
    "ITC-FnB-Analytics"
    "ITC-Guest-Demographics"
    "ITC-Profitability-Costs"
    "ITC-Final-Dashboards"
)

echo "================================================================="
echo "  ITC HOTELS — PUSHING REPOSITORIES TO GITHUB"
echo "  Target GitHub User: $GITHUB_USER"
echo "================================================================="

for mod in "${MODULES[@]}"; do
    REPO_DIR="$BASE_DIR/$mod"
    REPO_URL="https://github.com/$GITHUB_USER/$mod.git"

    echo ""
    echo ">>> Processing $mod..."
    cd "$REPO_DIR"

    # Check if remote origin exists, if so update it, else add it
    if git remote | grep -q "origin"; then
        git remote set-url origin "$REPO_URL"
    else
        git remote add origin "$REPO_URL"
    fi

    # Ensure branch is main
    git branch -M main

    echo "Pushing $mod to $REPO_URL..."
    # Attempt push
    if git push -u origin main; then
        echo "✓ Successfully pushed $mod"
    else
        echo "⚠️ Note: Make sure the repository '$mod' is already created on your GitHub account!"
    fi
done

echo ""
echo "================================================================="
echo "  ALL REPOSITORIES PROCESSED!"
echo "================================================================="
