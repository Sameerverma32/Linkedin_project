from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this to a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(200))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create all database tables
with app.app_context():
    db.create_all()

df = pd.read_csv('Linkedindataset_new.csv')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash('Successfully logged in!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Invalid email or password', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    
    if User.query.filter_by(email=email).first():
        flash('Email already exists')
        return redirect(url_for('login'))
    
    user = User(name=name, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    
    login_user(user)
    return redirect(url_for('index'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out!', 'success')
    return redirect(url_for('login'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

#graphs functions
def emplyment_types():
    fig = px.pie(df, names='Employment type', title='Distribution of Employment Types')
    graph1_html = pio.to_html(fig, full_html=False)
    return graph1_html

def seniority_levels():
    fig = px.box(df, x='Seniority level', y='months_experience', title='Distribution of Seniority Levels')
    graph2_html = pio.to_html(fig, full_html=False)
    return graph2_html

def experiencevsseniority():
    fig = px.scatter(df, x='months_experience', y='Seniority level',color='Industries', title='Experience vs Seniority by Industry')
    graph3_html = pio.to_html(fig, full_html=False)
    return graph3_html

def job_titles():
    fig = px.bar(df.head(10), x='company', y='title', title='Most Common Job Titles')
    graph4_html = pio.to_html(fig, full_html=False)
    return graph4_html

def senioritybyemployment():
    fig = px.box(df.head(20), x='Seniority level', y='Employment type', title='Seniority Level by Employment Type')
    graph5_html = pio.to_html(fig, full_html=False)
    return graph5_html

def education_levels():
    fig = px.pie(df, names='education', hole=0.4, title='Education Requirements')
    graph6_html = pio.to_html(fig, full_html=False)
    return graph6_html

def common_eductaion():
    fig = px.bar(df, x='education', y='description',title='Top Most Common Education across Industry', color='Industries')
    graph7_html = pio.to_html(fig, full_html=False)
    return graph7_html

def education_requirements():
    fig = px.box(df, x='education', y='company',title='Distribution of Qualification Requirements')
    graph8_html = pio.to_html(fig, full_html=False)
    return graph8_html

def breakdown_by_education():
    fig = px.box(df, x='Seniority level', y='education', title='Breakdown of Education within Seniority Levels')
    graph9_html = pio.to_html(fig, full_html=False)
    return graph9_html

def education_requirement_by_industries():
    fig = px.bar(df.head, x='education', y='Industries',title='Education Requirements across Industries', color='education')
    graph10_html = pio.to_html(fig, full_html=False)
    return graph10_html

def education_by_employment():
    fig = px.bar(df, x='Employment type', y='education', title='Education Requirements by Employment Type')
    graph11_html = pio.to_html(fig, full_html=False)
    return graph11_html

def seniority_breakdown():
    fig = px.pie(df, names='Seniority level', title='Seniority Level Breakdown')
    graph12_html = pio.to_html(fig, full_html=False)
    return graph12_html

def experience_vs_industries():
    fig = px.scatter(df, x='months_experience', y='Industries', color='Industries', title='Experience vs Industries') 
    graph13_html = pio.to_html(fig, full_html=False)
    return graph13_html

def industries_by_posts():
    fig = px.bar(df.head(10), x='Industries', title='Top 10 Industries by Job Posts')
    graph14_html = pio.to_html(fig, full_html=False)
    return graph14_html

def experience_by_industries():
    fig = px.histogram(df, x='months_experience', y='Industries', title='Experience Distribution by Industry')
    graph15_html = pio.to_html(fig, full_html=False)
    return graph15_html

def job_distribution_by_experience():
    fig = px.histogram(df.head(20), x='Job function', y='months_experience', title='Job Function Distribution by Experience')
    graph16_html = pio.to_html(fig, full_html=False)
    return graph16_html

def Job_Post_Distribution_by_Industry_by_Job_Function_by_Seniority_Level():
    fig = px.sunburst(df, path=['Industries', 'Job function', 'Seniority level'], values='post_id', title='Job Post Distribution by Industry, Job Function, and Seniority Level')
    graph17_html = pio.to_html(fig, full_html=False)
    return graph17_html

def treemap_of_job_posts():
    fig = px.treemap(df, path=['Industries', 'Job function', 'Seniority level'], values='post_id', title='Treemap of Job Posts')
    graph18_html = pio.to_html(fig, full_html=False)
    return graph18_html

def expreance_by_months():
    fig = px.histogram(df, x='months_experience', nbins=20, title='Distribution of Experience (Months)', color='Employment type')
    graph19_html = pio.to_html(fig, full_html=False)
    return graph19_html

def  education_level_proportion():
    fig = px.pie(df, names='education', title='Education Level Proportion')
    graph20_html = pio.to_html(fig, full_html=False)
    return graph20_html

def experience_by_title():
    fig = px.scatter(df, x='months_experience', y='title', title='Experience by Title')
    graph21_html = pio.to_html(fig, full_html=False)
    return graph21_html
    
def experience_by_education():
    fig = px.violin(df, x='education', y='months_experience', box=True, title='Experience by Education')
    graph22_html = pio.to_html(fig, full_html=False)
    return graph22_html
    
def experience_per_local():
    fig = px.histogram(df, x='months_experience', color='location', title='Experience per Location')
    graph23_html = pio.to_html(fig, full_html=False)
    return graph23_html
    
def  experience_vs_company(): 
    fig = px.scatter(df, x='months_experience', y='company', title='Experience vs Company')  
    graph24_html = pio.to_html(fig, full_html=False)
    return graph24_html

def experience_by_employment_type():
    fig = px.histogram(df, x='months_experience', color='Employment type', title='Experience by Employment Type')
    graph25_html = pio.to_html(fig, full_html=False)
    return graph25_html

def location_by_seniority():
    fig = px.sunburst(df, path=['location', 'Employment type', 'Seniority level'], title='Sunburst: Location > Employment > Seniority')
    graph26_html = pio.to_html(fig, full_html=False)
    return graph26_html

#analysis pages 
@app.route('/job_analysis')
@login_required
def job_analysis():
    graph1 = emplyment_types()
    graph2 = seniority_levels()
    graph3 = experiencevsseniority()
    graph4 = job_titles()
    graph5 = senioritybyemployment()
    return render_template('job_analysis.html', graph1_html=graph1, graph2_html=graph2, graph3_html=graph3,graph4_html=graph4,graph5_html=graph5)

@app.route('/education_analysis')
@login_required
def education_analysis():
    graph6_html = education_levels()
    graph7_html = common_eductaion()
    graph8_html = education_requirements()
    graph9_html = breakdown_by_education()
    graph10_html = education_requirement_by_industries()
    graph11_html = education_by_employment()
    return render_template('education_analysis.html', graph6_html=graph6_html, graph7_html=graph7_html, graph8_html=graph8_html, graph9_html=graph9_html, graph10_html=graph10_html, graph11_html=graph11_html)


@app.route('/industry_analysis')
@login_required
def industry_analysis():
    graph12_html = seniority_breakdown()
    graph13_html = experience_vs_industries()
    graph14_html = industries_by_posts()
    graph15_html = experience_by_industries()
    graph16_html = job_distribution_by_experience()
    graph17_html = Job_Post_Distribution_by_Industry_by_Job_Function_by_Seniority_Level()
    graph18_html = treemap_of_job_posts()
    graph19_html = expreance_by_months()
    graph20_html = education_level_proportion()
    graph21_html = experience_by_title()
    graph22_html = experience_by_education()
    graph23_html = experience_per_local()
    graph24_html = experience_vs_company()
    graph25_html = experience_by_employment_type()
    graph26_html = location_by_seniority()
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html, graph14_html=graph14_html, graph15_html=graph15_html, graph16_html=graph16_html, graph17_html=graph17_html, graph18_html=graph18_html, graph19_html=graph19_html, graph20_html=graph20_html, graph21_html=graph21_html, graph22_html=graph22_html, graph23_html=graph23_html, graph24_html=graph24_html, graph25_html=graph25_html, graph26_html=graph26_html)



if __name__ == '__main__':
    app.run(debug=True)
    