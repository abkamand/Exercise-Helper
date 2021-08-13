from flask import Flask, json, jsonify, request, render_template
import requests

app = Flask(__name__)

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
    response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    #Joel's wikipedia scraper service request
    response = requests.get("http://flip3.engr.oregonstate.edu:10664/search?q=biceps+curl")
    #print(response.url)
    #print(response.text)
    wiki_desc = response.text


    return render_template("novarms1.html", embed_link=youtube_link, summary = wiki_desc)

@app.route("/novback1")
def novback1():
    # youtube service request
    payload = {"videoid": "CAwf7n6Luuc"}
    response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
    youtube_link = response.text

    #Joel's wikipedia scraper service request
    response = requests.get("http://flip3.engr.oregonstate.edu:10664/search?q=Pull-down+(exercise)")
    wiki_desc = response.text

    return render_template("novback1.html", embed_link=youtube_link, summary = wiki_desc)

@app.route("/novcore1")
def novcore1():
    # youtube service request
    payload = {"videoid": "ASdvN_XEl_c"}
    response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    #Joel's wikipedia scraper service request
    response = requests.get("http://flip3.engr.oregonstate.edu:10664/search?q=Plank+(exercise)")
    #print(response.url)
    #print(response.text)
    wiki_desc = response.text

    return render_template("novcore1.html", embed_link=youtube_link, summary = wiki_desc)

@app.route("/novlegs1")
def novlegs1():
    # youtube service request
    payload = {"videoid": "gwLzBJYoWlI"}
    response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    #Joel's wikipedia scraper service request
    response = requests.get("http://flip3.engr.oregonstate.edu:10664/search?q=Calf+raises")
    #print(response.url)
    #print(response.text)
    wiki_desc = response.text

    return render_template("novlegs1.html", embed_link=youtube_link, summary = wiki_desc)

@app.route("/novchest1")
def novchest1():
    # youtube service request
    payload = {"videoid": "IODxDxX7oi4"}
    response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    #Joel's wikipedia scraper service request
    response = requests.get("http://flip3.engr.oregonstate.edu:10664/search?q=Push-up")
    #print(response.url)
    #print(response.text)
    wiki_desc = response.text

    return render_template("novchest1.html", embed_link=youtube_link, summary = wiki_desc)

# "Page 3 Proficient Routes"
@app.route("/profarms1")
def profarms1():
    # youtube service request
    payload = {"videoid": "VKFeB7ST830"}
    response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    #Joel's wikipedia scraper service request
    response = requests.get("http://flip3.engr.oregonstate.edu:10664/search?q=Bent-over+row")
    #print(response.url)
    #print(response.text)
    wiki_desc = response.text

    return render_template("profarms1.html", embed_link=youtube_link, summary = wiki_desc)

@app.route("/profback1")
def profback1():
    # youtube service request
    payload = {"videoid": "eGo4IYlbE5g"}
    response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    #Joel's wikipedia scraper service request
    response = requests.get("http://flip3.engr.oregonstate.edu:10664/search?q=Pull-up+(exercise)")
    #print(response.url)
    #print(response.text)
    wiki_desc = response.text

    return render_template("profback1.html", embed_link=youtube_link, summary = wiki_desc)

@app.route("/profcore1")
def profcore1():
    # youtube service request
    payload = {"videoid": "JB2oyawG9KI"}
    response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    #Joel's wikipedia scraper service request
    response = requests.get("http://flip3.engr.oregonstate.edu:10664/search?q=Leg+raise")
    #print(response.url)
    #print(response.text)
    wiki_desc = response.text

    return render_template("profcore1.html", embed_link=youtube_link, summary = wiki_desc)

@app.route("/proflegs1")
def proflegs1():
    # youtube service request
    payload = {"videoid": "1oed-UmAxFs"}
    response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    #Joel's wikipedia scraper service request
    response = requests.get("http://flip3.engr.oregonstate.edu:10664/search?q=Squat+(exercise)")
    #print(response.url)
    #print(response.text)
    wiki_desc = response.text

    return render_template("proflegs1.html", embed_link=youtube_link, summary = wiki_desc)

@app.route("/profchest1")
def profchest1():
    # youtube service request
    payload = {"videoid": "rT7DgCr-3pg"}
    response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    #Joel's wikipedia scraper service request
    response = requests.get("http://flip3.engr.oregonstate.edu:10664/search?q=Bench+press")
    #print(response.url)
    #print(response.text)
    wiki_desc = response.text

    return render_template("profchest1.html", embed_link=youtube_link, summary = wiki_desc)

# "Page 3 Expert Routes"
@app.route("/exparms1")
def exparms1():
    # youtube service request
    payload = {"videoid": "wjUmnZH528Y"}
    response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    #Joel's wikipedia scraper service request
    response = requests.get("http://flip3.engr.oregonstate.edu:10664/search?q=Dip+(exercise)")
    #print(response.url)
    #print(response.text)
    wiki_desc = response.text

    return render_template("exparms1.html", embed_link=youtube_link, summary = wiki_desc)

@app.route("/expback1")
def expback1():
    # youtube service request
    payload = {"videoid": "brhRXlOhsAM"}
    response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    #Joel's wikipedia scraper service request
    response = requests.get("http://flip3.engr.oregonstate.edu:10664/search?q=Chin-up")
    #print(response.url)
    #print(response.text)
    wiki_desc = response.text

    return render_template("expback1.html", embed_link=youtube_link, summary = wiki_desc)

@app.route("/expcore1")
def expore1():
    # youtube service request
    payload = {"videoid": "Iwyvozckjak"}
    response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text

    #Joel's wikipedia scraper service request
    response = requests.get("http://flip3.engr.oregonstate.edu:10664/search?q=Crunch+(exercise)")
    #print(response.url)
    #print(response.text)
    wiki_desc = response.text

    return render_template("expcore1.html", embed_link=youtube_link, summary = wiki_desc)

@app.route("/explegs1")
def explegs1():
    # youtube service request
    payload = {"videoid": "r4MzxtBKyNE"}
    response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text
    
    #Joel's wikipedia scraper service request
    response = requests.get("http://flip3.engr.oregonstate.edu:10664/search?q=Deadlift")
    #print(response.url)
    #print(response.text)
    wiki_desc = response.text

    return render_template("explegs1.html", embed_link=youtube_link, summary = wiki_desc)

@app.route("/expchest1")
def expchest1():
    # youtube service request
    payload = {"videoid": "eozdVDA78K0"}
    response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
    #print(response.url)
    #print(response.text)
    youtube_link = response.text
    
    #Joel's wikipedia scraper service request
    response = requests.get("http://flip3.engr.oregonstate.edu:10664/search?q=Fly+(exercise)")
    #print(response.url)
    #print(response.text)
    wiki_desc = response.text

    return render_template("expchest1.html", embed_link=youtube_link, summary = wiki_desc)

"""
# transform youtube video id into a youtube embed link and return
@app.route("/embedlink")
def embed_link():
    video_id = request.args.get('videoid')
    embed_link = "https://www.youtube.com/embed/" + video_id

    return embed_link"""

if __name__ == "__main__":
    app.run(debug=True)