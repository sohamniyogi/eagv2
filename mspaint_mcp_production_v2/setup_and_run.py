#!/usr/bin/env python3
"""
Setup and Run Script for MSPaint MCP Production v2
Sets up the Google Gemini API key and runs the demo
"""
import os
import sys
import subprocess
import threading
import time
import logging

# Set up the Google Gemini API key
GOOGLE_API_KEY = ""

def setup_environment():
    """Set up environment variables"""
    os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY
    os.environ['GEMINI_API_KEY'] = GOOGLE_API_KEY
    print(f"✅ Set GOOGLE_API_KEY: {GOOGLE_API_KEY[:20]}...")
    print(f"✅ Set GEMINI_API_KEY: {GOOGLE_API_KEY[:20]}...")

def check_requirements():
    """Check if required packages are installed"""
    required_packages = [
        'flask',
        'requests', 
        'pywinauto',
        'pywin32',
        'pillow',
        'google-genai'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        print("Installing missing packages...")
        for package in missing_packages:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
                print(f"✅ Installed {package}")
            except subprocess.CalledProcessError:
                print(f"❌ Failed to install {package}")
                return False
    else:
        print("✅ All required packages are installed")
    
    return True

def start_server():
    """Start the MCP server"""
    try:
        import mcp_server
        print("🚀 Starting MCP Server on http://127.0.0.1:5000")
        mcp_server.main()
    except Exception as e:
        print(f"❌ Server error: {e}")

def start_agent():
    """Start the AI agent"""
    try:
        import agent
        print("🤖 Starting AI Agent...")
        time.sleep(2)  # Give server time to start
        
        # Run with a custom question
        question = input("Enter your question for the AI agent (or press Enter for default): ").strip()
        if not question:
            question = "Draw a rectangle and write 'Hello AI!' inside it"
        
        print(f"🎯 Agent task: {question}")
        session = agent.run_agent(question, 'http://127.0.0.1:5000', 'llm_session.json')
        
        print("✅ Agent execution completed!")
        print("📄 Check 'llm_session.json' for detailed logs")
        print("📄 Check 'mcp_agent.log' for system logs")
        
        return session
        
    except Exception as e:
        print(f"❌ Agent error: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    """Main setup and execution function"""
    print("=" * 60)
    print("🎨 MSPaint MCP Production v2 - Setup & Run")
    print("=" * 60)
    
    # Check if running on Windows
    if os.name != 'nt':
        print("❌ This program requires Windows to control MS Paint")
        return
    
    print("✅ Running on Windows")
    
    # Setup environment
    setup_environment()
    
    # Check requirements
    if not check_requirements():
        print("❌ Failed to install required packages")
        return
    
    print("\n" + "=" * 60)
    print("🚀 Starting MSPaint MCP System...")
    print("=" * 60)
    
    # Start server in background thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # Wait a moment for server to start
    time.sleep(3)
    
    # Start agent
    session = start_agent()
    
    if session:
        print("\n" + "=" * 60)
        print("📊 Execution Summary:")
        print("=" * 60)
        print(f"🔧 Tools executed: {len(session.get('tool_execution', []))}")
        for i, tool_exec in enumerate(session.get('tool_execution', []), 1):
            tool_name = tool_exec.get('tool', 'unknown')
            status = tool_exec.get('response', {}).get('status', 'unknown')
            print(f"  {i}. {tool_name}: {status}")
        
        print(f"\n📝 Session saved to: llm_session.json")
        print(f"📝 Logs saved to: mcp_agent.log")
    
    print("\n🎉 Demo completed! Check MS Paint for results.")
    input("Press Enter to exit...")

if __name__ == '__main__':
    main()
