import os
import hashlib
import logging
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.wave import WAVE  

os.makedirs('logs', exist_ok=True)
os.makedirs('untrusted', exist_ok=True)
os.makedirs('vault', exist_ok=True)

logging.basicConfig(
    filename='logs/security_audit.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

class HashHarden:
    def __init__(self):
        self.signatures = {
            b'ID3': '.mp3',
            b'RIFF': '.wav'
        }

    def verify_signature(self, file_path):
        """Forensic Check: Does the file header match the extension?"""
        with open(file_path, 'rb') as f:
            header = f.read(4)
            for sig, ext in self.signatures.items():
                if header.startswith(sig):
                    return ext
        return None

    def generate_hash(self, file_path):
        """SHA-256 Hashing: Optimized for large WAV files."""
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(8192): 
                sha256.update(chunk)
        return sha256.hexdigest()[:12]

    def harden_asset(self, filename):
        input_path = os.path.join("untrusted", filename)
        
        detected_ext = self.verify_signature(input_path)
        if not detected_ext or not filename.lower().endswith(detected_ext):
            logging.error(f"SPOOF ALERT: {filename} failed signature verification.")
            return False

        try:
            artist_tag = "777_Artist"
            
            if detected_ext == '.mp3':
                audio = MP3(input_path, ID3=EasyID3)
                artist_tag = str(audio.get('artist', ['Unknown'])[0])
                audio.delete() # Wipe tags
                audio.save()
            elif detected_ext == '.wav':
                audio = WAVE(input_path)
                audio.delete()
                audio.save()

            fingerprint = self.generate_hash(input_path)
            clean_artist = artist_tag.replace(" ", "_")
            new_name = f"777_{clean_artist}_{fingerprint}{detected_ext}"
            
            os.rename(input_path, os.path.join("vault", new_name))
            logging.info(f"VAULTED: {filename} as {new_name}")
            return new_name

        except Exception as e:
            logging.error(f"CRITICAL ERROR: {filename} - {e}")
            return None


if __name__ == "__main__":
    guard = HashHarden()
    print("🛡️  777-HashHarden: Distribution Security Unit")
    print("-" * 50)
    
    queue = [f for f in os.listdir("untrusted") if f.lower().endswith((".mp3", ".wav"))]
    
    if not queue:
        print("💡 Status: Vault is empty. Drop .wav or .mp3 files in 'untrusted/'.")
    else:
        for file in queue:
            result = guard.harden_asset(file)
            if result:
                print(f"✅ SUCCESS: {result} is Distribution-Ready.")
            else:
                print(f"🚨 BLOCKED: {file} failed security audit.")
    
    print("-" * 50)