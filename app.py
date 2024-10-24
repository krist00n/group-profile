from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Data anggota tim
team_members = [
    {
        "name": "Gilang Wahyu Pratama",
        "nim": "22.83.0904",
        "education": "S1 Teknik Komputer Amikom",
        "bio": "saya Gilang, saya berasal dari jawa, saya kuliah di sini, hobi saya mancing (mainan alat pancing)",
        "image": "/static/images/gilang.jpg",
        "instagram": "https://www.instagram.com/gilang.w26_/",
        "instagram_username": "gilang.w26_"
    },
    {
        "name": "M. Hisyam Ramadhan",
        "nim": "22.83.0938",
        "education": "S1 Teknik Komputer Amikom",
        "bio": "Halo saya Hisyam, saya brasal dari Sleman Yogyakarta, prodi Teknik Komputer Universitas Amikom Yogyakarta",
        "image": "/static/images/hisyam.jpg",
        "instagram": "https://www.instagram.com/mhmd.hisyam_",
        "instagram_username": "mhmd.hisyam_"
    },
    {
        "name": "Faesal Krisna Wijaya",
        "nim": "22.83.0901",
        "education": "S1 Teknik Komputer Amikom",
        "bio": "Manusia sederhana yang belum punya apa-apa.",
        "image": "/static/images/krisna.jpg",
        "instagram": "https://instagram.com/n0tany1_",
        "instagram_username": "n0tany1"
    },
    {
        "name": "Marlinda Veronica O N",
        "nim": "21.83.0615",
        "education": "S1 Teknik Komputer Amikom",
        "bio": "Perkenalkan nama saya Vero. Saya berkuliah di Universitas Amikom Yogyakarta. Asal saya dari papua, dan hobi saya saat ini adalah menyanyi dan gitar.",
        "image": "/static/images/vero.jpg",
        "instagram": "https://www.instagram.com/ocyeanic.feronif/",
        "instagram_username": "ocyeanic.feronif"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/team', methods=['GET'])
def get_team_members():
    return jsonify(team_members)

if __name__ == '__main__':
    app.run(debug=True)
