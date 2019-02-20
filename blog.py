from flask import Flask,render_template,url_for,redirect
from forms import SignInForm,SignUpForm
app = Flask(__name__)
app.config['SECRET_KEY'] = "Yash1234"


@app.route("/home")
def home():
            return render_template('home.html')

@app.route("/about")
def about():
            return render_template('about.html',title="About")

@app.route("/signup",methods=['GET','POST'])
def signup():
            sform = SignUpForm()
            if sform.validate_on_submit():
                #flash('Account created for {form.username.data}!', 'success')
                return redirect(url_for('home'))
            return render_template('signup.html',title="Sign Up",form=sform)

@app.route("/signin")
def signin():
            sform = SignInForm()
            return render_template('signin.html',title="Sign In",form=sform)
