from app import create_app, db

app = create_app()

# Auto-create all tables when app starts
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=False)