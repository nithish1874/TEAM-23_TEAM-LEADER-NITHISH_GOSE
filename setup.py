"""
Setup script for Digital Fatigue Manager
Run this to initialize the project
"""
import sys
import subprocess
import os

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"\n{'='*50}")
    print(f"Step: {description}")
    print(f"{'='*50}")
    print(f"Running: {cmd}\n")
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return False

def main():
    """Main setup function"""
    print("\n" + "="*50)
    print("Digital Fatigue Manager - Setup")
    print("="*50 + "\n")
    
    # Get current directory
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    
    steps = [
        ("pip install -r requirements.txt", "Installing Python dependencies"),
        (f'python -c "import sys; sys.path.insert(0, \\".\\"); from backend.models.database import init_db; init_db(); print(\\"✅ Database initialized!\\")"', "Initializing database"),
        (f'python -c "import sys; sys.path.insert(0, \\".\\"); exec(open(\\"sample_data.py\\").read())"', "Loading sample data (optional)"),
    ]
    
    for cmd, desc in steps:
        if not run_command(cmd, desc):
            print(f"\n❌ Setup failed at: {desc}")
            print("Please check the error messages above.")
            return False
    
    print("\n" + "="*50)
    print("✅ Backend setup complete!")
    print("="*50)
    print("\nNext steps:")
    print("1. Install frontend dependencies: cd frontend && npm install")
    print("2. Run backend: cd backend && python main.py")
    print("3. Run frontend (in new terminal): cd frontend && npm run dev")
    print("\n")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

