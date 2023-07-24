from flask import Flask,request,jsonify,render_template,url_for,redirect
import requests
from main import helper
from dotenv import load_dotenv
import os

app=Flask(__name__)

entered_url=""

#@app.route('/')
#def home():
    #return render_template('index.html')

#@app.route('/search',methods=['POST'])
#def search():
    #url=request.form.get('url')
    #return redirect(url_for('result', url=url))
def configure():
    load_dotenv()    
    
@app.route('/', methods=['GET', 'POST'])
def index():
    global entered_url
    if request.method == 'POST':
        # Get the URL from the form input
        entered_url = request.form.get('url')
        # Redirect to the result route with the URL as a parameter
        return redirect('/result')
    return render_template('index.html')    
    

@app.route('/result')
def result():
   
    configure()
    global entered_url
    url=entered_url
    video_Id=helper.videoid(url,os.getenv('api_key'))
    channel_Id=helper.channelid(url,os.getenv('api_key'))
    videodata=helper.video_data(url,os.getenv('api_key'))
    list_of_videodata=list(videodata)
    Published=list_of_videodata[0]
    Title_of_video=list_of_videodata[1]
    Description_of_video=list_of_videodata[2]
    Channel_Title=list_of_videodata[3]
    channeldata=helper.channel_stats(channel_Id,os.getenv('api_key'))
    list_of_channeldata=list(channeldata)
    Total_no_videos=list_of_channeldata[0]
    No_of_subcribers=list_of_channeldata[1]
    Total_views=list_of_channeldata[2]
    
    commentdata=helper.comment(video_Id,os.getenv('api_key'))
    
    
    
    return render_template('result.html',Total_no_videos=Total_no_videos,Subscribers=No_of_subcribers,Views=Total_views,Published=Published,Title_of_video=Title_of_video,Description_of_video=Description_of_video,Channel_Title=Channel_Title,commentdata=commentdata)






if __name__=='__main__':
    app.run(debug=True)