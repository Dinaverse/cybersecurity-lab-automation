from flask import Flask, request, render_template_string, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

# In-memory storage for leaked letters (resets on restart)
leaked_letters = [
    "I've always loved the way you code... anonymous <3",
    "To the admin: Your robots.txt is showing. - Cupid"
]

HTML_TEMPLATE = """
<!-- Insert your existing CSS here -->
<div class="container">
    <h1>Cupid's Leaked Gallery</h1>
    <div id="gallery" style="text-align: left; margin-top: 20px;">
        {% for letter in letters %}
            <div class="letter-card" style="background: #fff0f5; padding: 15px; margin-bottom: 10px; border-radius: 10px; border-left: 5px solid #ff1493;">
                <p>"{{ letter }}"</p>
            </div>
        {% endfor %}
    </div>
    <hr>
    <form action="/submit" method="POST">
        <textarea name="message" placeholder="Submit your anonymous letter..." style="width:100%; height:60px;"></textarea>
        <button type="submit">Submit to Vault</button>
    </form>
</div>
"""

@app.route('/')
def gallery():
    return render_template_string(HTML_TEMPLATE, letters=leaked_letters)

@app.route('/submit', methods=['POST'])
def submit():
    # Use request.form to get data from the HTML form
    new_message = request.form.get('message')
    if new_message:
        leaked_letters.append(escape(new_message)) # Sanitize for safety
    return redirect(url_for('gallery'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
