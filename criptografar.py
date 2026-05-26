#!/usr/bin/env python3
import sys, os, json, hashlib, base64

# CHAVE SECRETA DO APP (mesma que está no SMALI)
SECRET_KEY = b"StreamFlix_Protecao_2026_v1"

# Chave XOR para criptografia
K = bytes([0x13, 0x37, 0x42, 0x69, 0x0A, 0x1B, 0x2C, 0x3D])

def xor(data):
    return bytes([b ^ K[i % len(K)] for i, b in enumerate(data)])

if len(sys.argv) < 2:
    print("Uso: python3 criptografar.py arquivo.json")
    sys.exit(1)

with open(sys.argv[1], "rb") as f:
    data = f.read()

# Calcular HMAC-SHA256 do payload original
hmac = hashlib.sha256(SECRET_KEY + data).digest().hex()

# Parse JSON e embutir checksum
payload = json.loads(data.decode('utf-8'))
payload["_integrity"] = hmac

# Converter de volta para bytes
final_data = json.dumps(payload, separators=(',', ':')).encode('utf-8')

# Criptografar
enc = xor(final_data)

with open("ghost.payload", "wb") as f:
    f.write(enc)

print(f"[OK] ghost.payload ({len(enc)} bytes)")
print(f"[HMAC] {hmac}")
print("[!] Faca upload no GitHub!")
