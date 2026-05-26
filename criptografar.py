#!/usr/bin/env python3
import sys, os

K = bytes([0x13, 0x37, 0x42, 0x69, 0x0A, 0x1B, 0x2C, 0x3D])

def xor(data):
    return bytes([b ^ K[i % len(K)] for i, b in enumerate(data)])

if len(sys.argv) < 2:
    print("Uso: python3 criptografar.py arquivo.json")
    sys.exit(1)

with open(sys.argv[1], "rb") as f:
    data = f.read()

enc = xor(data)
with open("ghost.payload", "wb") as f:
    f.write(enc)

print(f"[OK] ghost.payload ({len(enc)} bytes)")
print("[!] Faca upload no GitHub!")
