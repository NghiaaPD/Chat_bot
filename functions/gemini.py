import google.generativeai as genai
import time


def gemini(message, GEMINI_API_KEY):
    google_api_key = GEMINI_API_KEY
    if not google_api_key:
        yield "An error occurred: GEMINI_API_KEY is not set"
        return

    genai.configure(api_key=google_api_key)
    model = genai.GenerativeModel('gemini-1.0-pro')

    try:
        print(f"Generating content for message: {message}")  # Debugging: Check message
        response = model.generate_content(message, stream=True)
        response.resolve()

        if not hasattr(response, 'text'):
            yield "An error occurred: The response object does not have a 'text' attribute"
            return

        generated_text = response.text
        print(generated_text)
        for word in generated_text.split():
            yield word + " "
            time.sleep(0.05)

    except Exception as e:
        print(f"Exception: {str(e)}")
        yield f"An error occurred: {str(e)}"
