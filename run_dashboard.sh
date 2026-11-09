#!/usr/bin/env bash
# ==============================================================================
# ITC Hotels Analytics Project — Terminal Hub
# Invertis University, Bareilly | BCA Final Year Project
# ==============================================================================

BASE_DIR="/home/goku/ITC_Hotels_Project"
VENV_PYTHON="$BASE_DIR/.venv/bin/python"
VENV_JUPYTER="$BASE_DIR/.venv/bin/jupyter"
DB_FILE="$BASE_DIR/ITC-Final-Dashboards/itc_hotel_analytics.db"
PDF_FILE="$BASE_DIR/00_FINAL_DASHBOARDS_READY_TO_SUBMIT/4_COMPLETE_REPORT_PDF/ITC_Hotels_Project_Complete_Documentation.pdf"
EXCEL_FILE="$BASE_DIR/00_FINAL_DASHBOARDS_READY_TO_SUBMIT/1_EXCEL_DASHBOARD/ITC_Executive_Live_Dashboard.xlsx"

echo "=========================================================="
echo "  🏨 ITC HOTELS ANALYTICS & DATABASE SYSTEM"
echo "  BCA Final Year Project | Invertis University"
echo "=========================================================="
echo "1) Open Data Cleaning & EDA Notebook (Matplotlib Charts)"
echo "2) Open Interactive Plotly Executive Dashboard (Jupyter)"
echo "3) Open Master Live Excel Dashboard (.xlsx)"
echo "4) Open Complete 18-Page Project Report PDF"
echo "5) Launch Interactive SQL Query Shell (SQLite/MySQL)"
echo "6) View Database Schema & Statistics (18 Tables in 3NF)"
echo "7) Exit"
echo "=========================================================="
read -p "Enter choice [1-7]: " choice

case $choice in
    1)
        echo "Starting Jupyter Notebook with Data Cleaning & EDA..."
        cd "$BASE_DIR/00_FINAL_DASHBOARDS_READY_TO_SUBMIT/2_JUPYTER_DASHBOARD"
        "$VENV_JUPYTER" notebook data_cleaning_eda.ipynb
        ;;
    2)
        echo "Starting Jupyter Notebook with Interactive Dashboard..."
        cd "$BASE_DIR/00_FINAL_DASHBOARDS_READY_TO_SUBMIT/2_JUPYTER_DASHBOARD"
        "$VENV_JUPYTER" notebook interactive_jupyter_dashboard.ipynb
        ;;
    3)
        echo "Opening Master Excel Dashboard..."
        xdg-open "$EXCEL_FILE" 2>/dev/null || libreoffice "$EXCEL_FILE" &
        ;;
    4)
        echo "Opening Complete Project Report PDF..."
        xdg-open "$PDF_FILE" 2>/dev/null || evince "$PDF_FILE" &
        ;;
    5)
        echo "Launching Interactive SQLite SQL Shell on itc_hotel_analytics.db..."
        sqlite3 "$DB_FILE"
        ;;
    6)
        echo "Showing Database Tables & Record Counts:"
        "$VENV_PYTHON" -c "
import sqlite3
conn = sqlite3.connect('$DB_FILE')
c = conn.cursor()
tables = [t[0] for t in c.execute('SELECT name FROM sqlite_master WHERE type in (\'table\',\'view\') ORDER BY name').fetchall()]
print(f'\\n{\"Table/View\":<25} {\"Records\":>12}')
print('─' * 38)
for t in tables:
    cnt = c.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]
    print(f'{t:<25} {cnt:>12,}')
"
        ;;
    *)
        echo "Exiting."
        ;;
esac
