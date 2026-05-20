"""
Download required MediaPipe models
"""
import os
import urllib.request
import ssl

# Create models directory
os.makedirs("models", exist_ok=True)

# Disable SSL verification for downloading
ssl._create_default_https_context = ssl._create_unverified_context

# Model URL - try alternative sources
models = {
    "hand_landmarker": [
        "https://storage.googleapis.com/mediapipe-assets/hand_landmarker.task",
        "https://github.com/google-ai-edge/mediapipe/releases/download/v0.10.0/hand_landmarker.task",
    ]
}

for name, urls in models.items():
    model_path = f"models/{name}.task"
    
    if os.path.exists(model_path):
        # Check if it's valid
        with open(model_path, 'r') as f:
            content = f.read()
            if '<Error>' in content or 'xml' in content.lower():
                print(f"✗ Model {name} is corrupted (XML error), re-downloading...")
                os.remove(model_path)
            else:
                print(f"✓ Model {name} already exists")
                continue
    
    downloaded = False
    for url in urls:
        print(f"Trying to download {name} from {url}...")
        try:
            urllib.request.urlretrieve(url, model_path)
            print(f"✓ Downloaded {name}")
            downloaded = True
            break
        except Exception as e:
            print(f"  Failed: {e}")
    
    if not downloaded:
        print(f"✗ Could not download {name} from any source")
