from flask import Flask, render_template, request
import feedparser
import os

app = Flask(__name__)

def get_rss(seccio, diari, mode='local'):
    if mode == 'local':
        xml_path = os.path.join('rss', diari, f'{seccio}.xml')
        if not os.path.exists(xml_path):
            return None
        return feedparser.parse(xml_path)
    else:
        if diari == 'lavanguardia':
            url = f'https://www.lavanguardia.com/rss/{seccio}.xml'
        elif diari == 'puntavui':
            url = f'https://www.elpuntavui.cat/{seccio}.feed?type=rss'
        else:
            return None
        return feedparser.parse(url)

@app.route("/")
def inici():
    return render_template("index.html")

@app.route("/lavanguardia")
def lavanguardia():
    mode = request.args.get("mode", "remote")
    selected = request.args.get("seccio", "comer")  
    seccions = ['comer', 'cultura', 'deportes', 'economia']

    feeds = {
        seccio: get_rss(seccio, 'lavanguardia', mode)
        for seccio in seccions
    }

    return render_template("lavanguardia.html", feeds=feeds, mode=mode, selected=selected)


if __name__ == "__main__":
    app.run(debug=True)



