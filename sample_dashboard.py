from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/sample_api")
def sample_api():
    data = {
        "labels": [0, 20, 40, 60, 80, 100],
        "datasets": [
            {
                "label": "Sample Sensor 0",
                "yAxisID": "y0",
                "data": [
                    {"x": 0, "y": 0.0},
                    {"x": 20, "y": -0.5},
                    {"x": 40, "y": -0.866},
                    {"x": 60, "y": -1.0},
                    {"x": 80, "y": -0.866},
                    {"x": 100, "y": -0.5},
                ],
            },
            {
                "label": "Sample Sensor 1",
                "yAxisID": "y1",
                "data": [
                    {"x": 0, "y": 0.0},
                    {"x": 20, "y": 25.0},
                    {"x": 40, "y": 43.3},
                    {"x": 60, "y": 50.0},
                    {"x": 80, "y": 43.3},
                    {"x": 100, "y": 25.0},
                ],
            },
        ]
    }

    sample_graph = {
        "type": "line",
        "data": data,
        "options": {
            "responsive": True,
            "interaction": {
                "mode": "index",
                "intersect": False,
            },
            "stacked": False,
            "plugins": {
                "title": {
                    "display": True,
                    "text": "Chart.js Line Chart - Multi Axis",
                }
            },
            "scales": {
                "y0": {
                    "type": "linear",
                    "display": True,
                    "position": "left",
                },
                "y1": {
                    "type": "linear",
                    "display": True,
                    "position": "right",
                    "grid": {
                        "drawOnChartArea": False,
                    },
                },
            },
            "animations": False,
        },
    }

    return json.dumps(sample_graph)

@app.route("/")
def index():
    return render_template("sample_dashboard.html")

def main():
    app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ == "__main__":
    main()  