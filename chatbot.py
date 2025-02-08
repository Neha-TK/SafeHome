import google.generativeai as genai

# Replace with your actual API key
API_KEY = "AIzaSyAk1H9fJqhGEy8E60qsrRoDH1bWntygkYI"

# Configure API key
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel("gemini-pro")

def generate_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Example Usage
if __name__ == "__main__":
    user_input = input("Enter your question: ")
    ai_response = generate_response(user_input)
    print("\nGemini Response:", ai_response)
