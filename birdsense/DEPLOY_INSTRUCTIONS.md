# 🚀 BirdSense Deployment Instructions

## Quick Local Test (Running Now!)

Your BirdSense app is running locally at:
```
🌐 http://localhost:7860
```

Open this URL in your browser to test the app!

---

## Deploy to HuggingFace Spaces (5 minutes)

### Step 1: Get HuggingFace Token

1. Go to: **https://huggingface.co/settings/tokens**
2. Login with: `you@example.com` / ``
3. Click **"Create new token"**
4. Settings:
   - Name: `birdsense-deploy`
   - Type: `Write`
5. Click **"Create token"**
6. **Copy the token** (starts with `hf_...`)

### Step 2: Deploy

```bash
cd /Users/soham.niyogi/Soham/codebase/eagv2/birdsense
source venv/bin/activate
python deploy_to_hf.py --token YOUR_HF_TOKEN
```

Replace `YOUR_HF_TOKEN` with the token you copied.

### Step 3: Share!

After deployment, your app will be live at:
```
https://huggingface.co/spaces/YOUR_USERNAME/birdsense
```

---

## Alternative: Manual Upload

1. Go to: **https://huggingface.co/new-space**
2. Fill in:
   - Space name: `birdsense`
   - SDK: `Gradio`
   - License: `MIT`
3. Click **"Create space"**
4. Upload these files from `/Users/soham.niyogi/Soham/codebase/eagv2/birdsense/birdsense-space/`:
   - `app.py`
   - `requirements.txt`
   - `README.md`
5. Your space will automatically build and deploy!

---

## Files to Deploy

```
birdsense-space/
├── app.py              # Main Gradio app (REQUIRED)
├── requirements.txt    # Python dependencies (REQUIRED)
└── README.md           # Space metadata & description
```

---

## What's Included

✅ **SAM-Audio Style Preprocessing** - Bird frequency isolation (500-10000 Hz)
✅ **15 Indian Bird Species** - Knowledge base for identification
✅ **Audio Feature Analysis** - Frequency, syllables, patterns
✅ **Beautiful UI** - Dark theme, responsive design
✅ **Recording & Upload** - Record directly or upload files

---

## Support

For help, create an issue at:
https://github.com/sohamniyogi/eagv2/issues

