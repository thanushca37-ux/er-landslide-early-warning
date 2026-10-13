import uvicorn
import os
import sys

if __name__ == "__main__":
    print("=" * 70)
    print("🏔️  NER-LandslideWatch: AI-Powered Early Warning & Monitoring Platform")
    print("    Focused on North Eastern Region (NER) fragile hill terrain")
    print("    URL: http://127.0.0.1:8000")
    print("    Docs: http://127.0.0.1:8000/docs")
    print("=" * 70)
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
