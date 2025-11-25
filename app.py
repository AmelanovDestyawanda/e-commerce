from flask import Flask, render_template, request
from src.preprocess import preprocess_data
from src.rfm import create_rfm
from src.clustering import run_kmeans

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == "POST":
        n_clusters = int(request.form['cluster'])

        df = preprocess_data("data/ecom.csv")
        rfm = create_rfm(df)
        clustered = run_kmeans(rfm, n_clusters)

        clustered.to_csv("output/cluster_result.csv")
        result = clustered.head(20).to_html()

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)