import os
from datetime import datetime
from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)

COMMIT = (
    os.getenv("RENDER_GIT_COMMIT")
    or os.getenv("GIT_SHA")
    or "local"
)[:7]

BLOOD_GROUPS = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
AVAILABILITY = ["Available", "Not Available"]

donors = [
    {
        "id": 1,
        "name": "Demo Donor A",
        "blood_group": "O+",
        "city": "Pune",
        "contact": "demo@example.com",
        "last_donation": "2026-06-10",
        "availability": "Available",
    },
    {
        "id": 2,
        "name": "Demo Donor B",
        "blood_group": "A+",
        "city": "Pune",
        "contact": "demo@example.com",
        "last_donation": "2026-05-20",
        "availability": "Available",
    },
]


def validate_donor(data):
    required = [
        "name",
        "blood_group",
        "city",
        "contact",
        "last_donation",
        "availability",
    ]
    if any(not str(data.get(field, "")).strip() for field in required):
        return "All fields are required."

    if data["blood_group"] not in BLOOD_GROUPS:
        return "Invalid blood group."

    if data["availability"] not in AVAILABILITY:
        return "Invalid availability status."

    try:
        donation_date = datetime.strptime(
            data["last_donation"], "%Y-%m-%d"
        ).date()
    except ValueError:
        return "Last donation date must be in YYYY-MM-DD format."

    if donation_date > datetime.now().date():
        return "Last donation date cannot be in the future."

    return None


@app.route("/")
def home():
    blood_group = request.args.get("blood_group", "").strip()
    city = request.args.get("city", "").strip().lower()
    availability = request.args.get("availability", "").strip()

    filtered = donors
    if blood_group:
        filtered = [
            donor for donor in filtered if donor["blood_group"] == blood_group
        ]
    if city:
        filtered = [
            donor for donor in filtered if donor["city"].lower() == city
        ]
    if availability:
        filtered = [
            donor
            for donor in filtered
            if donor["availability"] == availability
        ]

    stats = {
        "total": len(donors),
        "available": sum(
            donor["availability"] == "Available" for donor in donors
        ),
        "o_positive": sum(
            donor["blood_group"] == "O+" for donor in donors
        ),
    }

    return render_template(
        "index.html",
        donors=filtered,
        stats=stats,
        blood_groups=BLOOD_GROUPS,
        availability_options=AVAILABILITY,
        selected_blood_group=blood_group,
        selected_city=request.args.get("city", ""),
        selected_availability=availability,
        commit=COMMIT,
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        donor = {
            "id": len(donors) + 1,
            "name": request.form.get("name", "").strip(),
            "blood_group": request.form.get("blood_group", "").strip(),
            "city": request.form.get("city", "").strip(),
            "contact": request.form.get("contact", "").strip(),
            "last_donation": request.form.get("last_donation", "").strip(),
            "availability": request.form.get("availability", "").strip(),
        }

        error = validate_donor(donor)
        if error is None:
            donors.append(donor)
            return redirect(url_for("home"))

    return render_template(
        "register.html",
        error=error,
        blood_groups=BLOOD_GROUPS,
        availability_options=AVAILABILITY,
        commit=COMMIT,
    )


@app.route("/api/donors")
def api_donors():
    blood_group = request.args.get("blood_group", "").strip()
    city = request.args.get("city", "").strip().lower()

    result = donors
    if blood_group:
        result = [
            donor for donor in result if donor["blood_group"] == blood_group
        ]
    if city:
        result = [
            donor for donor in result if donor["city"].lower() == city
        ]

    return jsonify(result)


@app.route("/health")
def health():
    return jsonify({"status": "ok", "commit": COMMIT})


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
