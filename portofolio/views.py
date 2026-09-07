from django.shortcuts import render

def landing_page(request):
    context = {
        "name": "Rois",
        "avatar_url": "/static/img/rois.jpg",
        "kicker": "Computer Science · Universitas Indonesia",
        "bio": "Computer Science student at Universitas Indonesia with a strong interest "
               "in data engineering — turning raw data into meaningful insights and "
               "understanding the systems behind large-scale data processing.",
        "npm": "2506620210",
        "program" : "Computer Science",
        "social_links": [
            {"name": "GitHub", "url": "https://github.com/Roisul-Umam"},
            {"name": "LinkedIn", "url": "https://www.linkedin.com/in/roisul-umam-83577b302/?locale=en"},
            {"name": "Email", "url": "mailto:umamr545@gmail.com"}
        ],
        "skills": [
            "Python for Data Analysis",
            "Java",
            "HTML & CSS",
            "SQL",
            "Git",
            "Figma for UI/UX",
            "Docker",
        ],
        "projects": [
            {
                "name": "Rainfall Model Prediction",
                "description": "Sebuah model prediksi curah hujan menggunakan teknik machine learning yang dibuat oleh saya sendiri.",
                "tags": ["Python", "Pandas", "Machine Learning", "Data Analysis"],
                "link": "#",
            },
            {
                "name": "Website Portofolio Ini",
                "description": "Sebuah website portofolio yang dibuat untuk menampilkan riwayat pendidikan, pengalaman kerja, dan project-project yang telah saya kerjakan.",
                "tags": ["Python", "Django", "HTML", "CSS", "SQL"],
                "link": "#",
            },
        ]
    }
    return render(request, "index.html", context)