from app import app, donors


def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_health():
    response = client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_add_valid_donor():
    donors.clear()
    response = client().post(
        "/register",
        data={
            "name": "Test Donor",
            "blood_group": "O+",
            "city": "Pune",
            "contact": "test@example.com",
            "last_donation": "2026-07-01",
            "availability": "Available",
        },
        follow_redirects=False,
    )
    assert response.status_code == 302
    assert donors[0]["blood_group"] == "O+"


def test_invalid_blood_group_rejected():
    donors.clear()
    response = client().post(
        "/register",
        data={
            "name": "Test Donor",
            "blood_group": "X+",
            "city": "Pune",
            "contact": "test@example.com",
            "last_donation": "2026-07-01",
            "availability": "Available",
        },
    )
    assert response.status_code == 200
    assert b"Invalid blood group" in response.data
    assert donors == []


def test_api_filters_by_blood_group():
    donors.clear()
    donors.extend(
        [
            {
                "id": 1,
                "name": "A",
                "blood_group": "O+",
                "city": "Pune",
                "contact": "a@example.com",
                "last_donation": "2026-06-01",
                "availability": "Available",
            },
            {
                "id": 2,
                "name": "B",
                "blood_group": "A+",
                "city": "Pune",
                "contact": "b@example.com",
                "last_donation": "2026-06-01",
                "availability": "Available",
            },
        ]
    )
    response = client().get("/api/donors?blood_group=O%2B")
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["blood_group"] == "O+"


def test_api_filters_by_city():
    donors.clear()
    donors.extend(
        [
            {
                "id": 1,
                "name": "Pune Donor",
                "blood_group": "O+",
                "city": "Pune",
                "contact": "pune@example.com",
                "last_donation": "2026-06-01",
                "availability": "Available",
            },
            {
                "id": 2,
                "name": "Mumbai Donor",
                "blood_group": "A+",
                "city": "Mumbai",
                "contact": "mumbai@example.com",
                "last_donation": "2026-06-01",
                "availability": "Available",
            },
        ]
    )

    response = client().get("/api/donors?city=Pune")

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["city"] == "Pune"


def test_future_donation_date_rejected():
    donors.clear()

    response = client().post(
        "/register",
        data={
            "name": "Future Donor",
            "blood_group": "O+",
            "city": "Pune",
            "contact": "future@example.com",
            "last_donation": "2099-01-01",
            "availability": "Available",
        },
    )

    assert response.status_code == 200
    assert b"cannot be in the future" in response.data
    assert donors == []
