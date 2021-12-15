{"filter":false,"title":"app.py","tooltip":"/flaskapp/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":41,"column":23},"end":{"row":41,"column":25},"action":"remove","lines":["BU"],"id":547},{"start":{"row":41,"column":23},"end":{"row":41,"column":29},"action":"insert","lines":["BUCKET"]}],[{"start":{"row":42,"column":27},"end":{"row":42,"column":62},"action":"remove","lines":["'tiles/10/S/DG/2015/12/7/0/B01.jp2'"],"id":548},{"start":{"row":42,"column":27},"end":{"row":42,"column":28},"action":"insert","lines":["f"]},{"start":{"row":42,"column":28},"end":{"row":42,"column":29},"action":"insert","lines":["i"]},{"start":{"row":42,"column":29},"end":{"row":42,"column":30},"action":"insert","lines":["l"]},{"start":{"row":42,"column":30},"end":{"row":42,"column":31},"action":"insert","lines":["e"]},{"start":{"row":42,"column":31},"end":{"row":42,"column":32},"action":"insert","lines":["n"]},{"start":{"row":42,"column":32},"end":{"row":42,"column":33},"action":"insert","lines":["a"]},{"start":{"row":42,"column":33},"end":{"row":42,"column":34},"action":"insert","lines":["m"]},{"start":{"row":42,"column":34},"end":{"row":42,"column":35},"action":"insert","lines":["e"]}],[{"start":{"row":48,"column":4},"end":{"row":48,"column":8},"action":"remove","lines":["    "],"id":549}],[{"start":{"row":48,"column":11},"end":{"row":48,"column":17},"action":"remove","lines":["output"],"id":550},{"start":{"row":48,"column":11},"end":{"row":48,"column":12},"action":"insert","lines":["i"]},{"start":{"row":48,"column":12},"end":{"row":48,"column":13},"action":"insert","lines":["m"]},{"start":{"row":48,"column":13},"end":{"row":48,"column":14},"action":"insert","lines":["g"]}],[{"start":{"row":51,"column":0},"end":{"row":51,"column":11},"action":"remove","lines":["    return "],"id":551},{"start":{"row":50,"column":4},"end":{"row":51,"column":0},"action":"remove","lines":["",""]},{"start":{"row":50,"column":0},"end":{"row":50,"column":4},"action":"remove","lines":["    "]},{"start":{"row":49,"column":4},"end":{"row":50,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":38,"column":2},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":552},{"start":{"row":39,"column":0},"end":{"row":39,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":39,"column":0},"end":{"row":39,"column":39},"action":"insert","lines":["@app.route(\"/upload\", methods=['POST'])"],"id":553}],[{"start":{"row":39,"column":13},"end":{"row":39,"column":19},"action":"remove","lines":["upload"],"id":554},{"start":{"row":39,"column":13},"end":{"row":39,"column":14},"action":"insert","lines":["t"]},{"start":{"row":39,"column":14},"end":{"row":39,"column":15},"action":"insert","lines":["e"]},{"start":{"row":39,"column":15},"end":{"row":39,"column":16},"action":"insert","lines":["m"]},{"start":{"row":39,"column":16},"end":{"row":39,"column":17},"action":"insert","lines":["p"]}],[{"start":{"row":39,"column":18},"end":{"row":39,"column":36},"action":"remove","lines":[", methods=['POST']"],"id":555}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":9},"action":"remove","lines":["import io"],"id":556},{"start":{"row":11,"column":43},"end":{"row":12,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":7,"column":0},"end":{"row":9,"column":18},"action":"remove","lines":["import matplotlib.pyplot as plt","import matplotlib.image as mpimg","import numpy as np"],"id":557},{"start":{"row":6,"column":14},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":37,"column":4},"end":{"row":43,"column":35},"action":"remove","lines":["s3 = boto3.resource('s3')","    bucket = s3.Bucket(BUCKET)","    object = bucket.Object(filename)","    ","    file_stream = io.StringIO()","    object.download_fileobj(file_stream)","    img = mpimg.imread(file_stream)"],"id":558}],[{"start":{"row":36,"column":9},"end":{"row":36,"column":17},"action":"remove","lines":["filename"],"id":559}],[{"start":{"row":35,"column":17},"end":{"row":35,"column":18},"action":"insert","lines":["/"],"id":560},{"start":{"row":35,"column":18},"end":{"row":35,"column":19},"action":"insert","lines":["<"]},{"start":{"row":35,"column":19},"end":{"row":35,"column":20},"action":"insert","lines":["f"]},{"start":{"row":35,"column":20},"end":{"row":35,"column":21},"action":"insert","lines":["i"]},{"start":{"row":35,"column":21},"end":{"row":35,"column":22},"action":"insert","lines":["l"]},{"start":{"row":35,"column":22},"end":{"row":35,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":35,"column":23},"end":{"row":35,"column":24},"action":"insert","lines":["n"],"id":561},{"start":{"row":35,"column":24},"end":{"row":35,"column":25},"action":"insert","lines":["a"]},{"start":{"row":35,"column":25},"end":{"row":35,"column":26},"action":"insert","lines":["m"]},{"start":{"row":35,"column":26},"end":{"row":35,"column":27},"action":"insert","lines":["e"]},{"start":{"row":35,"column":27},"end":{"row":35,"column":28},"action":"insert","lines":[">"]}],[{"start":{"row":36,"column":11},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":562},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"insert","lines":[" "],"id":563},{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"insert","lines":["g"]},{"start":{"row":4,"column":28},"end":{"row":4,"column":29},"action":"insert","lines":["e"]},{"start":{"row":4,"column":29},"end":{"row":4,"column":30},"action":"insert","lines":["t"]},{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"insert","lines":["]"]}],[{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"remove","lines":["]"],"id":564}],[{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"insert","lines":["_"],"id":565}],[{"start":{"row":4,"column":27},"end":{"row":4,"column":31},"action":"remove","lines":["get_"],"id":566},{"start":{"row":4,"column":27},"end":{"row":4,"column":38},"action":"insert","lines":["get_image()"]}],[{"start":{"row":4,"column":37},"end":{"row":4,"column":38},"action":"insert","lines":[","],"id":567}],[{"start":{"row":4,"column":37},"end":{"row":4,"column":38},"action":"remove","lines":[","],"id":568},{"start":{"row":4,"column":36},"end":{"row":4,"column":38},"action":"remove","lines":["()"]}],[{"start":{"row":4,"column":36},"end":{"row":4,"column":37},"action":"insert","lines":["."],"id":569}],[{"start":{"row":4,"column":36},"end":{"row":4,"column":37},"action":"remove","lines":["."],"id":570}],[{"start":{"row":4,"column":36},"end":{"row":4,"column":37},"action":"insert","lines":[","],"id":571}],[{"start":{"row":36,"column":11},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":572},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":37,"column":4},"end":{"row":37,"column":5},"action":"insert","lines":["g"],"id":573},{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"insert","lines":["e"]},{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"insert","lines":["t"]}],[{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"insert","lines":[" "],"id":574}],[{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"insert","lines":["i"],"id":575},{"start":{"row":37,"column":9},"end":{"row":37,"column":10},"action":"insert","lines":["m"]},{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"insert","lines":["a"]}],[{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"remove","lines":["a"],"id":576},{"start":{"row":37,"column":9},"end":{"row":37,"column":10},"action":"remove","lines":["m"]},{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"remove","lines":["i"]},{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"remove","lines":[" "]}],[{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"remove","lines":["t"],"id":577},{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"remove","lines":["e"]},{"start":{"row":37,"column":4},"end":{"row":37,"column":5},"action":"remove","lines":["g"]}],[{"start":{"row":37,"column":4},"end":{"row":37,"column":5},"action":"insert","lines":["i"],"id":578},{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"insert","lines":["m"]},{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"insert","lines":["e"]}],[{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"insert","lines":[" "],"id":579},{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"insert","lines":["="]}],[{"start":{"row":37,"column":9},"end":{"row":37,"column":10},"action":"insert","lines":[" "],"id":580}],[{"start":{"row":37,"column":9},"end":{"row":37,"column":10},"action":"remove","lines":[" "],"id":581},{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"remove","lines":["="]},{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"remove","lines":[" "]},{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"remove","lines":["e"]}],[{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"insert","lines":["h"],"id":582}],[{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"insert","lines":[" "],"id":583},{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"insert","lines":["="]}],[{"start":{"row":37,"column":9},"end":{"row":37,"column":10},"action":"insert","lines":[" "],"id":584}],[{"start":{"row":37,"column":9},"end":{"row":37,"column":10},"action":"remove","lines":[" "],"id":585},{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"remove","lines":["="]},{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"remove","lines":[" "]},{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"remove","lines":["h"]}],[{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"insert","lines":["g"],"id":586},{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"insert","lines":["="]}],[{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"insert","lines":[" "],"id":587}],[{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"remove","lines":[" "],"id":588},{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"remove","lines":["="]}],[{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"insert","lines":[" "],"id":589},{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"insert","lines":["="]}],[{"start":{"row":37,"column":9},"end":{"row":37,"column":10},"action":"insert","lines":[" "],"id":590},{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"insert","lines":["i"]}],[{"start":{"row":37,"column":11},"end":{"row":37,"column":12},"action":"insert","lines":["m"],"id":591},{"start":{"row":37,"column":12},"end":{"row":37,"column":13},"action":"insert","lines":["a"]}],[{"start":{"row":37,"column":12},"end":{"row":37,"column":13},"action":"remove","lines":["a"],"id":592},{"start":{"row":37,"column":11},"end":{"row":37,"column":12},"action":"remove","lines":["m"]},{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"remove","lines":["i"]}],[{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"insert","lines":["f"],"id":593},{"start":{"row":37,"column":11},"end":{"row":37,"column":12},"action":"insert","lines":["e"]}],[{"start":{"row":37,"column":11},"end":{"row":37,"column":12},"action":"remove","lines":["e"],"id":594},{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"remove","lines":["f"]}],[{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"insert","lines":["g"],"id":595}],[{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"remove","lines":["g"],"id":596},{"start":{"row":37,"column":10},"end":{"row":37,"column":21},"action":"insert","lines":["get_image()"]}],[{"start":{"row":37,"column":20},"end":{"row":37,"column":21},"action":"insert","lines":["b"],"id":597},{"start":{"row":37,"column":21},"end":{"row":37,"column":22},"action":"insert","lines":["u"]},{"start":{"row":37,"column":22},"end":{"row":37,"column":23},"action":"insert","lines":["c"]},{"start":{"row":37,"column":23},"end":{"row":37,"column":24},"action":"insert","lines":["k"]}],[{"start":{"row":37,"column":23},"end":{"row":37,"column":24},"action":"remove","lines":["k"],"id":598},{"start":{"row":37,"column":22},"end":{"row":37,"column":23},"action":"remove","lines":["c"]},{"start":{"row":37,"column":21},"end":{"row":37,"column":22},"action":"remove","lines":["u"]},{"start":{"row":37,"column":20},"end":{"row":37,"column":21},"action":"remove","lines":["b"]}],[{"start":{"row":37,"column":20},"end":{"row":37,"column":21},"action":"insert","lines":["B"],"id":599},{"start":{"row":37,"column":21},"end":{"row":37,"column":22},"action":"insert","lines":["U"]},{"start":{"row":37,"column":22},"end":{"row":37,"column":23},"action":"insert","lines":["C"]},{"start":{"row":37,"column":23},"end":{"row":37,"column":24},"action":"insert","lines":["K"]},{"start":{"row":37,"column":24},"end":{"row":37,"column":25},"action":"insert","lines":["E"]},{"start":{"row":37,"column":25},"end":{"row":37,"column":26},"action":"insert","lines":["T"]}],[{"start":{"row":37,"column":26},"end":{"row":37,"column":27},"action":"insert","lines":[","],"id":600}],[{"start":{"row":37,"column":27},"end":{"row":37,"column":28},"action":"insert","lines":[" "],"id":601},{"start":{"row":37,"column":28},"end":{"row":37,"column":29},"action":"insert","lines":["f"]},{"start":{"row":37,"column":29},"end":{"row":37,"column":30},"action":"insert","lines":["i"]},{"start":{"row":37,"column":30},"end":{"row":37,"column":31},"action":"insert","lines":["l"]},{"start":{"row":37,"column":31},"end":{"row":37,"column":32},"action":"insert","lines":["e"]},{"start":{"row":37,"column":32},"end":{"row":37,"column":33},"action":"insert","lines":["n"]},{"start":{"row":37,"column":33},"end":{"row":37,"column":34},"action":"insert","lines":["a"]}],[{"start":{"row":37,"column":34},"end":{"row":37,"column":35},"action":"insert","lines":["m"],"id":602},{"start":{"row":37,"column":35},"end":{"row":37,"column":36},"action":"insert","lines":["e"]}],[{"start":{"row":37,"column":36},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":603},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"remove","lines":["    "],"id":604},{"start":{"row":37,"column":36},"end":{"row":38,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":36,"column":9},"end":{"row":36,"column":10},"action":"insert","lines":["f"],"id":605},{"start":{"row":36,"column":10},"end":{"row":36,"column":11},"action":"insert","lines":["i"]},{"start":{"row":36,"column":11},"end":{"row":36,"column":12},"action":"insert","lines":["l"]},{"start":{"row":36,"column":12},"end":{"row":36,"column":13},"action":"insert","lines":["e"]},{"start":{"row":36,"column":13},"end":{"row":36,"column":14},"action":"insert","lines":["n"]},{"start":{"row":36,"column":14},"end":{"row":36,"column":15},"action":"insert","lines":["a"]},{"start":{"row":36,"column":15},"end":{"row":36,"column":16},"action":"insert","lines":["m"]},{"start":{"row":36,"column":16},"end":{"row":36,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"remove","lines":["    "],"id":606},{"start":{"row":38,"column":4},"end":{"row":39,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":14},"action":"remove","lines":["return img"],"id":607},{"start":{"row":40,"column":4},"end":{"row":40,"column":61},"action":"insert","lines":["return render_template('storage.html', contents=contents)"]}],[{"start":{"row":40,"column":28},"end":{"row":40,"column":35},"action":"remove","lines":["storage"],"id":608},{"start":{"row":40,"column":28},"end":{"row":40,"column":29},"action":"insert","lines":["t"]},{"start":{"row":40,"column":29},"end":{"row":40,"column":30},"action":"insert","lines":["m"]}],[{"start":{"row":40,"column":29},"end":{"row":40,"column":30},"action":"remove","lines":["m"],"id":609}],[{"start":{"row":40,"column":29},"end":{"row":40,"column":30},"action":"insert","lines":["e"],"id":610},{"start":{"row":40,"column":30},"end":{"row":40,"column":31},"action":"insert","lines":["m"]},{"start":{"row":40,"column":31},"end":{"row":40,"column":32},"action":"insert","lines":["p"]}],[{"start":{"row":40,"column":11},"end":{"row":40,"column":58},"action":"remove","lines":["render_template('temp.html', contents=contents)"],"id":611}],[{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"remove","lines":[" "],"id":612},{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"remove","lines":[" "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"remove","lines":["    "]},{"start":{"row":38,"column":4},"end":{"row":39,"column":2},"action":"remove","lines":["","  "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"remove","lines":["    "]},{"start":{"row":37,"column":37},"end":{"row":38,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":37,"column":37},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":613},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"remove","lines":["    "],"id":614},{"start":{"row":37,"column":37},"end":{"row":38,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":37,"column":37},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":615},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":38,"column":4},"end":{"row":39,"column":10},"action":"insert","lines":["imgplot = plt.imshow(img)","plt.show()"],"id":616}],[{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "],"id":617}],[{"start":{"row":6,"column":0},"end":{"row":8,"column":43},"action":"remove","lines":["import logging","import boto3","from botocore.exceptions import ClientError"],"id":618},{"start":{"row":6,"column":0},"end":{"row":12,"column":9},"action":"insert","lines":["import logging","import boto3","from botocore.exceptions import ClientError","import matplotlib.pyplot as plt","import matplotlib.image as mpimg","import numpy as np","import io"]}],[{"start":{"row":43,"column":4},"end":{"row":43,"column":14},"action":"remove","lines":["plt.show()"],"id":619}],[{"start":{"row":44,"column":11},"end":{"row":44,"column":21},"action":"insert","lines":["plt.show()"],"id":620}],[{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"remove","lines":["    "],"id":621},{"start":{"row":42,"column":29},"end":{"row":43,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":43,"column":11},"end":{"row":43,"column":21},"action":"remove","lines":["plt.show()"],"id":623}],[{"start":{"row":42,"column":29},"end":{"row":43,"column":0},"action":"insert","lines":["",""],"id":624},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":43,"column":4},"end":{"row":43,"column":14},"action":"insert","lines":["plt.show()"],"id":625}],[{"start":{"row":45,"column":0},"end":{"row":47,"column":0},"action":"remove","lines":["    ","    ",""],"id":626}],[{"start":{"row":41,"column":37},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":627},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "]},{"start":{"row":42,"column":4},"end":{"row":42,"column":5},"action":"insert","lines":["p"]},{"start":{"row":42,"column":5},"end":{"row":42,"column":6},"action":"insert","lines":["r"]},{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"insert","lines":["u"]}],[{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"remove","lines":["u"],"id":628}],[{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"insert","lines":["i"],"id":629},{"start":{"row":42,"column":7},"end":{"row":42,"column":8},"action":"insert","lines":["n"]},{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":42,"column":9},"end":{"row":42,"column":11},"action":"insert","lines":["()"],"id":630}],[{"start":{"row":42,"column":10},"end":{"row":42,"column":11},"action":"insert","lines":["i"],"id":631},{"start":{"row":42,"column":11},"end":{"row":42,"column":12},"action":"insert","lines":["m"]},{"start":{"row":42,"column":12},"end":{"row":42,"column":13},"action":"insert","lines":["g"]}],[{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"insert","lines":[" "],"id":632}],[{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"remove","lines":[" "],"id":633}],[{"start":{"row":43,"column":29},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":634},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":44,"column":4},"end":{"row":44,"column":14},"action":"insert","lines":["print(img)"],"id":635}],[{"start":{"row":44,"column":10},"end":{"row":44,"column":13},"action":"remove","lines":["img"],"id":636},{"start":{"row":44,"column":10},"end":{"row":44,"column":17},"action":"insert","lines":["imgplot"]}],[{"start":{"row":42,"column":0},"end":{"row":46,"column":11},"action":"remove","lines":["    print(img)","    imgplot = plt.imshow(img)","    print(imgplot)","    plt.show()","    return "],"id":644}],[{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"insert","lines":["    "],"id":645}],[{"start":{"row":43,"column":4},"end":{"row":43,"column":5},"action":"insert","lines":["r"],"id":646},{"start":{"row":43,"column":5},"end":{"row":43,"column":6},"action":"insert","lines":["e"]},{"start":{"row":43,"column":6},"end":{"row":43,"column":7},"action":"insert","lines":["t"]},{"start":{"row":43,"column":7},"end":{"row":43,"column":8},"action":"insert","lines":["u"]},{"start":{"row":43,"column":8},"end":{"row":43,"column":9},"action":"insert","lines":["r"]},{"start":{"row":43,"column":9},"end":{"row":43,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":43,"column":10},"end":{"row":43,"column":11},"action":"insert","lines":[" "],"id":647},{"start":{"row":43,"column":11},"end":{"row":43,"column":12},"action":"insert","lines":["i"]},{"start":{"row":43,"column":12},"end":{"row":43,"column":13},"action":"insert","lines":["m"]},{"start":{"row":43,"column":13},"end":{"row":43,"column":14},"action":"insert","lines":["g"]}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":7},"action":"remove","lines":["img"],"id":648},{"start":{"row":41,"column":4},"end":{"row":41,"column":12},"action":"insert","lines":["response"]}],[{"start":{"row":43,"column":11},"end":{"row":43,"column":14},"action":"remove","lines":["img"],"id":649},{"start":{"row":43,"column":11},"end":{"row":43,"column":19},"action":"insert","lines":["response"]}],[{"start":{"row":43,"column":3},"end":{"row":43,"column":19},"action":"remove","lines":[" return response"],"id":650},{"start":{"row":43,"column":3},"end":{"row":43,"column":60},"action":"insert","lines":["return render_template('storage.html', contents=contents)"]}],[{"start":{"row":43,"column":27},"end":{"row":43,"column":34},"action":"remove","lines":["storage"],"id":651},{"start":{"row":43,"column":27},"end":{"row":43,"column":28},"action":"insert","lines":["t"]},{"start":{"row":43,"column":28},"end":{"row":43,"column":29},"action":"insert","lines":["e"]},{"start":{"row":43,"column":29},"end":{"row":43,"column":30},"action":"insert","lines":["m"]},{"start":{"row":43,"column":30},"end":{"row":43,"column":31},"action":"insert","lines":["p"]}],[{"start":{"row":43,"column":3},"end":{"row":43,"column":4},"action":"insert","lines":[" "],"id":652}],[{"start":{"row":43,"column":40},"end":{"row":43,"column":48},"action":"remove","lines":["contents"],"id":653},{"start":{"row":43,"column":40},"end":{"row":43,"column":41},"action":"insert","lines":["r"]},{"start":{"row":43,"column":41},"end":{"row":43,"column":42},"action":"insert","lines":["e"]},{"start":{"row":43,"column":42},"end":{"row":43,"column":43},"action":"insert","lines":["s"]},{"start":{"row":43,"column":43},"end":{"row":43,"column":44},"action":"insert","lines":["p"]},{"start":{"row":43,"column":44},"end":{"row":43,"column":45},"action":"insert","lines":["o"]},{"start":{"row":43,"column":45},"end":{"row":43,"column":46},"action":"insert","lines":["n"]},{"start":{"row":43,"column":46},"end":{"row":43,"column":47},"action":"insert","lines":["e"]}],[{"start":{"row":43,"column":55},"end":{"row":43,"column":56},"action":"remove","lines":["s"],"id":654},{"start":{"row":43,"column":54},"end":{"row":43,"column":55},"action":"remove","lines":["t"]},{"start":{"row":43,"column":53},"end":{"row":43,"column":54},"action":"remove","lines":["n"]},{"start":{"row":43,"column":52},"end":{"row":43,"column":53},"action":"remove","lines":["e"]},{"start":{"row":43,"column":51},"end":{"row":43,"column":52},"action":"remove","lines":["t"]},{"start":{"row":43,"column":50},"end":{"row":43,"column":51},"action":"remove","lines":["n"]},{"start":{"row":43,"column":49},"end":{"row":43,"column":50},"action":"remove","lines":["o"]},{"start":{"row":43,"column":48},"end":{"row":43,"column":49},"action":"remove","lines":["c"]}],[{"start":{"row":43,"column":48},"end":{"row":43,"column":49},"action":"insert","lines":["r"],"id":655},{"start":{"row":43,"column":49},"end":{"row":43,"column":50},"action":"insert","lines":["e"]},{"start":{"row":43,"column":50},"end":{"row":43,"column":51},"action":"insert","lines":["s"]},{"start":{"row":43,"column":51},"end":{"row":43,"column":52},"action":"insert","lines":["p"]},{"start":{"row":43,"column":52},"end":{"row":43,"column":53},"action":"insert","lines":["o"]},{"start":{"row":43,"column":53},"end":{"row":43,"column":54},"action":"insert","lines":["n"]},{"start":{"row":43,"column":54},"end":{"row":43,"column":55},"action":"insert","lines":["s"]},{"start":{"row":43,"column":55},"end":{"row":43,"column":56},"action":"insert","lines":["e"]}]]},"ace":{"folds":[],"scrolltop":442,"scrollleft":0,"selection":{"start":{"row":43,"column":57},"end":{"row":43,"column":57},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":30,"state":"start","mode":"ace/mode/python"}},"timestamp":1639583073432,"hash":"7b82b55352d349a0ffde369f6cd02ec7c7f76c53"}