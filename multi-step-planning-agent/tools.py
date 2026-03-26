def search_places(location):
    return f"Top places in {location}: Munnar, Alleppey, Kochi"

def get_weather(location):
    return f"Weather in {location}: 25°C, partly cloudy"

def estimate_budget(days):
    return f"Estimated budget for {days} days: ₹15,000"

#tool schema for LLM
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_places",
            "description": "Find popular places in a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather info",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "estimate_budget",
            "description": "Get budget estimate",
            "parameters": {
                "type": "object",
                "properties": {
                    "days": {"type": "string"}
                },
                "required": ["days"]
            }
        }
    }
]