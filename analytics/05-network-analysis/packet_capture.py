import numpy as np

# Data representing suspicious network packet sizes
paquets = np.array([120, 85, 300, 150, 90, 450, 200, 175, 500, 130, 95, 400])

print(f"Suspicious Packet Array:\n{paquets}")
print("="*5, "Statistics", "="*5)
print(f"Total: {np.sum(paquets)}")
print(f"Mean: {np.mean(paquets):.2f}")
print(f"Maximum: {np.max(paquets)}")
print(f"Minimum: {np.min(paquets)}")
print(f"Standard Deviation: {np.std(paquets):.2f}")

# Anomaly Detection
threshold = 250
if np.any(paquets > threshold):
    print(f"⚠️ Abnormal network activity detected.")
    print(f"Packets exceeding {threshold}: {paquets[paquets > threshold]}")
else:
    print("✅ Network activity stable.")

# Data Reduction
reduction = paquets - (paquets * 0.15)
print(f"\nArray after 15% reduction:\n{reduction}")
print(f"Array sorted descending:\n{np.sort(reduction)[::-1]}")

print("\n" + "="*5, "Traffic Analysis", "="*5)
for paquet in paquets:
    if paquet < 150:
        print(f"{paquet}: ✅ Low Traffic")
    elif 150 <= paquet <= 300:
        print(f"{paquet}: ⚠️ Medium Traffic")
    else:  # paquet > 300
        print(f"{paquet}: 🚨 High Traffic")
