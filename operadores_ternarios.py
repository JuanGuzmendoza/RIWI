import requests
import json

def get_gemini_response(prompt):
    api_key = "AIzaSyCvtF5V6FLQpmhJnmln-jD0HMU3eqJ3qWI"  # Reemplaza con tu clave
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-thinking-exp-01-21:generateContent?key={api_key}"
    
    payload = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }],
        "generationConfig": {
            "temperature": 1,  # Aumentar la temperatura para mayor creatividad y sarcasmo
            "topP": 0.8,         # Ajustar topP para permitir más variedad
            "topK": 50,          # Aumentar topK para más opciones
            "maxOutputTokens": 8192
        }
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        json_response = response.json()
        
        if "candidates" in json_response and len(json_response["candidates"]) > 0:
            return json_response["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return "No se pudo obtener una respuesta."
    except Exception as e:
        return f"Error: {str(e)}"

# Ejemplo de uso
def test_gemini():
    pregunta = input("")
    respuesta = get_gemini_response(pregunta)
    print("Respuesta:", respuesta)

# Si ejecutas este archivo directamente
if __name__ == "__main__":
    test_gemini()