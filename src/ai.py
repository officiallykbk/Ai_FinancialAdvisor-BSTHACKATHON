import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def Insight(message):
    try:
        client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=os.environ["HF_TOKEN"],
        )
        prompt = f"""
        You are a financial advisor. 
        Analyze this financial data and provide insights:
        
        {json.dumps(message, indent=2)}

            Provide clear, actionable insights and recommendations in 2-3 paragraphs. Focus on:
            1. Key financial health indicators
            2. Areas of concern
            3. Practical recommendations
            4. Long-term financial planning advice"""

        response = client.chat.completions.create(
            model="moonshotai/Kimi-K2-Thinking:novita",
            messages=[
                {"role": "system", "content": "You are a Genius financial advisor."},
                {"role": "user", "content": prompt}
            ],
        )
        
        if response.choices and len(response.choices) > 0:
            return {
                "status": "success",
                "insight": response.choices[0].message.content.strip()
            }
        else:
            return {
                "status": "error",
                "message": "No response from AI model"
            }
            
    except Exception as e:
        # Fallback response if the AI service is unavailable
        return {
            "status": "error",
            "message": f"AI service error: {str(e)}",
            "fallback_insight": {
                "observation": "Unable to generate AI insights due to service error.",
                "suggestion": "Please check your internet connection and API key."
            }
        }
