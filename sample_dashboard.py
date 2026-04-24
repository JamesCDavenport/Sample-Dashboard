from flask import Flask, render_template

app = Flask(__name__)

@app.route("/sample_api")
def sample_api():
    sample_graph = {
        "type": "line",
        "data": "PLACEHOLDER",
        "options": {
            "responsive": True,
            "plugins": {
                "title": {
                    "display": True,
                    "text": "Sample Graph"
                },
            },
            "interaction": {
                "intersect": False,
            },
            "scales": {

            }
        }
    }

def main():
    app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ == "__main__":
    main()  