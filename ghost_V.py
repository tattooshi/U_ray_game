import pyxel
import random
move = [0,0,1,1,1,2,2,2,3,3,3,3,2,2,2,1,1,1,0,0,0,-1,-1,-1,-2,-2,-2,-3,-3,-3,-3,-2,-2,-2,-1,-1,-1]
class App:
    def __init__(self):     
        # 画面の大きさ
        pyxel.init(200, 200, "幽霊退治",fps=20) # fps は画面が切り替わる頻度        # 初期画面を         
        
        #音楽
        self.music_flug =False        

        # マウスを使えるようにする
        pyxel.mouse(True)
        
        # リソースファイルの読み込み
        pyxel.load("chiko_game.pyxres")
                      
        # 幽霊の座標
        self.ghost1_x, self.ghost1_y = 300, 300    # 幽霊1 の座標
        self.ghost2_x, self.ghost2_y = 300, 300    # 幽霊2 の座標
        self.ghost3_x, self.ghost3_y = 300, 300    # 幽霊3 の座標
        self.ghost4_x, self.ghost4_y = 300, 300    # 幽霊4 の座標
        self.ghost5_x, self.ghost5_y = 300, 300    # 死神の座標
        self.ghost6_x, self.ghost6_y = 300, 300    # 透明人間の座標
        
        
        # ヒットしたときの座標
        self.hitt1_x, self.hitt1_y = 300, 300    # ヒット幽霊1 の座標
        self.hitt2_x, self.hitt2_y = 300, 300    # ヒット幽霊2 の座標
        self.hitt3_x, self.hitt3_y = 300, 300    # ヒット幽霊3 の座標 
        self.hitt4_x, self.hitt4_y = 300, 300    # ヒット幽霊4 の座標  
        self.hitt5_x, self.hitt5_y = 300, 300    # ヒット死神の座標
        self.hitt6_x, self.hitt6_y = 300, 300    # ヒット透明人間の座標
        self.hitt7_x, self.hitt7_y = 300, 300    # ヒット砂時計の座標
    
        
        #砂時計の座標
        self.sunax, self.sunay=300,300
        self.suna_x1 = random.randint(40,160)  # 1回目の砂時計x座標　
        self.suna_x2 = random.randint(40,160)  # 2回目の砂時計x座標
        
        # 人魂1の値（変数を定義)
        self.bx = 100   # x 座標用
        self.by = 100   # y 座標用
        self.vx = 1   # x スピード用
        self.vy = 0.5   # y スピード用
        
        # 人魂2の値（変数を定義)
        self.cx = 150   # x 座標用
        self.cy = 50   # y 座標用
        self.wx = -0.4   # x スピード用
        self.wy = -0.6   # y スピード用
        
        # 時間のカウント
        self.time = 30   # 現在の時間
        self.time_up = 50 # タイムアップまでの時間
        self.hit_1_time, self.hit_2_time, self.hit_3_time, self.hit_4_time,self.hit_5_time,self.hit_6_time, self.hit_7_time,self.hit_8_time = 0,0,0,0,0,0,0,0 #########################
        
        # 透明人間の色
        self.colk = 7 
        # ヒットの座標
        self.hitt_x, self.hitt_y = 300, 300    # ヒット の座標
        
        # スコア表示
        self.score = 0
        
        pyxel.run(self.update, self.draw)

    def update(self):
         # Q ボタンで終了
        if pyxel.btnp(pyxel.KEY_Q): # Qキーで終了
            pyxel.quit()
        
        if self.music_flug == False:
            pyxel.playm(0,loop=True)
            self.music_flug=True
        
        # 現在の時間を経過させる
        self.time += 1
            
        # 幽霊出現時間のサイクルとタイミング
        if self.time % 60 == 10:
            self.ghost1_x, self.ghost1_y = random.randint(20, 180), random.randint(20, 180)    # 幽霊1 の座標
        if self.time % 70 == 5:
            self.ghost2_x, self.ghost2_y = random.randint(20, 180), random.randint(20, 180)    # 幽霊2 の座標
        if self.time % 80 == 20:
            self.ghost3_x, self.ghost3_y = random.randint(20, 180), random.randint(20, 180)    # 幽霊3 の座標
        if self.time % 120 == 40:
            self.ghost4_x, self.ghost4_y = random.randint(20, 180), random.randint(20, 180)    # 幽霊4 の座標
        if self.time % 140 == 50:
            self.ghost5_x, self.ghost5_y = random.randint(20, 180), random.randint(20, 180)    # 死神 の座標
        if self.time % 300 == 10:
            self.ghost6_x, self.ghost6_y = random.randint(20, 180), random.randint(140, 180)    # 透明人間 の座標
                        
        if self.time % 60 == 0:
            self.ghost1_x, self.ghost1_y = 300, 300    # 幽霊1 の座標
        if self.time % 70 == 0:
            self.ghost2_x, self.ghost2_y = 300, 300    # 幽霊2 の座標
        if self.time % 80 == 0:
            self.ghost3_x, self.ghost3_y = 300, 300    # 幽霊3 の座標
        if self.time % 120 == 0:
              self.ghost4_x, self.ghost4_y = 300, 300    # 幽霊4 の座標
        if self.time % 140 == 0:
            self.ghost5_x, self.ghost5_y = 300, 300    # 死神の座標
        if self.time % 300 == 0:
            self.ghost6_x, self.ghost6_y = 300, 300    # 透明人間の座標
            
        #砂時計の動き
        if self.time >= 800:
            self.sunax=self.suna_x2
            self.sunay+=3
        elif self.time >= 500 and self.time <= 700:
            self.sunax=self.suna_x1
            self.sunay+=2
        else:
            self.sunay= -10

            
        # マウスをクリックしたときの座標
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx = pyxel.mouse_x
            my = pyxel.mouse_y            
            dist1 = ((self.ghost1_x - mx)**2 + (self.ghost1_y - my)**2)**0.5  #幽霊1との距離
            dist2 = ((self.ghost2_x - mx)**2 + (self.ghost2_y - my)**2)**0.5  #幽霊2との距離
            dist3 = ((self.ghost3_x - mx)**2 + (self.ghost3_y - my)**2)**0.5  #幽霊3との距離
            dist4 = ((self.ghost4_x - mx)**2 + (self.ghost4_y - my)**2)**0.5  #幽霊4との距離
            dist5 = ((self.ghost5_x - mx)**2 + (self.ghost5_y - my)**2)**0.5  # 死神との距離
            dist6 = ((self.ghost6_x - mx)**2 + (self.ghost6_y - my)**2)**0.5  # 透明人間との距離
            dist7 = ((self.sunax - mx)**2 + (self.sunay - my)**2)**0.5         # 砂時計との距離
            dist8 = ((self.cx - mx)**2 + (self.cy - my)**2)**0.5         # 眼鏡人魂との距離
            
            if dist5 <= 20:
                self.hitt5_x, self.hitt5_y = self.ghost5_x, self.ghost5_y    # ヒット 幽霊5(死神)の座標
                self.ghost5_x, self.ghost5_y = 300, 300
                self.score -= 100
                self.hit_5_time = self.time  ###########
            elif  dist4<= 25:
                self.hitt4_x, self.hitt4_y = self.ghost4_x, self.ghost4_y    # ヒット 幽霊4の座標
                self.ghost4_x, self.ghost4_y = 300, 300 
                self.score += 30
                self.hit_4_time = self.time ###############
            elif dist3 <= 10:
                self.hitt3_x, self.hitt3_y = self.ghost3_x, self.ghost3_y    # ヒット 幽霊3の座標
                self.ghost3_x, self.ghost3_y = 300, 300 
                self.score += 20
                self.hit_3_time = self.time ##############
            elif dist2 <= 15:
                self.hitt2_x, self.hitt2_y = self.ghost2_x, self.ghost2_y    # ヒット 幽霊2の座標
                self.ghost2_x, self.ghost2_y = 300, 300 
                self.score += 25
                self.hit_2_time = self.time  ###########
            elif dist1 <= 20:
                self.hitt1_x, self.hitt1_y = self.ghost1_x, self.ghost1_y    # ヒット 幽霊1の座標
                self.ghost1_x, self.ghost1_y = 300, 300
                self.score += 30
                self.hit_1_time = self.time  ###########
            elif dist7 <= 20:
                self.hitt7_x, self.hitt7_y = self.sunax, self.sunay    # ヒット 砂時計の座標
                self.sunax, self.sunay = 300, 300
                self.hit_7_time = self.time  ###########
            elif dist6 <= 20:                                         # ヒット 透明人間の座標                    
                self.hitt6_x, self.hitt6_y = self.ghost6_x, self.ghost6_y
                self.ghost6_x, self.ghost6_y = 300, 300
                self.score += 100
                self.hit_6_time = self.time  ###########
            elif dist8 <= 20:                                         # ヒット 眼鏡人魂の座標                    
                self.colk = 0
                self.hit_8_time = self.time  ###########
            else:
                self.score -= 5
                

        #===================================================================================#
        # ヒットされた幽霊が消えるまでの時間設定
        if self.time - 10 >= self.hit_1_time:
                self.hitt1_x, self.hitt1_y = 300, 300    # ヒット幽霊1  ###########
        if self.time - 10 >= self.hit_2_time:
                self.hitt2_x, self.hitt2_y = 300, 300    # ヒット幽霊2  ##########
        if self.time - 10 >= self.hit_3_time:
                self.hitt3_x, self.hitt3_y = 300, 300    # ヒット幽霊3  ##########
        if self.time - 10 >= self.hit_4_time:
                self.hitt4_x, self.hitt4_y = 300, 300    # ヒット幽霊4  ##########
        if self.time - 10 >= self.hit_5_time:
                self.hitt5_x, self.hitt5_y = 300, 300    # ヒット死神 
        if self.time - 20 >= self.hit_6_time:
                self.hitt6_x, self.hitt6_y = 300, 300    # ヒット透明人間 
        if self.time - 40 >= self.hit_7_time:
                self.hitt7_x, self.hitt7_y = 300, 300    # ヒット砂時計 
        if self.time - 100 >= self.hit_8_time:
                self.colk = 7   # ヒット眼鏡人魂の有効時間
        #===================================================================================#
        
        
        
        # 人魂1の動くスピード
        if self.bx >= 193:
            self.vx *= -1
        
        if self.bx <= 7:
            self.vx *= -1
        
        if self.by >= 190:
            self.vy *= -1
        
        if self.by <= 10:
            self.vy *= -1
        
        self.bx += self.vx
        self.by += self.vy
        
        # 人魂2の動くスピード
        if self.cx >= 193:
            self.wx *= -1
        
        if self.cx <= 7:
            self.wx *= -1
        
        if self.cy >= 190:
            self.wy *= -1
        
        if self.cy <= 10:
            self.wy *= -1
        
        self.cx += self.wx
        self.cy += self.wy
                            
                        
    def draw(self):
                
        # pyxel edit chiko_game.pyxres        
        # 画面の色
        pyxel.cls(0)           
        pyxel.blt(-3,105,0,48,152,203,90,0)
        pyxel.blt(20,80,0,64,3,15,9,0) #雲
        pyxel.blt(100,60,0,64,3,15,9,0)
        pyxel.blt(160,70,0,64,3,15,9,0)           # 100 24 123 62
        
        
        # 人魂1を描く
        pyxel.blt(self.bx-7,self.by-10,0,82,25,12,20,0)
        # 人魂2を描く
        pyxel.blt(self.cx-10,self.cy-10,0,86,72,106,92,0)
        
        # 時間で終了
        if self.time_up-self.time/30 <= 0:
            pyxel.rect(0,0,200,200,2)
            pyxel.text(80,60, "TIME UP", 10)   # (始点座標 x, 始点座標 y, 文字（アルファベット限定）, 色)
            pyxel.text(80,80, f"SCORE : {self.score}", 10)   # (始点座標 x, 始点座標 y, 文字（アルファベット限定）, 色)
            if self.score >= 1800:
                pyxel.text(70,130, "You are genius", 10)
                pyxel.blt(150+move[self.time%37],130+move[self.time%37], 0,35,40,25,20,0)   # 大きな幽霊
            elif self.score >= 1500:
                pyxel.text(65,130, "You are not bad", 10) 
                pyxel.blt(150+move[self.time%37],130,0,6,18,20,11,0)     # ネコ 
            else:
                pyxel.text(50,130, "You are not good enough", 10) 
                pyxel.blt(150+move[self.time%37], 130,1 ,63, 14, 43, 50, 0)  # 死神
                
        else:    
            # goastを描く
            pyxel.blt(self.ghost1_x-7, self.ghost1_y-7+move[self.time%37], 0,40,96,15,15,0)    # 小さな幽霊 
            pyxel.blt(self.ghost2_x-12+move[self.time%37], self.ghost2_y-10+move[self.time%37], 0,35,40,25,20,0)  # 大きな幽霊  
            pyxel.blt(self.ghost3_x-9+move[self.time%37], self.ghost3_y-10,0,100,9,24,30,0)     # ネコ
            pyxel.blt(self.ghost4_x-8+move[self.time%37], self.ghost4_y-10,0,38,9,20,13,0)     # 黒ネコ
            pyxel.blt(self.ghost5_x-21, self.ghost5_y-25+move[self.time%37], 1 ,8, 14, 43, 50, 0)   # 死神を描く
            pyxel.blt(self.ghost6_x-7, self.ghost6_y-18, 0 ,152, 15, 15, 36, self.colk)     # 透明人間を描く
            
            # ヒットしたときを描く            
            pyxel.blt(self.hitt1_x-7, self.hitt1_y-7,0,40,112,15,15,0)   # 小さな幽霊
            pyxel.blt(self.hitt2_x-12, self.hitt2_y-10,0,35,64,25,20,0)  # 大きな幽霊            
            pyxel.blt(self.hitt3_x-9, self.hitt3_y-10,0,100,42,23,20,0)    # ネコ
            pyxel.blt(self.hitt4_x-9, self.hitt4_y-10,0,6,35,20,11,0)    # 黒ネコ
            pyxel.blt(self.hitt5_x-21, self.hitt5_y-25,1 ,63, 14, 43, 50,0 ) # 死神
            pyxel.blt(self.hitt6_x-7, self.hitt6_y-18, 0 ,176, 8, 15, 36, 0)     # 透明人間を描く
            #砂時計とヒットした時の砂時計
            pyxel.blt(self.sunax-7, self.sunay-7,0 ,129, 24, 13, 13,0 ) # 砂時計
            pyxel.blt(self.hitt7_x-7, self.hitt7_y-7,0 ,129, 8, 13, 13,0 ) # 逆さの砂時計
            #pyxel.blt(self.hitt4_x-21, self.hitt4_y-25,1 ,63, 14, 43, 50, ) # 死神
            
            
            # 点数を表示
            pyxel.text(10, 10, f" SCORE:{self.score} 点", 10)     # (始点座標 x, 始点座標 y, 文字（アルファベット限定）, 色)

            #　時間を表示
            pyxel.text(10, 20, f" time:{int(self.time_up-self.time/30)} 秒", 10)     # (始点座標 x, 始点座標 y, 文字（アルファベット限定）, 色)
App()