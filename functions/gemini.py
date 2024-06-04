import google.generativeai as genai


def gemini(message, GEMINI_API_KEY):
    google_api_key = GEMINI_API_KEY
    if not google_api_key:
        return "An error occurred: GEMINI_API_KEY is not set"

    genai.configure(api_key=google_api_key)
    model = genai.GenerativeModel('gemini-1.0-pro')

    try:
        print(f"Generating content for message: {message}")
        response = model.generate_content(message)

        if not hasattr(response, 'text'):
            return "An error occurred: The response object does not have a 'text' attribute"

        return response.text

    except Exception as e:
        print(f"Exception: {str(e)}")
        return f"An error occurred: {str(e)}"
