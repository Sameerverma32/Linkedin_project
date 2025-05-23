from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio


app = Flask(__name__)

df = pd.read_csv('Linkedindataset_new.csv')

@app.route('/login')
def login():
    return render_template('login.html')

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
    fig = px.bar(df, x='company', y='title', title='Most Common Job Titles')
    graph4_html = pio.to_html(fig, full_html=False)
    return graph4_html

def senioritybyemployment():
    fig = px.histogram(df, x='Seniority level', y='Employment type', title='Seniority Level by Employment Type', color='Employment type')
    graph5_html = pio.to_html(fig, full_html=False)
    return graph5_html

def education_levels():
    fig = px.pie(df, names='education', hole=0.4, title='Education Requirements')
    graph6_html = pio.to_html(fig, full_html=False)
    return graph6_html

def common_eductaion():
    fig = px.bar(df, x='education', y='description',title='Top Most Common Education Requirements', color='Industries')
    graph7_html = pio.to_html(fig, full_html=False)
    return graph7_html

def education_requirements():
    fig = px.box(df, x='education', y='company',title='Distribution of education Requirements')
    graph8_html = pio.to_html(fig, full_html=False)
    return graph8_html

def breakdown_by_education():
    fig = px.bar(df, x='Seniority level', y='education', title='Breakdown of Education within Seniority Levels')
    graph9_html = pio.to_html(fig, full_html=False)
    return graph9_html

def education_requirement_by_industries():
    fig = px.bar(df, x='education', y='Industries',title='Education Requirements across Industries', color='education')
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
    fig = px.bar(df, x='Industries', title='Top Industries by Job Posts')
    graph14_html = pio.to_html(fig, full_html=False)
    return graph14_html

def experience_by_industries():
    fig = px.histogram(df, x='months_experience', y='Industries', title='Experience Distribution by Industry')
    graph15_html = pio.to_html(fig, full_html=False)
    return graph15_html

def job_distribution_by_experience():
    fig = px.histogram(df, x='Job function', y='months_experience', title='Job Function Distribution by Experience')
    graph16_html = pio.to_html(fig, full_html=False)
    return graph16_html

def education_by_industries():
    fig = px.histogram(df, x='Job function', y='months_experience', title='Job Function Distribution by Experience')
    graph17_html = pio.to_html(fig, full_html=False)
    return graph17_html

def Job_Post_Distribution_by_Industry_by_Job_Function_by_Seniority_Level():
    fig = px.sunburst(df, path=['Industries', 'Job function', 'Seniority level'], values='post_id', title='Job Post Distribution by Industry, Job Function, and Seniority Level')
    graph18_html = pio.to_html(fig, full_html=False)
    return graph18_html

def treemap_of_job_posts():
    fig = px.treemap(df, path=['Industries', 'Job function', 'Seniority level'], values='post_id', title='Treemap of Job Posts')
    graph19_html = pio.to_html(fig, full_html=False)
    return graph19_html

def expreance_by_months():
    fig = px.histogram(df, x='months_experience', nbins=20, title='Distribution of Experience (Months)')
    graph20_html = pio.to_html(fig, full_html=False)
    return graph20_html

def  education_level_proportion():
    fig = px.pie(df, names='education', title='Education Level Proportion')
    graph21_html = pio.to_html(fig, full_html=False)
    return graph21_html

def experience_by_title():
    fig = px.scatter(df, x='months_experience', y='title', title='Experience by Title')
    graph22_html = pio.to_html(fig, full_html=False)
    return graph22_html

def function_beakdown_by_industries():
    fig = px.treemap(df, path=['Job function', 'title', 'education', 'Industries'], title='Industry & Function Breakdown')
    graph23_html = pio.to_html(fig, full_html=False)
    return graph23_html
    
def experience_by_education():
    fig = px.violin(df, x='education', y='months_experience', box=True, title='Experience by Education')
    graph24_html = pio.to_html(fig, full_html=False)
    return graph24_html
    
def experience_per_local():
    fig = px.histogram(df, x='months_experience', color='location', title='Experience per Location')
    graph25_html = pio.to_html(fig, full_html=False)
    return graph25_html
    
def  experience_vs_company(): 
    fig = px.scatter(df, x='months_experience', y='company', title='Experience vs Company')  
    graph26_html = pio.to_html(fig, full_html=False)
    return graph26_html

def experience_by_employment_type():
    fig = px.histogram(df, x='months_experience', color='Employment type', title='Experience by Employment Type')
    graph27_html = pio.to_html(fig, full_html=False)
    return graph27_html

def location_by_seniority():
    fig = px.sunburst(df, path=['location', 'Employment type', 'Seniority level'], title='Sunburst: Location > Employment > Seniority')
    graph28_html = pio.to_html(fig, full_html=False)
    return graph28_html

#analysis pages 
@app.route('/job_analysis')
def job_analysis():
    graph1_html = emplyment_types()
    graph2_html = seniority_levels()
    graph3_html = experiencevsseniority()
    graph4_html = job_titles()
    graph5_html = senioritybyemployment()
    return render_template('job_analysis.html', graph1_html=graph1_html, graph2_html=graph2_html, graph3_html=graph3_html, graph4_html=graph4_html, graph5_html=graph5_html)
    return render_template('job_analysis.html', graph1_html=graph1_html, graph2_html=graph2_html, graph3_html=graph3_html, graph4_html=graph4_html)
    return render_template('job_analysis.html', graph1_html=graph1_html, graph2_html=graph2_html, graph3_html=graph3_html)
    return render_template('job_analysis.html', graph1_html=graph1_html, graph2_html=graph2_html)
    return render_template('job_analysis.html', graph1_html=graph1_html)

@app.route('/education_analysis')
def education_analysis():
    graph6_html = education_levels()
    graph7_html = common_eductaion()
    graph8_html = education_requirements()
    graph9_html = breakdown_by_education()
    graph10_html = education_requirement_by_industries()
    graph11_html = education_by_employment()
    return render_template('education_analysis.html', graph6_html=graph6_html, graph7_html=graph7_html, graph8_html=graph8_html, graph9_html=graph9_html, graph10_html=graph10_html, graph11_html=graph11_html)
    return render_template('education_analysis.html', graph6_html=graph6_html, graph7_html=graph7_html, graph8_html=graph8_html, graph9_html=graph9_html, graph10_html=graph10_html)
    return render_template('education_analysis.html', graph6_html=graph6_html, graph7_html=graph7_html, graph8_html=graph8_html, graph9_html=graph9_html)
    return render_template('education_analysis.html', graph6_html=graph6_html, graph7_html=graph7_html, graph8_html=graph8_html)
    return render_template('education_analysis.html', graph6_html=graph6_html, graph7_html=graph7_html)
    return render_template('education_analysis.html', graph6_html=graph6_html)

@app.route('/industry_analysis')
def industry_analysis():
    graph12_html = seniority_breakdown()
    graph13_html = experience_vs_industries()
    graph14_html = industries_by_posts()
    graph15_html = experience_by_industries()
    graph16_html = job_distribution_by_experience()
    graph17_html = education_by_industries()
    graph18_html = Job_Post_Distribution_by_Industry_by_Job_Function_by_Seniority_Level()
    graph19_html = treemap_of_job_posts()
    graph20_html = expreance_by_months()
    graph21_html = education_level_proportion()
    graph22_html = experience_by_title()
    graph23_html = function_beakdown_by_industries()
    graph24_html = experience_by_education()
    graph25_html = experience_per_local()
    graph26_html = experience_vs_company()
    graph27_html = experience_by_employment_type()
    graph28_html = location_by_seniority()
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html, graph14_html=graph14_html, graph15_html=graph15_html, graph16_html=graph16_html, graph17_html=graph17_html, graph18_html=graph18_html, graph19_html=graph19_html, graph20_html=graph20_html, graph21_html=graph21_html, graph22_html=graph22_html, graph23_html=graph23_html, graph24_html=graph24_html, graph25_html=graph25_html, graph26_html=graph26_html, graph27_html=graph27_html, graph28_html=graph28_html)
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html, graph14_html=graph14_html, graph15_html=graph15_html, graph16_html=graph16_html, graph17_html=graph17_html, graph18_html=graph18_html, graph19_html=graph19_html, graph20_html=graph20_html, graph21_html=graph21_html, graph22_html=graph22_html, graph23_html=graph23_html, graph24_html=graph24_html, graph25_html=graph25_html, graph26_html=graph26_html, graph27_html=graph27_html)
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html, graph14_html=graph14_html, graph15_html=graph15_html, graph16_html=graph16_html, graph17_html=graph17_html, graph18_html=graph18_html, graph19_html=graph19_html, graph20_html=graph20_html, graph21_html=graph21_html, graph22_html=graph22_html, graph23_html=graph23_html, graph24_html=graph24_html, graph25_html=graph25_html, graph26_html=graph26_html)
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html, graph14_html=graph14_html, graph15_html=graph15_html, graph16_html=graph16_html, graph17_html=graph17_html, graph18_html=graph18_html, graph19_html=graph19_html, graph20_html=graph20_html, graph21_html=graph21_html, graph22_html=graph22_html, graph23_html=graph23_html, graph24_html=graph24_html, graph25_html=graph25_html)
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html, graph14_html=graph14_html, graph15_html=graph15_html, graph16_html=graph16_html, graph17_html=graph17_html, graph18_html=graph18_html, graph19_html=graph19_html, graph20_html=graph20_html, graph21_html=graph21_html, graph22_html=graph22_html, graph23_html=graph23_html, graph24_html=graph24_html)
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html, graph14_html=graph14_html, graph15_html=graph15_html, graph16_html=graph16_html, graph17_html=graph17_html, graph18_html=graph18_html, graph19_html=graph19_html, graph20_html=graph20_html, graph21_html=graph21_html, graph22_html=graph22_html, graph23_html=graph23_html)
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html, graph14_html=graph14_html, graph15_html=graph15_html, graph16_html=graph16_html, graph17_html=graph17_html, graph18_html=graph18_html, graph19_html=graph19_html, graph20_html=graph20_html, graph21_html=graph21_html, graph22_html=graph22_html)
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html, graph14_html=graph14_html, graph15_html=graph15_html, graph16_html=graph16_html, graph17_html=graph17_html, graph18_html=graph18_html, graph19_html=graph19_html, graph20_html=graph20_html, graph21_html=graph21_html)
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html, graph14_html=graph14_html, graph15_html=graph15_html, graph16_html=graph16_html, graph17_html=graph17_html, graph18_html=graph18_html, graph19_html=graph19_html, graph20_html=graph20_html)
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html, graph14_html=graph14_html, graph15_html=graph15_html, graph16_html=graph16_html, graph17_html=graph17_html, graph18_html=graph18_html, graph19_html=graph19_html)
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html, graph14_html=graph14_html, graph15_html=graph15_html, graph16_html=graph16_html, graph17_html=graph17_html, graph18_html=graph18_html)
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html, graph14_html=graph14_html, graph15_html=graph15_html, graph16_html=graph16_html, graph17_html=graph17_html)
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html, graph14_html=graph14_html, graph15_html=graph15_html, graph16_html=graph16_html)
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html, graph14_html=graph14_html, graph15_html=graph15_html)
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html, graph14_html=graph14_html)
    return render_template('industry_analysis.html', graph12_html=graph12_html, graph13_html=graph13_html)
    return render_template('industry_analysis.html', graph12_html=graph12_html)
    

if __name__ == '__main__':
    app.run(debug=True)