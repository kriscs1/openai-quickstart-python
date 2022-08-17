import os
import logging
from tkinter import *
from tkinter import messagebox

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        # prompt = request.form["prompt"]
        # examples = request.form["examples"]
        response = openai.Completion.create(
            model="text-davinci-002",
            max_tokens=300,
            prompt=request.form["examples"] + ' ' + request.form["prompt"],
            # prompt=generate_prompt(prompt),
            temperature=float(request.form["temperature"])
        )

        # logging.debug(response)
        # messagebox.showinfo("Response", response)
        return render_template("index.html", result=response.choices[0].text)
        # return redirect(url_for("index", result=response.choices[0].text))
    
    result = request.args.get("result")
    return render_template("index.html", result=result)


# def generate_prompt(prompt):
#     return """Suggest three names for an animal that is a superhero.

# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         prompt.capitalize()
#     )

if __name__ == "__main__":
    app.run()
