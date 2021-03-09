# 1.
F = 50 # N
s = 300 # m
# W = ?
# ------------------------
W = F * s
print("1. feladat: W =", W, "Joule" )

# 2.
F = 350 # N
s = 2 # m
# W = ?
# ------------------------
W = F * s
print("2. feladtat: W =", W, "Joule" )

#3.
F = 1000 # N
s = 5000 # m
# W = ?
# -------------------------
W = F * s
print("3. feladat : W=", W, "Joule")

#4.
m = 5 # kg
h = 2 # m
# W = ?
#---------------------------
# F = m * a         F = m * g
g = 9.81 # m/(s*s)
F = m * g
W = m * g * h
W = round(W, 2)
print("4. feladat : W=", W, " Joule")

# 8.
W = 300e6 # Joule
s = 2000 #m
# F = ?
#-------------------------
# W = F * s            /: s
# W / s = F
F = W / s
print("8. feladat: F=", F, "N")

# 9.
m = 25 # kg
s = 60 # m
u = 0.2
# W = ?
#---------------------------------

# súly = tömeg * gravitációs gyorsulás
G = m * 9.81
Fsurlodasi = -G * u
F = -Fsurlodasi
W = F * s
print("9. feladat: W =", W, "Joule" )