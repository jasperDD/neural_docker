{"filter":false,"title":"generator.py","tooltip":"/app/generator.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":12,"column":22},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":175},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["p"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["r"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["i"]},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["n"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":9},"end":{"row":13,"column":11},"action":"insert","lines":["()"],"id":176}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":12},"action":"insert","lines":["\"\""],"id":177}],[{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["t"],"id":178},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["e"]},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["s"]},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":18,"column":2},"end":{"row":18,"column":25},"action":"remove","lines":["      socket_callback()"],"id":179}],[{"start":{"row":44,"column":37},"end":{"row":45,"column":0},"action":"insert","lines":["",""],"id":180},{"start":{"row":45,"column":0},"end":{"row":45,"column":6},"action":"insert","lines":["      "]},{"start":{"row":45,"column":6},"end":{"row":46,"column":0},"action":"insert","lines":["",""]},{"start":{"row":46,"column":0},"end":{"row":46,"column":6},"action":"insert","lines":["      "]}],[{"start":{"row":46,"column":6},"end":{"row":46,"column":29},"action":"insert","lines":["      socket_callback()"],"id":181}],[{"start":{"row":46,"column":0},"end":{"row":46,"column":12},"action":"remove","lines":["            "],"id":182}],[{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "],"id":183}],[{"start":{"row":46,"column":4},"end":{"row":46,"column":8},"action":"insert","lines":["    "],"id":184}],[{"start":{"row":46,"column":0},"end":{"row":46,"column":8},"action":"remove","lines":["        "],"id":185}],[{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "],"id":186}],[{"start":{"row":46,"column":4},"end":{"row":46,"column":8},"action":"insert","lines":["    "],"id":187}],[{"start":{"row":46,"column":4},"end":{"row":46,"column":8},"action":"remove","lines":["    "],"id":188}],[{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"remove","lines":["    "],"id":189}],[{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "],"id":190}],[{"start":{"row":46,"column":4},"end":{"row":46,"column":8},"action":"insert","lines":["    "],"id":191}],[{"start":{"row":46,"column":4},"end":{"row":46,"column":8},"action":"remove","lines":["    "],"id":192},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"remove","lines":["    "]},{"start":{"row":45,"column":6},"end":{"row":46,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":45,"column":6},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":193},{"start":{"row":46,"column":0},"end":{"row":46,"column":6},"action":"insert","lines":["      "]}],[{"start":{"row":14,"column":41},"end":{"row":14,"column":42},"action":"insert","lines":["'"],"id":194}],[{"start":{"row":14,"column":44},"end":{"row":14,"column":45},"action":"insert","lines":["'"],"id":195}],[{"start":{"row":46,"column":0},"end":{"row":46,"column":23},"action":"remove","lines":["      socket_callback()"],"id":196}],[{"start":{"row":18,"column":2},"end":{"row":18,"column":4},"action":"insert","lines":["  "],"id":197}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":8},"action":"insert","lines":["    "],"id":198}],[{"start":{"row":18,"column":8},"end":{"row":18,"column":31},"action":"insert","lines":["      socket_callback()"],"id":199}],[{"start":{"row":18,"column":8},"end":{"row":18,"column":14},"action":"remove","lines":["      "],"id":200}],[{"start":{"row":14,"column":47},"end":{"row":14,"column":48},"action":"insert","lines":[" "],"id":201}],[{"start":{"row":14,"column":47},"end":{"row":14,"column":48},"action":"remove","lines":[" "],"id":203}],[{"start":{"row":20,"column":12},"end":{"row":20,"column":14},"action":"insert","lines":["# "],"id":204}],[{"start":{"row":19,"column":12},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":205},{"start":{"row":20,"column":0},"end":{"row":20,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":20,"column":12},"end":{"row":20,"column":55},"action":"insert","lines":["socketio.emit('message', {'percent': '10'})"],"id":206}],[{"start":{"row":20,"column":49},"end":{"row":20,"column":53},"action":"remove","lines":["'10'"],"id":207},{"start":{"row":20,"column":49},"end":{"row":20,"column":138},"action":"insert","lines":["int(self.state['bars'].get('t')['index'])/(int(self.state['bars'].get('t')['total'])/100)"]}],[{"start":{"row":12,"column":0},"end":{"row":15,"column":0},"action":"remove","lines":["def socket_callback():","    print(\"test\")","    socketio.emit('message', {'percent': '10'})",""],"id":208}],[{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"remove","lines":["",""],"id":209}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":25},"action":"remove","lines":["        socket_callback()"],"id":210},{"start":{"row":13,"column":34},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":13,"column":34},"end":{"row":13,"column":44},"action":"insert","lines":["int(round("],"id":211}],[{"start":{"row":13,"column":34},"end":{"row":13,"column":38},"action":"remove","lines":["int("],"id":212}],[{"start":{"row":13,"column":34},"end":{"row":13,"column":40},"action":"remove","lines":["round("],"id":213}],[{"start":{"row":15,"column":53},"end":{"row":15,"column":59},"action":"insert","lines":["round("],"id":214}],[{"start":{"row":15,"column":144},"end":{"row":15,"column":145},"action":"insert","lines":[")"],"id":215}],[{"start":{"row":41,"column":6},"end":{"row":42,"column":0},"action":"remove","lines":["",""],"id":216},{"start":{"row":41,"column":6},"end":{"row":42,"column":4},"action":"remove","lines":["","    "]}],[{"start":{"row":41,"column":0},"end":{"row":41,"column":6},"action":"remove","lines":["      "],"id":217}],[{"start":{"row":40,"column":37},"end":{"row":41,"column":0},"action":"remove","lines":["",""],"id":218}],[{"start":{"row":62,"column":29},"end":{"row":62,"column":30},"action":"insert","lines":[" "],"id":219},{"start":{"row":62,"column":30},"end":{"row":62,"column":31},"action":"insert","lines":["#"]}],[{"start":{"row":62,"column":30},"end":{"row":62,"column":31},"action":"insert","lines":["o"],"id":220},{"start":{"row":62,"column":31},"end":{"row":62,"column":32},"action":"insert","lines":["u"]},{"start":{"row":62,"column":32},"end":{"row":62,"column":33},"action":"insert","lines":["t"]},{"start":{"row":62,"column":33},"end":{"row":62,"column":34},"action":"insert","lines":["p"]},{"start":{"row":62,"column":34},"end":{"row":62,"column":35},"action":"insert","lines":["u"]},{"start":{"row":62,"column":35},"end":{"row":62,"column":36},"action":"insert","lines":["t"]},{"start":{"row":62,"column":36},"end":{"row":62,"column":37},"action":"insert","lines":["_"]},{"start":{"row":62,"column":37},"end":{"row":62,"column":38},"action":"insert","lines":["v"]},{"start":{"row":62,"column":38},"end":{"row":62,"column":39},"action":"insert","lines":["i"]},{"start":{"row":62,"column":39},"end":{"row":62,"column":40},"action":"insert","lines":["d"]}],[{"start":{"row":62,"column":40},"end":{"row":62,"column":41},"action":"insert","lines":["e"],"id":221},{"start":{"row":62,"column":41},"end":{"row":62,"column":42},"action":"insert","lines":["o"]},{"start":{"row":62,"column":42},"end":{"row":62,"column":43},"action":"insert","lines":["."]},{"start":{"row":62,"column":43},"end":{"row":62,"column":44},"action":"insert","lines":["m"]}],[{"start":{"row":62,"column":44},"end":{"row":62,"column":45},"action":"insert","lines":["p"],"id":222},{"start":{"row":62,"column":45},"end":{"row":62,"column":46},"action":"insert","lines":["4"]}],[{"start":{"row":62,"column":46},"end":{"row":62,"column":47},"action":"insert","lines":[" "],"id":223}],[{"start":{"row":62,"column":30},"end":{"row":62,"column":46},"action":"remove","lines":["output_video.mp4"],"id":224},{"start":{"row":62,"column":30},"end":{"row":62,"column":48},"action":"insert","lines":["\"output_video.mp4\""]}],[{"start":{"row":41,"column":20},"end":{"row":41,"column":77},"action":"insert","lines":["','.join(my_str[i:i+3] for i in range(0, len(my_str), 3))"],"id":225}],[{"start":{"row":41,"column":77},"end":{"row":41,"column":78},"action":"insert","lines":[" "],"id":226}],[{"start":{"row":41,"column":21},"end":{"row":41,"column":22},"action":"remove","lines":[","],"id":227}],[{"start":{"row":41,"column":21},"end":{"row":41,"column":22},"action":"insert","lines":["\\"],"id":228},{"start":{"row":41,"column":22},"end":{"row":41,"column":23},"action":"insert","lines":["т"]}],[{"start":{"row":41,"column":22},"end":{"row":41,"column":23},"action":"remove","lines":["т"],"id":229}],[{"start":{"row":41,"column":22},"end":{"row":41,"column":23},"action":"insert","lines":["т"],"id":230}],[{"start":{"row":41,"column":22},"end":{"row":41,"column":23},"action":"remove","lines":["т"],"id":231}],[{"start":{"row":41,"column":22},"end":{"row":41,"column":23},"action":"insert","lines":["n"],"id":232}],[{"start":{"row":41,"column":79},"end":{"row":41,"column":86},"action":"remove","lines":["phrase "],"id":233}],[{"start":{"row":41,"column":30},"end":{"row":41,"column":36},"action":"remove","lines":["my_str"],"id":234},{"start":{"row":41,"column":30},"end":{"row":41,"column":37},"action":"insert","lines":["phrase "]}],[{"start":{"row":41,"column":67},"end":{"row":41,"column":73},"action":"remove","lines":["my_str"],"id":235},{"start":{"row":41,"column":67},"end":{"row":41,"column":74},"action":"insert","lines":["phrase "]}],[{"start":{"row":41,"column":42},"end":{"row":41,"column":43},"action":"remove","lines":["3"],"id":236}],[{"start":{"row":41,"column":42},"end":{"row":41,"column":43},"action":"insert","lines":["3"],"id":237},{"start":{"row":41,"column":43},"end":{"row":41,"column":44},"action":"insert","lines":["7"]}],[{"start":{"row":41,"column":78},"end":{"row":41,"column":79},"action":"remove","lines":["3"],"id":238}],[{"start":{"row":41,"column":78},"end":{"row":41,"column":79},"action":"insert","lines":["3"],"id":239},{"start":{"row":41,"column":79},"end":{"row":41,"column":80},"action":"insert","lines":["7"]}],[{"start":{"row":25,"column":35},"end":{"row":25,"column":50},"action":"insert","lines":["font='FreeMono'"],"id":241}],[{"start":{"row":25,"column":28},"end":{"row":25,"column":33},"action":"remove","lines":["Arial"],"id":242},{"start":{"row":25,"column":28},"end":{"row":25,"column":36},"action":"insert","lines":["FreeMono"]}],[{"start":{"row":25,"column":38},"end":{"row":25,"column":53},"action":"remove","lines":["font='FreeMono'"],"id":246}],[{"start":{"row":25,"column":28},"end":{"row":25,"column":36},"action":"remove","lines":["FreeMono"],"id":247},{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"insert","lines":["A"]},{"start":{"row":25,"column":29},"end":{"row":25,"column":30},"action":"insert","lines":["r"]},{"start":{"row":25,"column":30},"end":{"row":25,"column":31},"action":"insert","lines":["i"]},{"start":{"row":25,"column":31},"end":{"row":25,"column":32},"action":"insert","lines":["a"]},{"start":{"row":25,"column":32},"end":{"row":25,"column":33},"action":"insert","lines":["l"]}],[{"start":{"row":25,"column":28},"end":{"row":25,"column":33},"action":"remove","lines":["Arial"],"id":248},{"start":{"row":25,"column":28},"end":{"row":25,"column":34},"action":"insert","lines":["Ubuntu"]}],[{"start":{"row":25,"column":28},"end":{"row":25,"column":34},"action":"remove","lines":["Ubuntu"],"id":249},{"start":{"row":25,"column":28},"end":{"row":25,"column":35},"action":"insert","lines":["Courier"]}],[{"start":{"row":25,"column":28},"end":{"row":25,"column":35},"action":"remove","lines":["Courier"],"id":250},{"start":{"row":25,"column":28},"end":{"row":25,"column":33},"action":"insert","lines":["Arial"]}],[{"start":{"row":41,"column":82},"end":{"row":41,"column":83},"action":"insert","lines":["."],"id":251}],[{"start":{"row":41,"column":82},"end":{"row":41,"column":84},"action":"remove","lines":[". "],"id":252},{"start":{"row":41,"column":82},"end":{"row":41,"column":98},"action":"insert","lines":[".encode('utf-8')"]}],[{"start":{"row":41,"column":83},"end":{"row":41,"column":98},"action":"remove","lines":["encode('utf-8')"],"id":253},{"start":{"row":41,"column":82},"end":{"row":41,"column":83},"action":"remove","lines":["."]}],[{"start":{"row":83,"column":8},"end":{"row":83,"column":10},"action":"insert","lines":["# "],"id":254}],[{"start":{"row":84,"column":12},"end":{"row":84,"column":14},"action":"insert","lines":["# "],"id":255}],[{"start":{"row":86,"column":8},"end":{"row":86,"column":10},"action":"insert","lines":["# "],"id":256}],[{"start":{"row":87,"column":8},"end":{"row":87,"column":10},"action":"insert","lines":["# "],"id":257}],[{"start":{"row":88,"column":0},"end":{"row":88,"column":4},"action":"insert","lines":["    "],"id":258}],[{"start":{"row":88,"column":4},"end":{"row":88,"column":8},"action":"insert","lines":["    "],"id":259}],[{"start":{"row":88,"column":8},"end":{"row":89,"column":0},"action":"insert","lines":["",""],"id":260},{"start":{"row":89,"column":0},"end":{"row":89,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":88,"column":8},"end":{"row":88,"column":16},"action":"insert","lines":["self.cvc"],"id":261}],[{"start":{"row":88,"column":16},"end":{"row":88,"column":17},"action":"insert","lines":["ю"],"id":262},{"start":{"row":88,"column":17},"end":{"row":88,"column":18},"action":"insert","lines":["в"]},{"start":{"row":88,"column":18},"end":{"row":88,"column":19},"action":"insert","lines":["г"]},{"start":{"row":88,"column":19},"end":{"row":88,"column":20},"action":"insert","lines":["к"]},{"start":{"row":88,"column":20},"end":{"row":88,"column":21},"action":"insert","lines":["ф"]},{"start":{"row":88,"column":21},"end":{"row":88,"column":22},"action":"insert","lines":["е"]},{"start":{"row":88,"column":22},"end":{"row":88,"column":23},"action":"insert","lines":["ш"]},{"start":{"row":88,"column":23},"end":{"row":88,"column":24},"action":"insert","lines":["щ"]},{"start":{"row":88,"column":24},"end":{"row":88,"column":25},"action":"insert","lines":["т"]}],[{"start":{"row":88,"column":25},"end":{"row":88,"column":26},"action":"insert","lines":[" "],"id":263},{"start":{"row":88,"column":26},"end":{"row":88,"column":27},"action":"insert","lines":["="]},{"start":{"row":88,"column":27},"end":{"row":88,"column":28},"action":"insert","lines":["2"]}],[{"start":{"row":88,"column":27},"end":{"row":88,"column":28},"action":"remove","lines":["2"],"id":264}],[{"start":{"row":88,"column":25},"end":{"row":88,"column":27},"action":"remove","lines":[" ="],"id":265}],[{"start":{"row":88,"column":13},"end":{"row":88,"column":25},"action":"remove","lines":["cvcювгкфешщт"],"id":266}],[{"start":{"row":88,"column":13},"end":{"row":88,"column":14},"action":"insert","lines":["с"],"id":267}],[{"start":{"row":88,"column":13},"end":{"row":88,"column":14},"action":"remove","lines":["с"],"id":268}],[{"start":{"row":88,"column":13},"end":{"row":88,"column":14},"action":"insert","lines":["c"],"id":269},{"start":{"row":88,"column":14},"end":{"row":88,"column":15},"action":"insert","lines":["v"]}],[{"start":{"row":88,"column":14},"end":{"row":88,"column":15},"action":"remove","lines":["v"],"id":270},{"start":{"row":88,"column":13},"end":{"row":88,"column":14},"action":"remove","lines":["c"]}],[{"start":{"row":88,"column":13},"end":{"row":88,"column":14},"action":"insert","lines":["c"],"id":271},{"start":{"row":88,"column":14},"end":{"row":88,"column":15},"action":"insert","lines":["v"]},{"start":{"row":88,"column":15},"end":{"row":88,"column":16},"action":"insert","lines":["c"]},{"start":{"row":88,"column":16},"end":{"row":88,"column":17},"action":"insert","lines":["."]},{"start":{"row":88,"column":17},"end":{"row":88,"column":18},"action":"insert","lines":["d"]},{"start":{"row":88,"column":18},"end":{"row":88,"column":19},"action":"insert","lines":["u"]},{"start":{"row":88,"column":19},"end":{"row":88,"column":20},"action":"insert","lines":["r"]},{"start":{"row":88,"column":20},"end":{"row":88,"column":21},"action":"insert","lines":["a"]}],[{"start":{"row":88,"column":21},"end":{"row":88,"column":22},"action":"insert","lines":["t"],"id":272},{"start":{"row":88,"column":22},"end":{"row":88,"column":23},"action":"insert","lines":["i"]},{"start":{"row":88,"column":23},"end":{"row":88,"column":24},"action":"insert","lines":["o"]},{"start":{"row":88,"column":24},"end":{"row":88,"column":25},"action":"insert","lines":["n"]}],[{"start":{"row":88,"column":25},"end":{"row":88,"column":26},"action":"insert","lines":[" "],"id":273},{"start":{"row":88,"column":26},"end":{"row":88,"column":27},"action":"insert","lines":["="]}],[{"start":{"row":88,"column":27},"end":{"row":88,"column":28},"action":"insert","lines":[" "],"id":274},{"start":{"row":88,"column":28},"end":{"row":88,"column":29},"action":"insert","lines":["2"]}],[{"start":{"row":88,"column":29},"end":{"row":89,"column":0},"action":"insert","lines":["",""],"id":275},{"start":{"row":89,"column":0},"end":{"row":89,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":89,"column":8},"end":{"row":89,"column":16},"action":"insert","lines":["self.cvc"],"id":276}],[{"start":{"row":89,"column":16},"end":{"row":90,"column":8},"action":"insert","lines":[".write_videofile(self.output_path+self.output_text_filename, fps=self.output_fps, codec=self.output_codec, bitrate=self.video_bitrate, logger=None)","        "],"id":277}],[{"start":{"row":90,"column":8},"end":{"row":91,"column":8},"action":"remove","lines":["","        "],"id":278}],[{"start":{"row":88,"column":28},"end":{"row":88,"column":29},"action":"remove","lines":["2"],"id":279}],[{"start":{"row":88,"column":28},"end":{"row":88,"column":29},"action":"insert","lines":["4"],"id":280}]]},"ace":{"folds":[],"scrolltop":780,"scrollleft":0,"selection":{"start":{"row":77,"column":6},"end":{"row":77,"column":6},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":54,"state":"start","mode":"ace/mode/python"}},"timestamp":1583443695697,"hash":"94f2efce1a472a48be52adcc59541d99e2455580"}