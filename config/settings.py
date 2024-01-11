SELENOID_IP = "127.0.0.1"

BROWSER_CAPABILITIES = {
    "browserName": "chrome",
    "browserVersion": "119.0",
    "goog:chromeOptions": {"args": [
        "--ignore-certificate-errors", 
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-gpu"
        ]},
    "selenoid:options": {
        "enableVNC": True,
        "screenResolution": "1280x1024x24",
        "name": "selenoid-example",
        "sessionTimeout": "1m",
        "timeZone": "America/Sao_Paulo",
        
        "labels": {
            "manual": "true"
        },
    
    }
}