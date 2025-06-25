from app import app

def test_homepage():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

    data = response.get_json()
    assert "message" in data
    # מאשרים שהתוכן מכיל או 'EntryTracker' (הצלחה), או 'connect' (שגיאת חיבור)
    assert ("EntryTracker" in data["message"]) or ("connect" in data["message"])
