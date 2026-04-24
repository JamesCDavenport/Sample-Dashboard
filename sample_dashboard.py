from flask import Flask, render_template

app = Flask(__name__)

@app.route("/sample_api")
def sample_api():
    data = {
        "datasets": [
            {
                "label": "Sample Sensor 0",
                "yAxisID": "y0",
                "data": [
                    {"x": 1777032000000, "y": 0.0},
                    {"x": 1777032300000, "y": 0.5},
                    {"x": 1777032600000, "y": 0.866},
                    {"x": 1777032900000, "y": 1.0},
                    {"x": 1777033200000, "y": 0.866},
                    {"x": 1777033500000, "y": 0.5},
                    {"x": 1777033800000, "y": 0.0},
                    {"x": 1777034100000, "y": -0.5},
                    {"x": 1777034400000, "y": -0.866},
                    {"x": 1777034700000, "y": -1.0},
                    {"x": 1777035000000, "y": -0.866},
                    {"x": 1777035300000, "y": -0.5},
                ],
            },
            {
                "label": "Sample Sensor 1",
                "yAxisID": "y1",
                "data": [
                    {"x": 1777032000000, "y": 0.0},
                    {"x": 1777032300000, "y": 25.0},
                    {"x": 1777032600000, "y": 43.3},
                    {"x": 1777032900000, "y": 50.0},
                    {"x": 1777033200000, "y": 43.3},
                    {"x": 1777033500000, "y": 25.0},
                    {"x": 1777033800000, "y": 0.0},
                    {"x": 1777034100000, "y": -25.0},
                    {"x": 1777034400000, "y": -43.3},
                    {"x": 1777034700000, "y": -50.0},
                    {"x": 1777035000000, "y": -43.3},
                    {"x": 1777035300000, "y": -25.0},
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
                "y": {
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
        },
    }

def main():
    app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ == "__main__":
    main()  