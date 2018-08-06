import re

s = '''
[180124]TVアニメ『賭ケグルイ』オリジナルサウンドトラック「賭ケグルイノ音 -Notes for “kakegurui”-」[320K+BK(JPG)]/2018年1月新番动漫已发售CD下载索引.url:URL=http://www.tsdm.me/forum.php?mod=viewthread&tid=8
[180124]TVアニメ『賭ケグルイ』オリジナルサウンドトラック「賭ケグルイノ音 -Notes for “kakegurui”-」[320K+BK(JPG)]/2018年1月新番动漫已发售CD下载索引.url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAXA-favicon.ic
[180124]TVアニメ『賭ケグルイ』オリジナルサウンドトラック「賭ケグルイノ音 -Notes for “kakegurui”-」[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:URL=http://www.tsdm.me/forum.php?mod=vi
[180124]TVアニメ『賭ケグルイ』オリジナルサウンドトラック「賭ケグルイノ音 -Notes for “kakegurui”-」[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:IconFile=C:\WINDOWS\system32\SHELL32.dl
[180124]TVアニメ『賭ケグルイ』オリジナルサウンドトラック「賭ケグルイノ音 -Notes for “kakegurui”-」[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvY
[180124]TVアニメ『賭ケグルイ』オリジナルサウンドトラック「賭ケグルイノ音 -Notes for “kakegurui”-」[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:[{000214A0-0000-0000-C000-000000000046}
[180124]TVアニメ『賭ケグルイ』オリジナルサウンドトラック「賭ケグルイノ音 -Notes for “kakegurui”-」[320K+BK(JPG)]/天使动漫自抓[WAV+CUE+LOG+PNG]下载.url:URL=http://www.tsdm.me/forum.php?mod=viewthread&tid=8
[180124]TVアニメ『賭ケグルイ』オリジナルサウンドトラック「賭ケグルイノ音 -Notes for “kakegurui”-」[320K+BK(JPG)]/天使动漫自抓[WAV+CUE+LOG+PNG]下载.url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAXA-favicon.ic
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/2018年1月新番动漫已发售CD下载索引.url:URL=http://www.tsdm.me/forum.php?mod=vie
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/2018年1月新番动漫已发售CD下载索引.url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYA
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:BASEURL=http://bbs.mumayi.
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:URL=http://www.tsdm.me/for
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:Modified=20708FDD7B96CB01D
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:IconFile=C:\WINDOWS\system
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:IconFile=D:+AFyRzYmBdoSLul
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:[{000214A0-0000-0000-C000-
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「Sincerely」[アーティスト盤]／TRUE/tonk 自购[HI-RES]Sincerely[96kHz／24bit][F
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「Sincerely」[アーティスト盤]／TRUE/tonk 自购[HI-RES]Sincerely[96kHz／24bit][F
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「Sincerely」[アーティスト盤]／TRUE/tonk 自购[HI-RES]Sincerely[96kHz／24bit][F
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「Sincerely」[アーティスト盤]／TRUE/tonk 自购[HI-RES]Sincerely[96kHz／24bit][F
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「Sincerely」[アーティスト盤]／TRUE/tonk 自购[HI-RES]Sincerely[96kHz／24bit][F
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「Sincerely」[アーティスト盤]／TRUE/tonk 自购[HI-RES]Sincerely[96kHz／24bit][F
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「Sincerely」[アーティスト盤]／TRUE/tonk 自购[HI-RES]Sincerely[96kHz／24bit][F
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「Sincerely」[アーティスト盤]／TRUE/tonk 自购[HI-RES]Sincerely[96kHz／24bit][F
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「Sincerely」[アーティスト盤]／TRUE/tonk 自购[HI-RES]Sincerely[96kHz／24bit][F
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「Sincerely」[アーティスト盤]／TRUE/tonk 自购[HI-RES]Sincerely[96kHz／24bit][F
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「Sincerely」[アーティスト盤]／TRUE/tonk 自购[HI-RES]Sincerely[96kHz／24bit][F
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「Sincerely」[アーティスト盤]／TRUE/tonk 自购[HI-RES]Sincerely[96kHz／24bit][F
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「Sincerely」[アーティスト盤]／TRUE/tonk 自购[HI-RES]Sincerely[96kHz／24bit][F
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「Sincerely」[アーティスト盤]／TRUE/tonk 自购[HI-RES]Sincerely[96kHz／24bit][F
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「みちしるべ」[アーティスト盤]／茅原実里/tonk 自购[HI-RES]みちしるべ[96kHz／24
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「みちしるべ」[アーティスト盤]／茅原実里/tonk 自购[HI-RES]みちしるべ[96kHz／24
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「みちしるべ」[アーティスト盤]／茅原実里/tonk 自购[HI-RES]みちしるべ[96kHz／24
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「みちしるべ」[アーティスト盤]／茅原実里/tonk 自购[HI-RES]みちしるべ[96kHz／24
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「みちしるべ」[アーティスト盤]／茅原実里/tonk 自购[HI-RES]みちしるべ[96kHz／24
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「みちしるべ」[アーティスト盤]／茅原実里/tonk 自购[HI-RES]みちしるべ[96kHz／24
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「みちしるべ」[アーティスト盤]／茅原実里/tonk 自购[HI-RES]みちしるべ[96kHz／24
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「みちしるべ」[アーティスト盤]／茅原実里/tonk 自购[HI-RES]みちしるべ[96kHz／24
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「みちしるべ」[アーティスト盤]／茅原実里/tonk 自购[HI-RES]みちしるべ[96kHz／24
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「みちしるべ」[アーティスト盤]／茅原実里/tonk 自购[HI-RES]みちしるべ[96kHz／24
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「みちしるべ」[アーティスト盤]／茅原実里/tonk 自购[HI-RES]みちしるべ[96kHz／24
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「みちしるべ」[アーティスト盤]／茅原実里/tonk 自购[HI-RES]みちしるべ[96kHz／24
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「みちしるべ」[アーティスト盤]／茅原実里/tonk 自购[HI-RES]みちしるべ[96kHz／24
[180131]TVアニメ『ヴァイオレット・エヴァーガーデン』OP & ED[アーティスト盤]「Sincerely」／TRUE 「みちしるべ」／茅原実里[320K]/「みちしるべ」[アーティスト盤]／茅原実里/tonk 自购[HI-RES]みちしるべ[96kHz／24
[180425]PS4／PSV『うたわれるもの 散りゆく者への子守唄』主題歌シングル「君だけの旅路 Re：boot」／Suara[320K]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:URL=http://www.tsdm.me/forum.php?mod=viewthr
[180425]PS4／PSV『うたわれるもの 散りゆく者への子守唄』主題歌シングル「君だけの旅路 Re：boot」／Suara[320K]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAXA-f
[180425]PS4／PSV『うたわれるもの 散りゆく者への子守唄』主題歌シングル「君だけの旅路 Re：boot」／Suara[320K]/wsnxx 自购[Hi-Res][96kHz／24bit][ALAC].url:URL=http://www.tsdm.me/forum.php?mod=viewthread&tid=8
[180425]PS4／PSV『うたわれるもの 散りゆく者への子守唄』主題歌シングル「君だけの旅路 Re：boot」／Suara[320K]/wsnxx 自购[Hi-Res][96kHz／24bit][ALAC].url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAXA-favicon.ic
[180425]sumika - Fiction e.p(TVアニメ『ヲタクに恋は難しい』OPテーマ「フィクション」)[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:URL=http://www.tsdm.me/forum.php?mod=viewthread&tid=6
[180425]sumika - Fiction e.p(TVアニメ『ヲタクに恋は難しい』OPテーマ「フィクション」)[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAXA-favicon.ic
[180509]TVアニメ『ウマ娘 プリティーダービー』ED主題歌 ANIMATION DERBY 02 グロウアップ・シャイン![320K+BK(JPG)]/2018年4月新番动漫已发售CD下载索引.url:URL=https://www.tsdm.me/forum.php?mod=viewthread&tid=88
[180509]TVアニメ『ウマ娘 プリティーダービー』ED主題歌 ANIMATION DERBY 02 グロウアップ・シャイン![320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:URL=http://www.tsdm.me/forum.php?mod=view
[180509]TVアニメ『ウマ娘 プリティーダービー』ED主題歌 ANIMATION DERBY 02 グロウアップ・シャイン![320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAX
[180509]TVアニメ『ウマ娘 プリティーダービー』ED主題歌 ANIMATION DERBY 02 グロウアップ・シャイン![320K+BK(JPG)]/天使动漫自抓[WAV+CUE+LOG+BK(PNG)]下载.url:URL=http://www.tsdm.me/forum.php?mod=viewthread&tid
[180509]TVアニメ『ウマ娘 プリティーダービー』ED主題歌 ANIMATION DERBY 02 グロウアップ・シャイン![320K+BK(JPG)]/天使动漫自抓[WAV+CUE+LOG+BK(PNG)]下载.url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAXA-favicon.
[180516]TVアニメ『Caligula -カリギュラ-』EDテーマ「HYPNO」／村川梨衣、小澤亜李、高橋李依、田中美海[320K+BK(JPG)]/2018年4月新番动漫已发售CD下载索引.url:URL=http://www.tsdm.me/forum.php?mod=viewthread&tid=8
[180516]TVアニメ『Caligula -カリギュラ-』EDテーマ「HYPNO」／村川梨衣、小澤亜李、高橋李依、田中美海[320K+BK(JPG)]/2018年4月新番动漫已发售CD下载索引.url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAXA-favicon.ic
[180516]TVアニメ『Caligula -カリギュラ-』EDテーマ「HYPNO」／村川梨衣、小澤亜李、高橋李依、田中美海[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:URL=http://www.tsdm.me/forum.php?mod=vi
[180516]TVアニメ『Caligula -カリギュラ-』EDテーマ「HYPNO」／村川梨衣、小澤亜李、高橋李依、田中美海[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:IconFile=C:\WINDOWS\system32\SHELL32.dl
[180516]TVアニメ『Caligula -カリギュラ-』EDテーマ「HYPNO」／村川梨衣、小澤亜李、高橋李依、田中美海[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvY
[180516]TVアニメ『Caligula -カリギュラ-』EDテーマ「HYPNO」／村川梨衣、小澤亜李、高橋李依、田中美海[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:[{000214A0-0000-0000-C000-000000000046}
[180516]TVアニメ『Caligula -カリギュラ-』EDテーマ「HYPNO」／村川梨衣、小澤亜李、高橋李依、田中美海[320K+BK(JPG)]/天使动漫自抓[WAV+CUE+LOG+BK(PNG)]下载.url:URL=http://www.tsdm.me/forum.php?mod=viewthread&t
[180516]TVアニメ『Caligula -カリギュラ-』EDテーマ「HYPNO」／村川梨衣、小澤亜李、高橋李依、田中美海[320K+BK(JPG)]/天使动漫自抓[WAV+CUE+LOG+BK(PNG)]下载.url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAXA-favico
[180523]TVアニメ『LOST SONG』OP主題歌「歌えばそこに君がいるから」(アニメ盤)／鈴木このみ[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:URL=http://www.tsdm.me/forum.php?mod=viewthread&ti
[180523]TVアニメ『LOST SONG』OP主題歌「歌えばそこに君がいるから」(アニメ盤)／鈴木このみ[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAXA-favicon
[180418]TVアニメ『Caligula -カリギュラ-』ゲーム挿入歌 アニメ Re：アレンジVer.ミニアルバム[320K+BK(JPG)]/10元买CD 支援自购规则（无损音质+BK扫图）新老CD皆可.url:URL=http://www.tsdm.me/forum.php?mod=viewthre
[180418]TVアニメ『Caligula -カリギュラ-』ゲーム挿入歌 アニメ Re：アレンジVer.ミニアルバム[320K+BK(JPG)]/10元买CD 支援自购规则（无损音质+BK扫图）新老CD皆可.url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAXA-fa
[180418]TVアニメ『Caligula -カリギュラ-』ゲーム挿入歌 アニメ Re：アレンジVer.ミニアルバム[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:URL=http://www.tsdm.me/forum.php?mod=viewthread&
[180418]TVアニメ『Caligula -カリギュラ-』ゲーム挿入歌 アニメ Re：アレンジVer.ミニアルバム[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAXA-favic
[180221]TVアニメ『宇宙よりも遠い場所』EDテーマ「ここから、ここから」／水瀬いのり、花澤香菜、井口裕香、早見沙織[320K+BK(JPG)]/2018年1月新番动漫已发售CD下载索引.url:URL=http://www.tsdm.me/forum.php?mod=view
[180221]TVアニメ『宇宙よりも遠い場所』EDテーマ「ここから、ここから」／水瀬いのり、花澤香菜、井口裕香、早見沙織[320K+BK(JPG)]/2018年1月新番动漫已发售CD下载索引.url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAX
[180221]TVアニメ『宇宙よりも遠い場所』EDテーマ「ここから、ここから」／水瀬いのり、花澤香菜、井口裕香、早見沙織[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:BASEURL=http://bbs.mumayi.n
[180221]TVアニメ『宇宙よりも遠い場所』EDテーマ「ここから、ここから」／水瀬いのり、花澤香菜、井口裕香、早見沙織[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:URL=http://www.tsdm.me/foru
[180221]TVアニメ『宇宙よりも遠い場所』EDテーマ「ここから、ここから」／水瀬いのり、花澤香菜、井口裕香、早見沙織[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:IconFile=C:\WINDOWS\system3
[180221]TVアニメ『宇宙よりも遠い場所』EDテーマ「ここから、ここから」／水瀬いのり、花澤香菜、井口裕香、早見沙織[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:IconFile=D:+AFyRzYmBdoSLuld
[180221]TVアニメ『宇宙よりも遠い場所』EDテーマ「ここから、ここから」／水瀬いのり、花澤香菜、井口裕香、早見沙織[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:[{000214A0-0000-0000-C000-0
[180221]TVアニメ『宇宙よりも遠い場所』EDテーマ「ここから、ここから」／水瀬いのり、花澤香菜、井口裕香、早見沙織[320K+BK(JPG)]/天使动漫自抓[WAV+CUE+LOG+PNG]下载.url:URL=http://www.tsdm.me/forum.php?mod=view
[180221]TVアニメ『宇宙よりも遠い場所』EDテーマ「ここから、ここから」／水瀬いのり、花澤香菜、井口裕香、早見沙織[320K+BK(JPG)]/天使动漫自抓[WAV+CUE+LOG+PNG]下载.url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAX
[180221]TVアニメ『恋は雨上がりのように』EDテーマ「Refrain／眩いばかり」[DVD付期間生産限定盤]／Aimer[320K+BK(JPG)]/2018年1月新番动漫已发售CD下载索引.url:URL=http://www.tsdm.me/forum.php?mod=viewthread&tid=
[180221]TVアニメ『恋は雨上がりのように』EDテーマ「Refrain／眩いばかり」[DVD付期間生産限定盤]／Aimer[320K+BK(JPG)]/2018年1月新番动漫已发售CD下载索引.url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAXA-favicon.i
[180221]TVアニメ『恋は雨上がりのように』EDテーマ「Refrain／眩いばかり」[DVD付期間生産限定盤]／Aimer[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:BASEURL=http://bbs.mumayi.net/index.ph
[180221]TVアニメ『恋は雨上がりのように』EDテーマ「Refrain／眩いばかり」[DVD付期間生産限定盤]／Aimer[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:URL=http://www.tsdm.me/forum.php?mod=v
[180221]TVアニメ『恋は雨上がりのように』EDテーマ「Refrain／眩いばかり」[DVD付期間生産限定盤]／Aimer[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:IconFile=C:\WINDOWS\system32\SHELL32.d
[180221]TVアニメ『恋は雨上がりのように』EDテーマ「Refrain／眩いばかり」[DVD付期間生産限定盤]／Aimer[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTv
[180221]TVアニメ『恋は雨上がりのように』EDテーマ「Refrain／眩いばかり」[DVD付期間生産限定盤]／Aimer[320K+BK(JPG)]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:[{000214A0-0000-0000-C000-000000000046
[180221]TVアニメ『恋は雨上がりのように』EDテーマ「Refrain／眩いばかり」[DVD付期間生産限定盤]／Aimer[320K+BK(JPG)]/天使动漫自抓[WAV+CUE+LOG+PNG+DVD]下载.url:URL=http://www.tsdm.me/forum.php?mod=viewthread&
[180221]TVアニメ『恋は雨上がりのように』EDテーマ「Refrain／眩いばかり」[DVD付期間生産限定盤]／Aimer[320K+BK(JPG)]/天使动漫自抓[WAV+CUE+LOG+PNG+DVD]下载.url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAXA-favic
[180307]TVアニメ『DARLING in the FRANXX』OP主題歌「KISS OF DEATH [Produced by HYDE]」／中島美嘉[320K]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:URL=http://www.tsdm.me/forum.php?mod=viewthread&ti
[180307]TVアニメ『DARLING in the FRANXX』OP主題歌「KISS OF DEATH [Produced by HYDE]」／中島美嘉[320K]/2500部动漫,720P,高清蓝光下载,全部有效[天使动漫].url:IconFile=D:+AFyRzYmBdoSLuldbW4mIxWWHTvYAXA-favicon
[180307]TVアニメ『DARLING in the FRANXX』OP主題歌「KISS OF DEATH [Produced by HYDE]」／中島美嘉[320K]/kannagiumine 自抓[WAV+CUE+LOG+PNG+DVD]下载.url:URL=http://www.tsdm.me/forum.php?mod=viewthread&tid=876
'''


ss = s.split('\n')
for sss in ss:
    if sss !='':
        print("rm '/media/ed/TOSHIBA EXT/ACG2018/" + sss.split('l:')[0] + "l'")


# 取出''中間的字
# pattern = re.compile("'(.*)'")
# # ss = s.replace('\\', '')
# ss = pattern.findall(s)
# for sss in ss:
#     str = sss.split("'")[0]
#     print('"' + str + '",')
# '''

# ss = s.replace('modified:', 'git add ')
# print(ss)
# s.replace('{', '')
# s.replace('}', '')
# s.replace('\n', '')
# s.replace('\r', '')
# s.replace('\t', '')
# ss = s.split(',')
# for str in ss:
#     print(str)



# ss = s.split('\r\n')
# for sss in ss:
#     ssss = sss.split('|')
#     for sssss in ssss:
#         print(sssss)

var = '''
      "GET /abnormality/bloodPressure/case/:caseId/log",
      "GET /vitals/provider/:userId/subject/:subjectId/biochemistry",
      "GET /vitals/provider/:userId/subject/:subjectId/bloodGlucose",
      "GET /vitals/provider/:userId/subject/:subjectId/bloodPressure",
      "GET /vitals/provider/:userId/subject/:subjectId/bodyInfo",
      "GET /vitals/provider/:userId/subject/:subjectId/bodyTemperature",
      "GET /vitals/provider/:userId/subject/:subjectId/waist"

'''
