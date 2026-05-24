sessions_minutes = [2, 15, 240, 60, 3, 10, 7, 130, 90, 4, 55, 300]
sessions_longues = []
sessions_courtes = []

sessions_minutes.sort()
print("Duree la plus courte : ", sessions_minutes[0], "minutes")
print("Duree la plus longue : ", sessions_minutes[-1], "minutes")
print("Duree moyenne des sessions : ", round(sum(sessions_minutes)/len(sessions_minutes),2), "minutes")

for i in range(0,len(sessions_minutes)):
    if sessions_minutes[i] < 5:
       sessions_courtes.append(sessions_minutes[i])

sessions_courtes.sort()

for i in range(0,len(sessions_minutes)):
    if sessions_minutes[i] > 120:
       sessions_longues.append(sessions_minutes[i])

sessions_longues.sort(reverse=True)

print("Sessions trop courtes (<5 min) : ", sessions_courtes)
print("Sessions trop longues (>120 min) : ", sessions_longues)
