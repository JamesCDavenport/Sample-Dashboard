from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/sample_api")
def sample_api():
    data = {
        "datasets": [
            {
                "label": "Sample Sensor 0",
                "yAxisID": "y0",
                "data": [
                    {"x": 17770320, "y": 0.0},
                    {"x": 17770323, "y": 0.5},
                    {"x": 17770326, "y": 0.866},
                    {"x": 17770329, "y": 1.0},
                    {"x": 17770332, "y": 0.866},
                    {"x": 17770335, "y": 0.5},
                    {"x": 17770338, "y": 0.0},
                    {"x": 17770341, "y": -0.5},
                    {"x": 17770344, "y": -0.866},
                    {"x": 17770347, "y": -1.0},
                    {"x": 17770350, "y": -0.866},
                    {"x": 17770353, "y": -0.5},
                ],
            },
            {
                "label": "Sample Sensor 1",
                "yAxisID": "y1",
                "data": [
                    {"x": 17770320, "y": 0.0},
                    {"x": 17770323, "y": 25.0},
                    {"x": 17770326, "y": 43.3},
                    {"x": 17770329, "y": 50.0},
                    {"x": 17770332, "y": 43.3},
                    {"x": 17770335, "y": 25.0},
                    {"x": 17770338, "y": 0.0},
                    {"x": 17770341, "y": -25.0},
                    {"x": 17770344, "y": -43.3},
                    {"x": 17770347, "y": -50.0},
                    {"x": 17770350, "y": -43.3},
                    {"x": 17770353, "y": -25.0},
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