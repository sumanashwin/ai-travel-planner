# 🌍 AI Travel Planner

An AI-powered travel itinerary generator built with **Gradio** and **OpenRouter**.

The app creates a personalized multi-day travel plan based on destination, budget, travel style, and interests.

---

## 🚀 Features

* Interactive **Gradio UI**
* **Model selection dropdown** (OpenRouter models)
* **Streaming AI responses**
* Clean **Markdown travel itinerary**
* Example prompts for quick testing

---

## 🛠️ Tech Stack

* Python
* Gradio
* OpenRouter API
* Large Language Models

---

## 📦 Installation (Local)

Clone the repository:

```bash
git clone https://github.com/sumanashwin/ai-travel-planner.git
cd ai-travel-planner
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python app.py
```

---

## 🔐 Environment Variables

Create a `.env` file and add:

```
OPENROUTER_API_KEY=your_api_key_here
```

---

## 🌐 Deployment

This project can be deployed on **Hugging Face Spaces** using the **Gradio SDK**.

---

## 📸 Example

The app generates a structured travel guide like:

```
🌍 Travel Plan for Kyoto

✨ Overview  
Brief introduction.

📅 Day 1  
Morning activities  
Afternoon activities  
Evening activities  

🍜 Must-Try Food  
Local dishes to try.

💰 Budget Tips  
Cost-saving advice.
```

---

## 📄 License

MIT License
