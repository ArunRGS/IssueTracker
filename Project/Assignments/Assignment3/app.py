from flask import Flask, render_template,request
import requests


app = Flask(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/testApi',methods=['POST'])
def api():
    url = "https://anime-quotes1.p.rapidapi.com/api/random"

    headers = {
        "X-RapidAPI-Key": "5ee701d49bmsh8fa86c398281d3bp17a3c9jsn99c19b815523",
        "X-RapidAPI-Host": "anime-quotes1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    q = response.json()
    print(q)
    result = q['quote']
    return render_template('login.html', output=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')