# 🛡️ 777-HashHarden 
**A Zero-Trust Asset Sanitization & Integrity Pipeline for 777heaven Records.**

> "Trust is a vulnerability. In the music industry, receiving 'Final' files from unknown sources is a security nightmare. This tool is the digital gatekeeper for our production vault."

---

## 🔍 Overview
**777-HashHarden** is a specialized security middleware developed to bridge the gap between untrusted artist submissions and secure label distribution. As a Cybersecurity student and founder of **777heaven Records**, I built this to automate the "cleansing" of music assets (MP3/WAV) before they touch our internal storage.

This project demonstrates the application of **Digital Forensics**, **Cryptographic Integrity**, and **Zero-Trust architecture** within a real-world business workflow.

---

## 🛠️ Key Technical Features

### 1. Forensic Signature Verification (Magic Bytes)
The engine ignores file extensions, which can be easily spoofed. Instead, it performs a deep header inspection to verify the file's "DNA":
* **WAV:** Detects the `RIFF` container signature.
* **MP3:** Detects the `ID3` or sync frame signature.
* *Outcome:* Prevents renamed malicious executables (`.exe`) from entering the pipeline.

### 2. Privacy Scrubbing (Metadata Forensics)
Music files often contain hidden "ghost data"—GPS coordinates, studio file paths, and private artist information. 
* **MP3:** Wipes ID3v1/v2 tags using `mutagen`.
* **WAV:** Strips RIFF metadata chunks.
* *Outcome:* Ensures 100% digital privacy for artists before their files reach third-party distributors.

### 3. SHA-256 Cryptographic Fingerprinting
Every sanitized asset is assigned a unique 12-character hexadecimal hash.
* *Outcome:* Provides an immutable "receipt" of the file's state. If a file is corrupted or tampered with during distribution, the hash mismatch will flag the error immediately.

### 4. Automated Audit Logging
All operations—successes and rejected threats—are logged with timestamps in a secure audit trail for forensic review.

---

## 🚀 Getting Started

### Prerequisites
* **OS:** Windows or Linux (**Aurora DX** / Fedora).
* **Language:** Python 3.8+
* **Library:** Mutagen

### Installation
```bash
# Clone the repository
git clone [https://github.com/AlasdairDev/777-HashHarden.git](https://github.com/AlasdairDev/777-HashHarden.git)

# Navigate to directory
cd 777-HashHarden

# Install dependencies
pip install mutagen