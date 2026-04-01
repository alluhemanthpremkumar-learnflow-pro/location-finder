<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>premlocationfinder</title>
    <style>
        body { font-family: sans-serif; text-align: center; padding-top: 50px; }
        .loc-btn { cursor: pointer; border: 2px solid #ddd; padding: 10px; border-radius: 8px; }
    </style>
</head>
<body>
    <h2>Click the image to share location</h2>
    <div class="loc-btn" onclick="getLocation()">
        <img src="https://via.placeholder.com/300x150?text=Click+to+Share+Location" alt="Share Location">
    </div>
    <p id="status"></p>

    <script>
        function getLocation() {
            const status = document.getElementById("status");
            if (navigator.geolocation) {
                status.innerHTML = "Requesting permission...";
                navigator.geolocation.getCurrentPosition(
                    (position) => {
                        const lat = position.coords.latitude;
                        const lon = position.coords.longitude;
                        // Redirect to the /data route with parameters
                        window.location.href = `/data?lat=${lat}&lon=${lon}`;
                    },
                    (error) => {
                        status.innerHTML = "Error: " + error.message;
                    }
                );
            } else { 
                status.innerHTML = "Geolocation is not supported by this browser."; 
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/data')
def get_data():
    # Retrieving data passed via URL parameters
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat and lon:
        return f"""
        <div style="text-align:center; margin-top:50px;">
            <h1>Location Received</h1>
            <p><strong>Latitude:</strong> {lat}</p>
            <p><strong>Longitude:</strong> {lon}</p>
            <a href="/">Back</a>
        </div>
        """
    return "No location data received.", 400

if __name__ == '__main__':
    # Set host to '0.0.0.0' to make it accessible on your local network
    app.run(debug=True, host='0.0.0.0', port=5000)