from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
    if name:
        return f"""
       <h1>Welcome Pleas Enter your{name}! </h1>
       <p>Great to see you.</p>
       <a href="/">Go Back</a>
       """
    return f"""
    <h1>Welcome!</h1>
    <form>
        <input type="text" name="name placeholder="Enter your name">
        <button type="submit">Click Me</button>
        </form>
        """
if __name__ == "__main__":
    app.run(debug=True)