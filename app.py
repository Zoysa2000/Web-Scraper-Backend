from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import scrape_linkedin_jobs

app = Flask(__name__)
CORS(app)

@app.route("/api/jobs", methods=["GET"])
def get_jobs():
    keyword = request.args.get("keyword", "AI Engineer")
    location = request.args.get("location", "USA")
    jobs = scrape_linkedin_jobs(keyword, location)
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(debug=True)

