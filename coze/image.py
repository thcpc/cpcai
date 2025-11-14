import requests


class Image:
    def download(self, urls: list[str]):
        for url in urls:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            try:
                # 发送GET请求获取图片数据
                response = requests.get(url, headers=headers, timeout=10)
                # 检查请求是否成功（状态码200表示成功）
                response.raise_for_status()
                save_path = url.split("/")[-1]
                # 以二进制模式写入文件（图片是二进制数据）
                with open(save_path, 'wb') as f:
                    f.write(response.content)  # response.content是二进制内容

                print(f"图片已保存至：{save_path}")

            except Exception as e:
                print(f"下载失败：{e}")  # 捕获异常（如网络错误、URL无效等）


if __name__ == '__main__':
    test_urls = [
        {"height": 1080, "url": "https://i2.hdslb.com/bfs/archive/4ad57acbd684054fb721d4d49e2ff098bd516e92.jpg",
         "width": 1920},
        {"height": 1080, "url": "https://content-assets.eneba.games/clp/08af2b1a-6438-4374-af61-479c2f308d99.jpg",
         "width": 1920},
        {"height": 1080, "url": "https://cdn.gamer-network.net/2018/metabomb/codblackoutfastcollapseguide.jpg",
         "width": 1920},
        {"height": 1439, "url": "https://i2.hdslb.com/bfs/archive/b6ff690abb2e13565c2bad49204860b85f98a868.jpg",
         "width": 2559},
        {"height": 1440, "url": "https://i0.hdslb.com/bfs/archive/a685827b805fc953a52f09eefeff3c9ec607871b.jpg",
         "width": 2560},
        {"height": 1080, "url": "https://i1.hdslb.com/bfs/archive/0619cbeb79122bb72d82000160de341c7890e142.jpg",
         "width": 1728}, {"height": 1080,
                          "url": "https://pic.biubiu001.com/gamebase/gamedb/res/20241102/4/4/be59c023415188e100a6eec675b37ca3.jpeg",
                          "width": 1920},
        {"height": 1080, "url": "https://i2.hdslb.com/bfs/archive/3f5d96f0f3f321260e04fea223e1cab8b7de79c9.jpg",
         "width": 1920},
        {"height": 941, "url": "https://i1.hdslb.com/bfs/archive/07ae7abc8137c4299b153fc045c9531b41a6929f.jpg",
         "width": 1672},
        {"height": 1080, "url": "https://i0.hdslb.com/bfs/archive/ce3db47002fcda63a25c17e5f64cdfae37db91ae.jpg",
         "width": 1920},
        {"height": 3000, "url": "https://imgessl.kugou.com/stdmusic/20210123/20210123001200774428.jpg", "width": 3000},
        {"height": 988, "url": "https://i1.hdslb.com/bfs/archive/d405f3f17c37e3f7731ceced699b949ae79726b0.jpg",
         "width": 1758},
        {"height": 1200, "url": "https://pic.rmb.bdstatic.com/bjh/news/516138e11bbe4cdfae81e1e991962c86.jpeg",
         "width": 1920},
        {"height": 1080, "url": "https://i2.hdslb.com/bfs/archive/d4b55938431e7f1ce4ed2d67f65c16ce63501de0.jpg",
         "width": 1920},
        {"height": 1440, "url": "https://i2.hdslb.com/bfs/archive/41e451842d01e678b51f907ee848e8b380f58614.jpg",
         "width": 2560},
        {"height": 1348, "url": "https://i1.hdslb.com/bfs/archive/57a69ba5e99e32afe4cf315ee7134f42bdd863c2.jpg",
         "width": 2398},
        {"height": 2048, "url": "https://imgessl.kugou.com/stdmusic/20250101/20250101201507898815.jpg", "width": 2048},
        {"height": 1080,
         "url": "https://shared.cdn.queniuqe.com/store_item_assets/steam/apps/2933620/bf0acb9de1cfda4522823bf019a12f577725bd11/ss_bf0acb9de1cfda4522823bf019a12f577725bd11.1920x1080.jpg?t=1754583050",
         "width": 1920},
        {"height": 1080, "url": "https://i2.hdslb.com/bfs/archive/3d74758d351856abe32de74f5ea7163b97dfaa55.jpg",
         "width": 1920},
        {"height": 1080, "url": "https://content-assets.eneba.games/clp/ab134028-b1e2-4e73-ac8f-194fa88b091b.jpg",
         "width": 1920}, {"height": 1080,
                          "url": "https://www.callofduty.com/content/dam/atvi/callofduty/cod-touchui/blog/body/bo6/season-02/BO6-SEASON-02-ANNOUNCEMENT-001.jpg",
                          "width": 1920}, {"height": 900,
                                           "url": "https://xqieua.bay.livefilestore.com/y1pFhUavS9tzNqpcSUk8xvfZlSvcZE-TxjUG79TUAGzjyqRMAPtWOLJQhOOLNaMR9ox6nvTHUY3sWsQ4cXI7sCgJ9kaDY5B4qw7/1.jpg?psid=1",
                                           "width": 1600}, {"height": 476,
                                                            "url": "https://support.activision.com/servlet/servlet.ImageServer?id=0150B000005m14b&oid=00DU0000000HMgw&lastMod=1472789632000",
                                                            "width": 847},
        {"height": 948, "url": "https://i1.hdslb.com/bfs/archive/9b5303132833b86142a4a67c5c789336c7098683.jpg",
         "width": 1685},
        {"height": 576, "url": "https://ww4.sinaimg.cn/large/0068Hy18gw1exny394ulbj30sg0g00yx.jpg", "width": 1024},
        {"height": 1080, "url": "https://i0.hdslb.com/bfs/archive/850b19d2ba679faae4c21107e6496dfe5c29a756.jpg",
         "width": 1920}, {"height": 1440,
                          "url": "https://t15.baidu.com/it/u=1159042267,2282092163&fm=225&app=113&f=JPEG?w=2560&h=1440&s=1F846D854C9030D2523119040300F0D1",
                          "width": 2560},
        {"height": 720, "url": "https://i1.hdslb.com/bfs/archive/ae78a65987565c91ca2b9382ec7b9be06ed53214.jpg",
         "width": 1280}, {"height": 2160,
                          "url": "https://www.gamehackstudios.com/wp-content/uploads/2014/11/Call-of-Duty-Advanced-Warfare-full-game-download-for-free-crack-torrent-working-2014-2015.jpg",
                          "width": 3840},
        {"height": 1080, "url": "https://news.mydrivers.com/Img/20100529/12264837.jpg", "width": 1920}]
    Image().download([url["url"] for url in test_urls])
