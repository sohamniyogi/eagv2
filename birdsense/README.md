# 🐦 BirdSense - AI Bird Identification System

**Developed by Soham**

A novel hybrid AI system for intelligent bird identification using audio, images, and descriptions. BirdSense combines cutting-edge deep learning with traditional ornithological knowledge to deliver accurate species identification.

---

## 🌟 Key Features

| Feature | Description |
|---------|-------------|
| **🎵 Audio Identification** | META SAM-Audio + BirdNET hybrid with multi-bird detection |
| **📷 Image Identification** | Vision AI with feature-based analysis |
| **📝 Description Matching** | Natural language bird identification |
| **🇮🇳 India-Specific Info** | Local names, habitats, birding spots |
| **🔄 Multi-Backend Support** | Ollama (local) or Azure OpenAI (cloud) |
| **📊 Streaming Results** | Real-time analysis trail with accordion view |

---

## 🏗️ Novel Hybrid Architecture

BirdSense introduces a **novel multi-stage hybrid architecture** that combines specialized ML models with large language models for superior accuracy.

### Audio Identification Pipeline

```
┌─────────────────────────────────────────────────────────────────────┐
│                    BIRDSENSE AUDIO PIPELINE                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  AUDIO INPUT                                                        │
│       │                                                             │
│       ▼                                                             │
│  ┌─────────────────────────────────────┐                           │
│  │  STAGE 1: META SAM-Audio            │                           │
│  │  ├── Noise filtering                │                           │
│  │  ├── Bird call segmentation         │                           │
│  │  └── Frequency band separation:     │                           │
│  │      • Very Low (100-500 Hz) - Owls │                           │
│  │      • Low (500-1500 Hz) - Crows    │                           │
│  │      • Medium (1500-3000 Hz) - Mynas│                           │
│  │      • High (3000-6000 Hz) - Finches│                           │
│  │      • Very High (6000+ Hz)         │                           │
│  └─────────────────────────────────────┘                           │
│       │                                                             │
│       ▼                                                             │
│  ┌─────────────────────────────────────┐                           │
│  │  STAGE 2: BirdNET (Cornell Lab)     │                           │
│  │  ├── Spectrogram analysis           │                           │
│  │  ├── 6000+ species recognition      │                           │
│  │  └── Multi-pass analysis:           │                           │
│  │      • Full audio analysis          │                           │
│  │      • Per-frequency-band analysis  │                           │
│  └─────────────────────────────────────┘                           │
│       │                                                             │
│       ▼                                                             │
│  ┌─────────────────────────────────────┐                           │
│  │  STAGE 3: Feature Extraction        │                           │
│  │  ├── Frequency range analysis       │                           │
│  │  ├── Pattern detection              │                           │
│  │  ├── Syllable counting              │                           │
│  │  └── Rhythm classification          │                           │
│  └─────────────────────────────────────┘                           │
│       │                                                             │
│       ▼                                                             │
│  ┌─────────────────────────────────────┐                           │
│  │  STAGE 4: LLM Validation Layer      │                           │
│  │  ├── Contextual reasoning           │                           │
│  │  ├── Location/season validation     │                           │
│  │  └── Confidence adjustment          │                           │
│  └─────────────────────────────────────┘                           │
│       │                                                             │
│       ▼                                                             │
│  IDENTIFIED BIRDS (with enriched info)                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Image Identification Pipeline

```
┌─────────────────────────────────────────────────────────────────────┐
│                    BIRDSENSE IMAGE PIPELINE                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  IMAGE INPUT                                                        │
│       │                                                             │
│       ▼                                                             │
│  ┌─────────────────────────────────────┐                           │
│  │  Vision Model (LLaVA/GPT-4o)        │                           │
│  │  ├── Systematic feature analysis:   │                           │
│  │  │   • BEAK: Color, shape           │                           │
│  │  │   • HEAD: Crown, eye pattern     │                           │
│  │  │   • BODY: Plumage, breast        │                           │
│  │  │   • SIZE: Relative sizing        │                           │
│  │  └── Multi-bird detection           │                           │
│  └─────────────────────────────────────┘                           │
│       │                                                             │
│       ▼                                                             │
│  ┌─────────────────────────────────────┐                           │
│  │  Enrichment Layer                   │                           │
│  │  ├── Wikipedia image fetch          │                           │
│  │  ├── Species information            │                           │
│  │  ├── Habitat & diet data            │                           │
│  │  └── India-specific info            │                           │
│  └─────────────────────────────────────┘                           │
│       │                                                             │
│       ▼                                                             │
│  IDENTIFIED BIRDS (with images & facts)                            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
birdsense/
├── app.py              # Gradio UI (clean, minimal)
├── providers.py        # LLM Provider Factory Pattern
├── analysis.py         # Bird Identification Logic
├── prompts.py          # Model-specific prompts
├── confusion_rules.py  # Feature validation hints
├── feedback.py         # User feedback collection
├── requirements.txt    # Python dependencies
├── Dockerfile          # Cloud deployment
├── .env               # Local configuration (gitignored)
│
├── api/               # REST API (FastAPI)
│   ├── main.py        # API server entry point
│   ├── routes/        # API endpoints
│   │   ├── auth_routes.py      # JWT authentication
│   │   └── identify_routes.py  # Bird identification
│   ├── auth/          # JWT handler
│   └── models/        # Pydantic schemas
│
└── mobile/            # React Native Expo App
    ├── app/           # Expo Router screens
    │   ├── (tabs)/    # Tab navigation
    │   └── login.tsx  # Authentication
    └── src/
        ├── services/  # API client
        ├── context/   # Auth context
        └── components/# Reusable UI
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.12
- Ollama (for local models)
- Docker (for cloud deployment)

### Local Development

#### 1. Clone and Setup

```bash
cd birdsense

# Create virtual environment
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### 2. Install Ollama Models (Local Backend)

```bash
# Install Ollama from https://ollama.ai
ollama pull llava:7b      # Vision model
ollama pull phi4:latest   # Text model
```

#### 3. Configure Environment

```bash
# Copy template
cp env-template.txt .env

# Edit .env with your settings:
# Option A: Use Ollama (local) - no API key needed
# Option B: Use Azure OpenAI - add your credentials
```

**Example `.env` for Azure OpenAI:**
```env
IS_AZURE=true
LITELLM_API_KEY=your-azure-api-key
LITELLM_API_BASE=https://your-resource.azure-api.net/your-endpoint
AZURE_DEPLOYMENT=your-deployment-name
AZURE_API_VERSION=2024-02-15-preview
LITELLM_VISION_MODEL=gpt-4o
LITELLM_TEXT_MODEL=gpt-4o
```

#### 4. Run Locally

```bash
python app.py
```

Open **http://localhost:7860** in your browser.

---

## 🔌 REST API

BirdSense includes a FastAPI-based REST API for programmatic access.

### Run API Server

```bash
cd birdsense
source venv/bin/activate
uvicorn api.main:app --reload --port 8000
```

**Swagger UI**: http://localhost:8000/docs  
**ReDoc**: http://localhost:8000/redoc

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/auth/login` | Get JWT token |
| `GET` | `/auth/me` | Get current user |
| `POST` | `/identify/audio` | Upload audio file |
| `POST` | `/identify/audio/base64` | Base64 audio |
| `POST` | `/identify/image` | Upload image file |
| `POST` | `/identify/image/base64` | Base64 image |
| `POST` | `/identify/description` | Text description |

### Authentication

Default users:

| Username | Password |
|----------|----------|
| `admin` | `` |
| `demo` | `` |
| `soham` | `` |

### Postman Collection

Import `api/BirdSense_API.postman_collection.json` into Postman for ready-to-use requests.

---

## 📱 Mobile App (React Native)

A cross-platform mobile app built with Expo.

### Run Mobile App

```bash
cd birdsense/mobile

# Install dependencies
npm install

# Start Expo
npm start

# Scan QR code with Expo Go app
```

### Features

- 🎵 **Audio Recording** - Record and identify bird calls
- 📷 **Camera/Gallery** - Take or select bird photos
- 📝 **Description** - Text-based identification
- 🔐 **Authentication** - JWT-based login

### Configure API URL

Edit `mobile/src/services/api.ts`:

```typescript
const API_CONFIG = {
  BASE_URL: 'https://your-deployed-api.run.app',
};
```

---

## ☁️ Cloud Deployment

### Deploy to Google Cloud Run

#### 1. Build Docker Image

```bash
# Build for linux/amd64 (Cloud Run requirement)
docker buildx build --platform linux/amd64 -t your-dockerhub/birdsense:latest --push .
```

#### 2. Deploy to Cloud Run

```bash
gcloud run deploy birdsense \
  --image docker.io/your-dockerhub/birdsense:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 2Gi \
  --cpu 2 \
  --timeout 300 \
  --set-env-vars "IS_AZURE=true" \
  --set-env-vars "LITELLM_API_KEY=your-api-key" \
  --set-env-vars "LITELLM_API_BASE=https://your-endpoint" \
  --set-env-vars "AZURE_DEPLOYMENT=your-deployment" \
  --set-env-vars "AZURE_API_VERSION=2024-02-15-preview" \
  --set-env-vars "LITELLM_VISION_MODEL=gpt-4o" \
  --set-env-vars "LITELLM_TEXT_MODEL=gpt-4o" \
  --port 7860
```

#### 3. Verify Deployment

```bash
# Get service URL
gcloud run services describe birdsense --region us-central1 --format 'value(status.url)'

# Test
curl https://your-service-url.run.app
```

### Deploy with Docker Compose (Self-hosted)

```yaml
# docker-compose.yml
version: '3.8'
services:
  birdsense:
    image: your-dockerhub/birdsense:latest
    ports:
      - "7860:7860"
    environment:
      - IS_AZURE=true
      - LITELLM_API_KEY=${LITELLM_API_KEY}
      - LITELLM_API_BASE=${LITELLM_API_BASE}
      - AZURE_DEPLOYMENT=${AZURE_DEPLOYMENT}
    restart: unless-stopped
```

```bash
docker-compose up -d
```

---

## 🔧 Backend Configuration

### Option 1: Ollama (Local - Free)

Best for development and privacy-conscious deployments.

| Model | Purpose | Size |
|-------|---------|------|
| LLaVA 7B | Vision | ~4GB |
| phi4 14B | Text/Reasoning | ~8GB |

**Quality**: ⭐⭐⭐⭐ (Good)

### Option 2: Azure OpenAI (Enterprise)

Best for production with enterprise security.

| Model | Purpose |
|-------|---------|
| GPT-4o | Vision + Text |

**Quality**: ⭐⭐⭐⭐⭐ (Excellent)

### Option 3: OpenAI Public API

Best for quick cloud deployment.

```env
IS_AZURE=false
LITELLM_API_KEY=sk-your-openai-key
LITELLM_API_BASE=https://api.openai.com
LITELLM_VISION_MODEL=gpt-4o
LITELLM_TEXT_MODEL=gpt-4o
```

---

## 🎯 API Endpoints

BirdSense uses Gradio's built-in API. Access programmatically:

```python
from gradio_client import Client

client = Client("https://your-birdsense-url")

# Image identification
result = client.predict(
    image="path/to/bird.jpg",
    location="Mumbai, India",
    api_name="/identify_image"
)

# Audio identification  
result = client.predict(
    audio="path/to/bird_call.wav",
    location="Kerala, India",
    month="March",
    api_name="/identify_audio"
)
```

---

## 📊 Technical Stack

| Component | Technology |
|-----------|------------|
| **Web UI** | Gradio 4.x |
| **REST API** | FastAPI + Uvicorn |
| **Mobile App** | React Native (Expo) |
| **Audio Analysis** | BirdNET (TensorFlow), scipy, librosa |
| **Vision Models** | LLaVA 7B, GPT-4o |
| **Text Models** | phi4 14B, GPT-4o |
| **Authentication** | JWT (python-jose, passlib) |
| **Image Sources** | Wikipedia, Wikimedia Commons, iNaturalist |
| **Containerization** | Docker |
| **Cloud Platform** | Google Cloud Run |

---

## 🧪 Testing

### Test Audio Multi-Bird Detection

```python
# Verify SAM-Audio + BirdNET pipeline
from analysis import identify_audio_streaming
import numpy as np

# Generate test audio or load from file
# The pipeline will:
# 1. Separate frequency bands
# 2. Run BirdNET on each band
# 3. Deduplicate and merge results
```

### Test Image Identification

```python
from analysis import fetch_bird_image

# Verify image fetching uses scientific name
url = fetch_bird_image("Great Tit", "Parus major")
print(f"Image URL: {url}")  # Should return Wikipedia image
```

---

## 🔄 Recent Updates

### v6.0 (Latest)
- ✅ **REST API** - FastAPI endpoints with Swagger docs
- ✅ **Mobile App** - React Native Expo app
- ✅ **JWT Authentication** - Secure API access
- ✅ **Postman Collection** - Ready-to-use API tests

### v5.0
- ✅ **Multi-bird audio detection** via SAM-Audio frequency separation
- ✅ **Fixed bird image fetching** using scientific names
- ✅ **India-specific information** always included
- ✅ **Accordion UI** for multiple results
- ✅ **Refactored architecture** with Factory Pattern
- ✅ **Azure OpenAI support** for enterprise deployment

### Architecture
- `providers.py` - Clean LLM backend abstraction
- `analysis.py` - Separated identification logic
- `prompts.py` - Externalized all LLM prompts
- `api/` - REST API with Factory Pattern
- `mobile/` - Cross-platform mobile app

---

## 🙏 Acknowledgments

- **Cornell Lab of Ornithology** - BirdNET model
- **Meta AI** - LLaVA vision-language model
- **OpenAI / Microsoft** - GPT-4o models
- **Ollama** - Local model serving
- **Wikipedia / iNaturalist** - Bird images and data

---

**🐦 BirdSense** - *Bringing AI to Bird Identification*

*Developed by Soham*
