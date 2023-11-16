from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
api_key = "API KEY"

# Initialize OpenAI
openai.api_key = api_key


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        past_travel_info = request.form.get("q")

        # Enhance the prompt with context for a future tour plan
        prompt = f"Based on my past travel experiences, I would like to plan a future tour. I have visited {past_travel_info}. Please suggest a new destination, activities, and the duration of the trip."

        # Call OpenAI to generate the future tour plan
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=200,  # Adjust token limit as needed
        )
        tour_plan = response.choices[0].text.strip()

        return render_template("index.html", past_travel_info=past_travel_info, tour_plan=tour_plan)

    return render_template("index.html", past_travel_info="", tour_plan="")


if __name__ == "__main__":
    app.run(debug=True)