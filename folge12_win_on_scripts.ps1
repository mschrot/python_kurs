# Policy dauerhaft ändern (für deinen Benutzer)
# ✅ Lokale Skripte dürfen ausgeführt werden
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser


# 🔒 Vorteil: Gilt nur für dieses PowerShell-Fenster. Beim Schließen ist alles wie vorher.
#Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
