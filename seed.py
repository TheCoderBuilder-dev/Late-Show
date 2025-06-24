import csv
from app import create_app
from app.models import db, Guest, Episode, Appearance

# Make the app
app = create_app()
with app.app_context():
    print("Seeding database...")
    db.drop_all()
    db.create_all()
    with open('guests.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            guest = Guest(
                id=int(row['id']),
                name=row['name'],
                occupation=row['occupation']
            )
            db.session.add(guest)
    ep1 = Episode(date="1/11/99", number=1)
    ep2 = Episode(date="1/12/99", number=2)
    db.session.add_all([ep1, ep2])


    ap1 = Appearance(rating=4, episode=ep1, guest_id=1)
    ap2 = Appearance(rating=5, episode=ep2, guest_id=3)
    db.session.add_all([ap1, ap2])

    # Save everything
    db.session.commit()

    print(" Done seeding!")
