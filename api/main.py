from fastapi.responses import JSONResponse
from fastapi import FastAPI
from app.metrics import get_system_metrics
from app.chatbot import create_chatbot
import logging
from app.openai import create_openai_chatbot

app = FastAPI()

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

@app.get("/chatbot")
async def chatbot_interaction():
    try:
        # # Step 1: Collect system metrics
        # metrics = get_system_metrics()

        # # Step 2: Prepare the input for the chatbot
        # recommendations_input = f"Here are the current system metrics: {metrics}. How can I optimize the system?"
        # logging.debug(f"Recommendations Input: {recommendations_input}")

        # # Step 3: Generate chatbot response
        # chain = create_chatbot(recommendations_input)
        # raw_response = chain.invoke({"recommendations": recommendations_input})
        # logging.debug(f"Raw response: {raw_response}")

        # # Step 4: Convert raw response to string
        # if hasattr(raw_response, "to_string"):  # For LangChain StringPromptValue
        #     response = raw_response.to_string()
        # elif isinstance(raw_response, str):
        #     response = raw_response
        # else:
        #     response = str(raw_response)

        # # Step 5: Return JSON response
        # return JSONResponse(content={
        #     "metrics": metrics,
        #     "chatbot_response": response
        # })
        response = create_openai_chatbot()
        return response

    except Exception as e:
        logging.exception("Error in /chatbot endpoint")
        return JSONResponse(content={"error": str(e)}, status_code=500)
