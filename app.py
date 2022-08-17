import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = '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'

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        response = openai.Completion.create(
            model="text-davinci-002",
            max_tokens=300,
            prompt=request.form["examples"] + ' ' + request.form["prompt"],
            temperature=float(request.form["temperature"])
        )

        return render_template("index.html", result=response.choices[0].text)
    
    result = request.args.get("result")
    return render_template("index.html", result=result)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
