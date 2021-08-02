from flask import Flask, json, jsonify, request, render_template
import requests

app = Flask(__name__)


# Home route
@app.route("/")
def home():
    return render_template("home.html")

# "Page 2 Routes"
@app.route("/arms")
def arms():
    return render_template("arms.html")

@app.route("/back")
def back():
    return render_template("back.html")

@app.route("/core")
def core():
    return render_template("core.html")

@app.route("/legs")
def legs():
    return render_template("legs.html")

@app.route("/chest")
def chest():
    return render_template("chest.html")

# "Page 3 Novice Routes"
@app.route("/novarms1")
def novarms1():
    # youtube service request
    payload = {"videoid": "XE_pHwbst04"}
    response = requests.get("http://127.0.0.1:5000/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text


    return render_template("novarms1.html", embed_link=youtube_link)

@app.route("/novback1")
def novback1():
    # youtube service request
    payload = {"videoid": "CAwf7n6Luuc"}
    response = requests.get("http://127.0.0.1:5000/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    return render_template("novback1.html", embed_link=youtube_link)

@app.route("/novcore1")
def novcore1():
    # youtube service request
    payload = {"videoid": "ASdvN_XEl_c"}
    response = requests.get("http://127.0.0.1:5000/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    return render_template("novcore1.html", embed_link=youtube_link)

@app.route("/novlegs1")
def novlegs1():
    # youtube service request
    payload = {"videoid": "gwLzBJYoWlI"}
    response = requests.get("http://127.0.0.1:5000/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    return render_template("novlegs1.html", embed_link=youtube_link)

@app.route("/novchest1")
def novchest1():
    # youtube service request
    payload = {"videoid": "IODxDxX7oi4"}
    response = requests.get("http://127.0.0.1:5000/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    return render_template("novchest1.html", embed_link=youtube_link)

# "Page 3 Proficient Routes"
@app.route("/profarms1")
def profarms1():
    # youtube service request
    payload = {"videoid": "VKFeB7ST830"}
    response = requests.get("http://127.0.0.1:5000/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    return render_template("profarms1.html", embed_link=youtube_link)

@app.route("/profback1")
def profback1():
    # youtube service request
    payload = {"videoid": "eGo4IYlbE5g"}
    response = requests.get("http://127.0.0.1:5000/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    return render_template("profback1.html", embed_link=youtube_link)

@app.route("/profcore1")
def profcore1():
    # youtube service request
    payload = {"videoid": "JB2oyawG9KI"}
    response = requests.get("http://127.0.0.1:5000/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    return render_template("profcore1.html", embed_link=youtube_link)

@app.route("/proflegs1")
def proflegs1():
    # youtube service request
    payload = {"videoid": "1oed-UmAxFs"}
    response = requests.get("http://127.0.0.1:5000/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    return render_template("proflegs1.html", embed_link=youtube_link)

@app.route("/profchest1")
def profchest1():
    # youtube service request
    payload = {"videoid": "rT7DgCr-3pg"}
    response = requests.get("http://127.0.0.1:5000/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    return render_template("profchest1.html", embed_link=youtube_link)

# "Page 3 Expert Routes"
@app.route("/exparms1")
def exparms1():
    # youtube service request
    payload = {"videoid": "wjUmnZH528Y"}
    response = requests.get("http://127.0.0.1:5000/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    return render_template("exparms1.html", embed_link=youtube_link)

@app.route("/expback1")
def expback1():
    # youtube service request
    payload = {"videoid": "brhRXlOhsAM"}
    response = requests.get("http://127.0.0.1:5000/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    return render_template("expback1.html", embed_link=youtube_link)

@app.route("/expcore1")
def expore1():
    # youtube service request
    payload = {"videoid": "Iwyvozckjak"}
    response = requests.get("http://127.0.0.1:5000/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    return render_template("expcore1.html", embed_link=youtube_link)

@app.route("/explegs1")
def explegs1():
    # youtube service request
    payload = {"videoid": "r4MzxtBKyNE"}
    response = requests.get("http://127.0.0.1:5000/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text
    
    return render_template("explegs1.html", embed_link=youtube_link)

@app.route("/expchest1")
def expchest1():
    # youtube service request
    payload = {"videoid": "eozdVDA78K0"}
    response = requests.get("http://127.0.0.1:5000/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text
    
    return render_template("expchest1.html", embed_link=youtube_link)

# microservice, transform youtube video id into a youtube embed link, and return back
@app.route("/embedlink")
def embed_link():
    video_id = request.args.get('videoid')
    #print(video_id)


    embed_link = "https://www.youtube.com/embed/" + video_id
    #print(embed_link)

    return embed_link


if __name__ == "__main__":
    app.run(debug=True)