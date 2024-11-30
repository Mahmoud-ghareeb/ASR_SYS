import os
import openai
import yaml


class LLMService:

    def __init__(self):
        self.tools = [
                {
                    "type": "function",
                    "function": {
                        "name": "get_analysis_of_a_transcript",
                        "description": "Perform sentiment analysis, extract product-related topics, categorize them, and summarize the transcript",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "analysis": {
                                    "type": "object",
                                    "description": "Contains 4 keys for sentiment analysis, topic extraction, named entity recognition, and summarization",
                                    "properties": {
                                        "sentiment_analysis": {
                                            "type": "string",
                                            "description": "The sentiment analysis result of the transcript",
                                            "enum": [
                                                    "positive",
                                                    "negative",
                                                    "neutral"
                                                ],
                                        },
                                        "topic_extraction_categorization": {
                                            "type": "array",
                                            "description": "List of product-related topics categorized into structured topics such as 'Network Issues', 'Billing', 'Customer Service', etc.",
                                            "items": {
                                                "type": "string"
                                            }
                                        },
                                        "named_entity_recognition": {
                                            "type": "object",
                                            "description": "Contains identified named entities in the transcript, where the key is the entity and the value is an array of occurrences of that entity",
                                            "properties": {
                                                "product_names": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "company_names": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "technical_names": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "customer_names": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                }
                                            }

                                        },
                                        "summarization": {
                                            "type": "string",
                                            "description": "A concise summary of the key points from the transcript"
                                        }
                                    },
                                    "required": [
                                        "sentiment_analysis",
                                        "topic_extraction_categorization",
                                        "named_entity_recognition",
                                        "summarization"
                                    ]
                                }
                            }
                        }
                    }
                }
            ]

        self.sambanova_api_key = os.environ.get("SAMBANOVA_API_KEY")
        self.open_ai_api_key = os.environ.get("OPENAI_API_KEY")
        self.initial_prompt = self.get_prompt()


    def get_prompt(self):
        """
        Get The Initial Prompt From yaml File
        """
        
        with open('configs/config.yaml', 'r') as file:
            return yaml.load(file, Loader=yaml.FullLoader)["prompts"]["initial_propmt"]


    def get_sambanova_response(self, message):
        """
        Function to use sembanova cloud API
        """

        client = openai.OpenAI(
            api_key=self.sambanova_api_key,
            base_url="https://api.sambanova.ai/v1",
        )
        
        response = client.chat.completions.create(
            model='Meta-Llama-3.1-8B-Instruct',
            messages=[
                    {"role":"system","content": self.initial_prompt },
                    {"role":"user","content": message}
                ],
            tools=self.tools,
            tool_choice="auto"
        )

        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls

        if tool_calls:
            tool_call = tool_calls[0]
            return tool_call.function.arguments
        
        else:
            return response_message.content
        
    
    def get_open_ai_response(self, message):
        """
        Function to use OpenAi API
        """

        client = openai.OpenAI(
            api_key=self.open_ai_api_key,
        )
        
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                    {"role":"system","content": self.initial_prompt },
                    {"role":"user","content": message}
                ],
            tools=self.tools,
            tool_choice="auto"
        )

        return response.choices[0].message.tool_calls[0].function.arguments
    


