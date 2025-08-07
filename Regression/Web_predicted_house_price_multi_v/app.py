from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load your trained model
model = joblib.load('model_jb1.joblib')

# Route: Display form and handle POST
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            # Get form values and convert to float/int as required
            area = float(request.form['area'])
            bedrooms = int(request.form['bedrooms'])
            bathrooms = int(request.form['bathrooms'])
            stories = int(request.form['stories'])
            guestroom = int(request.form['guestroom'])
            basement = int(request.form['basement'])

            features = [area, bedrooms, bathrooms, stories, guestroom, basement]
            prediction = int(model.predict([features])[0])

            return render_template('form.html', prediction=f"Predicted Price: PKR {prediction:,}")
        except:
            return render_template('form.html', prediction="⚠️ Invalid input. Please try again.")

    return render_template('form.html')
    
if __name__ == '__main__':
    app.run(debug=True)
