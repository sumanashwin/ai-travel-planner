import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables (.env locally, HuggingFace Secrets in deployment)
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY is not set")

# Initialize OpenRouter client
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# Supported models
MODELS = [
    "openai/gpt-4o-mini",
    "anthropic/claude-3-haiku",
    "meta-llama/llama-3-70b-instruct",
    "mistralai/mistral-7b-instruct"
]


# Travel planner function
def generate_travel_plan(destination, days, budget, style, interests, model):

    prompt = f"""
You are an expert travel planner.

Create a beautiful travel itinerary in Markdown.

Destination: {destination}
Trip Length: {days} days
Budget: {budget}
Travel Style: {style}
User Interests: {interests}

Format exactly like this:

# 🌍 Travel Plan for {destination}

## ✨ Overview
Short engaging introduction.

## 📅 Day 1
Morning activities  
Afternoon activities  
Evening activities  

Continue until Day {days}.

## 🍜 Must-Try Food
List 4-5 local dishes.

## 💰 Budget Tips
Practical saving advice.

## ✈️ Travel Tips
Important traveler tips.
"""

    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    response = ""

    for chunk in completion:
        delta = chunk.choices[0].delta.content or ""
        response += delta
        yield response


# CSS styling for itinerary panel
css = """
#travel_output {
    background: #ffffff;
    padding: 25px;
    border-radius: 14px;
    border: 1px solid #e2e8f0;
    max-height: 600px;
    overflow-y: auto;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.05);
}
"""


# UI
with gr.Blocks(fill_width=True) as demo:

    gr.Markdown(
        """
# 🌍 AI Travel Planner

Generate a personalized multi-day travel itinerary using AI.
"""
    )

    gr.Markdown("---")

    with gr.Row():

        # INPUT PANEL
        with gr.Column(scale=1):

            gr.Markdown("## ✈️ Trip Details")

            destination = gr.Textbox(
                label="Destination",
                placeholder="e.g. Kyoto, Bali, Paris"
            )

            days = gr.Number(
                label="Number of Days",
                value=5,
                precision=0
            )

            budget = gr.Dropdown(
                ["low", "medium", "luxury"],
                label="Budget",
                value="medium"
            )

            style = gr.Dropdown(
                ["backpacking", "family", "luxury", "adventure", "culture"],
                label="Travel Style",
                value="culture"
            )

            interests = gr.Textbox(
                label="Interests",
                placeholder="food, temples, nature, nightlife"
            )

            model = gr.Dropdown(
                MODELS,
                label="Model",
                value=MODELS[0]
            )

            generate_button = gr.Button(
                "Generate Travel Plan",
                variant="primary"
            )

        # OUTPUT PANEL
        with gr.Column(scale=2):

            gr.Markdown("## 🗺️ Generated Itinerary")

            output = gr.Markdown(
                elem_id="travel_output"
            )

    gr.Markdown("---")

    gr.Examples(
        examples=[
            ["Paris", 5, "medium", "culture", "food", MODELS[0]],
            ["Tokyo", 7, "luxury", "adventure", "anime", MODELS[0]],
            ["Kerala", 4, "medium", "family", "nature", MODELS[0]]
        ],
        inputs=[destination, days, budget, style, interests, model]
    )

    generate_button.click(
        generate_travel_plan,
        inputs=[destination, days, budget, style, interests, model],
        outputs=output,
        show_progress=True
    )


demo.launch(css=css, theme=gr.themes.Soft())