from pyngrok import ngrok

# Start a tunnel to port 5000
public_url = ngrok.connect(5000)
print("🔗 ngrok tunnel URL:", public_url)

# Keep tunnel open
input("Press ENTER to exit\n")
