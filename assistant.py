# assistant.py – She Safe GBV AI Assistant
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
# The newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# Do not change this unless explicitly requested by the user
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are She Safe, an AI chatbot that helps users facing Gender-Based Violence (GBV).
Your role is to:
- Assess the situation safely and anonymously.
- Identify the type of GBV: physical, emotional, sexual, digital, economic, or other.
- Provide actionable guidance: emergency contacts, shelters, hotlines, legal aid.
- Suggest safety plans and coping strategies.
- Share awareness tips: consent, rights, healthy relationships.
- Offer mental health support: breathing exercises, survivor stories.
- Always be empathetic, concise, and privacy-focused.
- If someone is in immediate danger, prioritize directing them to emergency services.
- Respect confidentiality and never judge or blame the survivor.
- Provide culturally sensitive advice for users in Ethiopia and Cameroon.
"""

def get_response(user_input):
    """
    Get AI response from OpenAI for GBV support
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # The newest OpenAI model
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"I apologize, but I'm experiencing technical difficulties right now. Please try again later or contact emergency services if you're in immediate danger. Error: {str(e)}"

def get_safety_tips():
    """
    Provide general safety tips for GBV survivors
    """
    return """
    **General Safety Tips:**
    
    🛡️ **Personal Safety:**
    - Trust your instincts - if something feels wrong, it probably is
    - Keep important documents in a safe, accessible place
    - Have an emergency bag ready with essentials
    - Identify safe places you can go quickly if needed
    
    📱 **Digital Safety:**
    - Use privacy settings on social media
    - Change passwords regularly
    - Be cautious about sharing location information
    - Consider using a different device for seeking help
    
    🤝 **Building Support:**
    - Identify trusted friends, family, or colleagues
    - Connect with local support organizations
    - Consider joining support groups
    - Remember: seeking help is a sign of strength, not weakness
    
    ⚠️ **If in immediate danger, contact local emergency services immediately.**
    """

def get_coping_strategies():
    """
    Provide mental health coping strategies
    """
    return """
    **Coping Strategies for Mental Health:**
    
    🧘 **Grounding Techniques:**
    - 5-4-3-2-1 method: Name 5 things you see, 4 you can touch, 3 you hear, 2 you smell, 1 you taste
    - Deep breathing: Inhale for 4 counts, hold for 4, exhale for 6
    - Progressive muscle relaxation
    
    💝 **Self-Care Practices:**
    - Maintain a daily routine when possible
    - Engage in activities that bring you joy
    - Practice self-compassion - you are not to blame
    - Journal your thoughts and feelings
    
    🌱 **Building Resilience:**
    - Focus on what you can control
    - Set small, achievable goals
    - Celebrate small victories
    - Remember that healing is not linear
    
    💪 **Remember:** You are stronger than you know, and you deserve support and safety.
    """
