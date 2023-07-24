import requests


def video_data(url,api_key):
    video_id=url[32:]
    video_info_url=f"https://youtube.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id={video_id}&key={api_key}"
    video_info_response=requests.get(video_info_url)
    video_info_data=video_info_response.json()
    video_info_big_box=video_info_data['items']
    published_At=video_info_big_box[0]['snippet']['publishedAt']
    title_of_video=video_info_big_box[0]['snippet']['title']
    description_of_video=video_info_big_box[0]['snippet']['description']
    channel_title=video_info_big_box[0]['snippet']['channelTitle']
    channel_id=video_info_big_box[0]['snippet']['channelId']
    Statistics_of_video=video_info_big_box[0]['statistics']
    return published_At,title_of_video,description_of_video,channel_title,channel_id


def channel_stats(channel_id,api_key):
    link=f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}"

    channel= requests.get(link)
    channel_data=channel.json()
    channel_info=channel_data['items'][0]['statistics']
    Total_video=channel_data['items'][0]['statistics']['videoCount']
    Subcribers=channel_data['items'][0]['statistics']['subscriberCount']
    Total_view=channel_data['items'][0]['statistics']['viewCount']
    return Total_video,Subcribers,Total_view

def comment(video_id,api_key):
    list_of_comment=[]
    comment_url=f"https://youtube.googleapis.com/youtube/v3/commentThreads?part=snippet,replies&videoId={video_id}&key={api_key}"
    comment_response=requests.get(comment_url)
    comments_data=comment_response.json()
    comments=[item["snippet"]["topLevelComment"]["snippet"]["textOriginal"] for item in comments_data["items"]]
    big_box=comments_data["items"]
    for i in range(len(big_box)):
        list_of_comment.append(big_box[i]['snippet']['topLevelComment']['snippet']['textOriginal'])
    return list_of_comment

def comments(list_of_comment):
    for i in range(len(list_of_comment)):
        return list_of_comment[i]
    
def channelid(url,api_key):
    video_id=url[32:]
    video_info_url=f"https://youtube.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id={video_id}&key={api_key}"
    video_info_response=requests.get(video_info_url)
    video_info_data=video_info_response.json()
    video_info_big_box=video_info_data['items']
    #print(video_info_big_box)
    channel_id=video_info_big_box[0]['snippet']['channelId']
    return channel_id

def videoid(url,api_key):
    
    video_id=url[32:]
    return video_id