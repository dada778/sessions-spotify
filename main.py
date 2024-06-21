import spotipy
from spotipy.oauth2 import SpotifyOAuth

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 設置 API 認證範圍
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# 加載憑證
creds = ServiceAccountCredentials.from_json_keyfile_name("/Desktop/data/your file.json", scope)

# 授權並打開 Google 試算表
client = gspread.authorize(creds)
spreadsheet = client.open("你的試算表名稱")

# 選擇工作表
#sheet = spreadsheet.worksheet("Sheet1")  # 或者使用名稱，如：spreadsheet.worksheet("工作表名稱")
# 使用工作表索引访问工作表
sheet = spreadsheet.get_worksheet(0)  # 0 表示第一个工作表

# 獲取某一列數據（例如第一列）
column_data = sheet.col_values(2)  # 1 表示第一列

# 打印數據
#print(column_data[2])


# 填寫你的Spotify API憑證
CLIENT_ID = 'your cilint id'
CLIENT_SECRET = 'your CLIENT_SECRET'
REDIRECT_URI = 'http://localhost:8888/callback' #把這串直接貼到 spotify dev REDIRECT_URI

# 設置Spotipy OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-public"))

# 獲取用戶ID
user_id = sp.current_user()["id"]

# 歌單名稱和描述
playlist_name = "你要的歌單名稱"
playlist_description = "你對歌單的描述"

# 你想要添加到歌單的Spotify歌曲網址
track_urls = []

for url in column_data[1:]:
    track_urls.append(url)

print(track_urls)

# 創建歌單
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, description=playlist_description)
playlist_id = playlist["id"]

# 添加歌曲到歌單
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=track_urls)

print(f"Playlist '{playlist_name}' created successfully with tracks added!")

