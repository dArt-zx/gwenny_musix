from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    lyrics = [
        "So I'ma love you every night like it's the last night",
        "Like it's the last night",
        "If the world was ending",
        "I'd wanna be next to you",
        "If the party was over",
        "And our time on Earth was through",
        "I'd wanna hold you just for a while",
        "And die with a smile",
        "If the world was ending",
        "I'd wanna be next to you",
        "Right next to you"
    ]
    delays = [600, 700, 1000, 4600, 1000, 3600, 1700, 2000, 900, 1200, 500]

    return render_template('index.html', lyrics=lyrics, delays=delays)

if __name__ == '__main__':
    app.run(debug=True)
