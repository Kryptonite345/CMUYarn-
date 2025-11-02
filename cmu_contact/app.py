from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# ---------- DATABASE CONNECTION ----------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cmuwebsite"
)
cursor = db.cursor()

# ---------- STATIC PAGE ROUTES ----------
@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html')

@app.route('/admission')
def admission():
    return render_template('Admission.html')

@app.route('/courses')
def courses():
    return render_template('Courses.html')

@app.route('/news')
def news():
    return render_template('News.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/enroll')
def enroll():
    return render_template('enrollment_form.html')

# ---------- CONTACT US FORM ----------
@app.route('/submit_message', methods=['POST'])
def submit_message():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    sql = "INSERT INTO messages (name, email, subject, message) VALUES (%s, %s, %s, %s)"
    values = (name, email, subject, message)
    cursor.execute(sql, values)
    db.commit()

    # After saving, stay on the same page
    return redirect(url_for('contact_us'))

# ---------- ENROLLMENT FORM ----------
@app.route('/submit_enrollment', methods=['POST'])
def submit_enrollment():
    data = request.form.to_dict()
    sql = """
    INSERT INTO enrollments (
        program, last_name, given_name, middle_name, ext_name,
        gender, civil_status, birth_date, birth_place, nationality,
        religion, contact_no, email_address, address, residence,
        indigenous_group, indigenous_details, father_name, father_occupation,
        father_income, father_contact, mother_name, mother_occupation,
        mother_income, mother_contact, guardian_name, guardian_relationship,
        guardian_occupation, guardian_income, guardian_contact, school_name,
        school_address, lrn, disability, disability_details, facebook, time
    ) VALUES (
        %(program)s, %(last_name)s, %(given_name)s, %(middle_name)s, %(ext_name)s,
        %(gender)s, %(civil_status)s, %(birth_date)s, %(birth_place)s, %(nationality)s,
        %(religion)s, %(contact_no)s, %(email_address)s, %(address)s, %(residence)s,
        %(indigenous_group)s, %(indigenous_details)s, %(father_name)s, %(father_occupation)s,
        %(father_income)s, %(father_contact)s, %(mother_name)s, %(mother_occupation)s,
        %(mother_income)s, %(mother_contact)s, %(guardian_name)s, %(guardian_relationship)s,
        %(guardian_occupation)s, %(guardian_income)s, %(guardian_contact)s, %(school_name)s,
        %(school_address)s, %(lrn)s, %(disability)s, %(disability_details)s, %(facebook)s, %(time)s
    )
    """
    cursor.execute(sql, data)
    db.commit()

    # After saving, stay on the same page
    return redirect(url_for('enroll'))

# ---------- MAIN ----------
if __name__ == '__main__':
    app.run(debug=True)
