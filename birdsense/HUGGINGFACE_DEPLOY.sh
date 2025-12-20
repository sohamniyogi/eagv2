#!/bin/bash
# BirdSense HuggingFace Spaces Deployment Script
# Run this script to deploy to HuggingFace Spaces

echo "🐦 BirdSense HuggingFace Deployment"
echo "=================================="

# Check if huggingface-cli is installed
if ! command -v huggingface-cli &> /dev/null; then
    echo "Installing huggingface_hub..."
    pip install huggingface_hub
fi

# Login
echo ""
echo "📝 Logging into HuggingFace..."
echo "Use your credentials: you@example.com / [your_password]"
huggingface-cli login

# Create space directory
SPACE_DIR="birdsense-space"
echo ""
echo "📁 Preparing deployment files in $SPACE_DIR..."

mkdir -p $SPACE_DIR

# Copy necessary files
cp app.py $SPACE_DIR/
cp requirements.txt $SPACE_DIR/
cp -r audio $SPACE_DIR/
cp -r llm $SPACE_DIR/
cp -r data $SPACE_DIR/
cp -r models $SPACE_DIR/

# Create README for the Space
cat > $SPACE_DIR/README.md << 'EOF'
---
title: BirdSense
emoji: 🐦
colorFrom: green
colorTo: blue
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
license: mit
---

# 🐦 BirdSense - Zero-Shot Bird Identification

Intelligent bird recognition using LLM-based zero-shot identification.

## Features
- 🎯 **10,000+ Species**: Identify any bird worldwide
- 🚫 **No Training Required**: Zero-shot LLM identification
- 🇮🇳 **India Focus**: Special attention to Indian birds
- 🌍 **Novelty Detection**: Alerts for unusual sightings
- 📊 **Detailed Analysis**: Confidence scores with reasoning

## How to Use
1. Record audio using your microphone or upload a file
2. Add optional location and time context
3. Click "Identify Bird" to get results

## Technology
- **LLM**: Ollama with qwen2.5:3b
- **Audio Analysis**: librosa + scipy
- **Framework**: Gradio

## CSCR Initiative
Part of the Citizen Science for Conservation Research initiative.
EOF

# Create requirements for Space
cat > $SPACE_DIR/requirements.txt << 'EOF'
gradio>=4.0.0
torch>=2.0.0
torchaudio>=2.0.0
numpy>=1.24.0
scipy>=1.11.0
librosa>=0.10.1
soundfile>=0.12.1
ollama>=0.1.0
nest_asyncio>=1.5.0
httpx>=0.24.0
EOF

echo ""
echo "✅ Files prepared!"
echo ""
echo "📤 To deploy, run:"
echo "   cd $SPACE_DIR"
echo "   huggingface-cli repo create birdsense --type space --space_sdk gradio"
echo "   git init"
echo "   git add ."
echo "   git commit -m 'Initial BirdSense deployment'"
echo "   git remote add origin https://huggingface.co/spaces/YOUR_USERNAME/birdsense"
echo "   git push -u origin main"
echo ""
echo "🌐 Your app will be live at: https://huggingface.co/spaces/YOUR_USERNAME/birdsense"

