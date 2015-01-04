>>> from graphillion import GraphSet           #Graphillionのインポート
>>> import graphillion.tutorial as tl          #チュートリアルのためのヘルパーメソッド
>>> universeList = tl.grid(8,8)                #ユニバースとなる格子グラフのリストを作成
>>> GraphSet.set_universe(universeList)
>>> start = 1                                  #求めるパスの始点
>>> goal = 81                                  #求めるパスの終点
>>> pathsGraphSet = GraphSet.paths(start,goal) #指定した始点と終点を結ぶ全てのパスを求める
>>> len(pathsGraphSet)                         #パスの数を返す
3266598486981642
>>> for path in pathsGraphSet:                 #パスの列挙
...     path
...     break                                  #breakがないとひたすら列挙し続ける
... 
[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), …
>>> pathsGraphSet.choice()                     #パス集合から1つのパスを抽出
[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), …








