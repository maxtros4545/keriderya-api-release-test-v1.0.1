from app import app, db  # Import the app and db instances
from app.models.menu_model import MenuModel

# Create some dummy data
dummy_data = MenuModel(name="Sample Menu", price=100, description="Sample description", availability=True, restaurant_id=1, category_id=1)

# Set up the application context
with app.app_context():
    # Add the dummy data to the session
    db.session.add(dummy_data)
    
    # Commit the changes to the database
    db.session.commit()

    print("Dummy data added successfully.")
