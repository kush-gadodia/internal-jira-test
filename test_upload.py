import requests

with open('agent_flow/mock_documents/mock_adhaar.png', 'rb') as f:
    files = {
        'file': ('mock_adhaar.png', f.read(), 'image/png')
    }

data = {
    'folder': 'identity',
}

try:
    response = requests.post("http://localhost:8000/api/upload", files=files, data=data)
    print("Status:", response.status_code)
    print("JSON:", response.json())
except Exception as e:
    print("Error:", e)
