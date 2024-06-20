from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL database connection
db = mysql.connector.connect(
    host="sql12.freesqldatabase.com",
    user="sql12714674",
    password="15cCYtDhUC",
    database="sql12714674"
)
cursor = db.cursor()

@app.route('/report', methods=['POST'])
def submit_report():
    try:
        spam_emails = request.form['spam_emails']
        spam_sms = request.form['spam_sms']
        spam_calls = request.form['spam_calls']
        malicious_urls = request.form['malicious_urls']
        phishing_urls = request.form['phishing_urls']
        illicit_video_urls = request.form['illicit_video_urls']

        query = "INSERT INTO reports (spam_emails, spam_sms, spam_calls, malicious_urls, phishing_urls, illicit_video_urls) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (spam_emails, spam_sms, spam_calls, malicious_urls, phishing_urls, illicit_video_urls)
        cursor.execute(query, values)
        db.commit()

        return 'Report submitted successfully'
    except Exception as e:
        # Return the error message as a JSON response
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
