from workflow import run_workflow
from dashboard import show_dashboard

if __name__ == "__main__":
    print("Starting Grant Agent...")
    run_workflow()
    print("Workflow complete. Opening dashboard...")
    show_dashboard()