from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Define an endpoint that takes two query parameters and returns JSON
@app.route('/endpoint', methods=['GET'])
def my_endpoint():
    # Get query parameters from the request
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Check if both parameters are provided
    if slack_name is None or track is None:
        return jsonify({"error": "Both parameters (param1 and param2) are required."}), 400
    
    day = datetime.now()
    current_day = (day.strftime("%A"))

    utc_time_value = datetime.utcnow()
    utc_time = utc_time_value.strftime("%Y-%m-%dT%H:%M:%SZ")
    

    github_file_url = "https://github.com/Stefanie-A/hngx-stageone-task/blob/master/task.py"
    github_repo_url = "https://github.com/Stefanie-A/hngx-stageone-task"
    result = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    # Return the result as JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')