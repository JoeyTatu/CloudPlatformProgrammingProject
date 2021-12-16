{"filter":false,"title":"app.py","tooltip":"/flaskapp/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":28,"column":4},"end":{"row":28,"column":8},"action":"remove","lines":["    "],"id":1242}],[{"start":{"row":28,"column":19},"end":{"row":28,"column":26},"action":"remove","lines":["s Index"],"id":1243},{"start":{"row":28,"column":19},"end":{"row":28,"column":20},"action":"insert","lines":["/"]}],[{"start":{"row":28,"column":20},"end":{"row":28,"column":21},"action":"insert","lines":["P"],"id":1244},{"start":{"row":28,"column":21},"end":{"row":28,"column":22},"action":"insert","lines":["R"]},{"start":{"row":28,"column":22},"end":{"row":28,"column":23},"action":"insert","lines":["o"]},{"start":{"row":28,"column":23},"end":{"row":28,"column":24},"action":"insert","lines":["f"]},{"start":{"row":28,"column":24},"end":{"row":28,"column":25},"action":"insert","lines":["i"]},{"start":{"row":28,"column":25},"end":{"row":28,"column":26},"action":"insert","lines":["l"]},{"start":{"row":28,"column":26},"end":{"row":28,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":28,"column":21},"end":{"row":28,"column":22},"action":"remove","lines":["R"],"id":1245}],[{"start":{"row":28,"column":21},"end":{"row":28,"column":22},"action":"insert","lines":["r"],"id":1246}],[{"start":{"row":14,"column":21},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":1247},{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":16,"column":0},"end":{"row":38,"column":14},"action":"insert","lines":["from flask import Flask","from flask_sqlalchemy import SQLAlchemy","","# init SQLAlchemy so we can use it later in our models","db = SQLAlchemy()","","def create_app():","    app = Flask(__name__)","","    app.config['SECRET_KEY'] = 'secret-key-goes-here'","    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'","","    db.init_app(app)","","    # blueprint for auth routes in our app","    from .auth import auth as auth_blueprint","    app.register_blueprint(auth_blueprint)","","    # blueprint for non-auth parts of app","    from .main import main as main_blueprint","    app.register_blueprint(main_blueprint)","","    return app"],"id":1248}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":39},"action":"remove","lines":["from flask import Flask","from flask_sqlalchemy import SQLAlchemy"],"id":1249}],[{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"remove","lines":["",""],"id":1250},{"start":{"row":14,"column":21},"end":{"row":15,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":9},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":1251}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":39},"action":"insert","lines":["from flask import Flask","from flask_sqlalchemy import SQLAlchemy"],"id":1252}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":23},"action":"remove","lines":["from flask import Flask"],"id":1253},{"start":{"row":12,"column":9},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":39},"action":"remove","lines":["from flask_sqlalchemy import SQLAlchemy"],"id":1254}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":39},"action":"insert","lines":["from flask_sqlalchemy import SQLAlchemy"],"id":1255}],[{"start":{"row":3,"column":39},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":1256}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":25},"action":"remove","lines":["    app = Flask(__name__)"],"id":1257},{"start":{"row":21,"column":17},"end":{"row":22,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":53},"action":"remove","lines":["    app.config['SECRET_KEY'] = 'secret-key-goes-here'"],"id":1258}],[{"start":{"row":22,"column":0},"end":{"row":23,"column":0},"action":"remove","lines":["",""],"id":1259}],[{"start":{"row":57,"column":26},"end":{"row":58,"column":0},"action":"insert","lines":["",""],"id":1260},{"start":{"row":58,"column":0},"end":{"row":58,"column":4},"action":"insert","lines":["    "]},{"start":{"row":58,"column":4},"end":{"row":59,"column":0},"action":"insert","lines":["",""]},{"start":{"row":59,"column":0},"end":{"row":59,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":59,"column":0},"end":{"row":59,"column":4},"action":"remove","lines":["    "],"id":1261}],[{"start":{"row":59,"column":0},"end":{"row":61,"column":26},"action":"insert","lines":["@app.route(\"/account/login\")","def log_in():","    return \"Account/Login\""],"id":1262}],[{"start":{"row":59,"column":25},"end":{"row":59,"column":26},"action":"remove","lines":["n"],"id":1263},{"start":{"row":59,"column":24},"end":{"row":59,"column":25},"action":"remove","lines":["i"]}],[{"start":{"row":59,"column":24},"end":{"row":59,"column":25},"action":"insert","lines":["o"],"id":1264},{"start":{"row":59,"column":25},"end":{"row":59,"column":26},"action":"insert","lines":["u"]},{"start":{"row":59,"column":26},"end":{"row":59,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":60,"column":7},"end":{"row":60,"column":10},"action":"remove","lines":["_in"],"id":1265},{"start":{"row":60,"column":7},"end":{"row":60,"column":8},"action":"insert","lines":["p"]},{"start":{"row":60,"column":8},"end":{"row":60,"column":9},"action":"insert","lines":["i"]},{"start":{"row":60,"column":9},"end":{"row":60,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":60,"column":9},"end":{"row":60,"column":10},"action":"remove","lines":["t"],"id":1266},{"start":{"row":60,"column":8},"end":{"row":60,"column":9},"action":"remove","lines":["i"]},{"start":{"row":60,"column":7},"end":{"row":60,"column":8},"action":"remove","lines":["p"]}],[{"start":{"row":60,"column":7},"end":{"row":60,"column":8},"action":"insert","lines":["o"],"id":1267},{"start":{"row":60,"column":8},"end":{"row":60,"column":9},"action":"insert","lines":["u"]},{"start":{"row":60,"column":9},"end":{"row":60,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":56,"column":7},"end":{"row":56,"column":10},"action":"remove","lines":["_in"],"id":1268},{"start":{"row":56,"column":7},"end":{"row":56,"column":8},"action":"insert","lines":["i"]},{"start":{"row":56,"column":8},"end":{"row":56,"column":9},"action":"insert","lines":["n"]}],[{"start":{"row":61,"column":23},"end":{"row":61,"column":24},"action":"remove","lines":["i"],"id":1269},{"start":{"row":61,"column":23},"end":{"row":61,"column":24},"action":"insert","lines":["o"]},{"start":{"row":61,"column":24},"end":{"row":61,"column":25},"action":"insert","lines":["u"]},{"start":{"row":61,"column":25},"end":{"row":61,"column":26},"action":"insert","lines":["t"]}],[{"start":{"row":61,"column":26},"end":{"row":61,"column":27},"action":"remove","lines":["n"],"id":1270}],[{"start":{"row":40,"column":11},"end":{"row":40,"column":25},"action":"remove","lines":["'Hello World!'"],"id":1271},{"start":{"row":40,"column":11},"end":{"row":40,"column":40},"action":"insert","lines":["render_template('index.html')"]}],[{"start":{"row":49,"column":11},"end":{"row":49,"column":27},"action":"remove","lines":["\"Account/Profile"],"id":1272},{"start":{"row":49,"column":11},"end":{"row":49,"column":42},"action":"insert","lines":["render_template('profile.html')"]}],[{"start":{"row":49,"column":28},"end":{"row":49,"column":29},"action":"insert","lines":["/"],"id":1273},{"start":{"row":49,"column":29},"end":{"row":49,"column":30},"action":"insert","lines":["a"]},{"start":{"row":49,"column":30},"end":{"row":49,"column":31},"action":"insert","lines":["c"]},{"start":{"row":49,"column":31},"end":{"row":49,"column":32},"action":"insert","lines":["c"]},{"start":{"row":49,"column":32},"end":{"row":49,"column":33},"action":"insert","lines":["o"]},{"start":{"row":49,"column":33},"end":{"row":49,"column":34},"action":"insert","lines":["u"]}],[{"start":{"row":49,"column":34},"end":{"row":49,"column":35},"action":"insert","lines":["n"],"id":1274}],[{"start":{"row":49,"column":34},"end":{"row":49,"column":35},"action":"remove","lines":["n"],"id":1275},{"start":{"row":49,"column":33},"end":{"row":49,"column":34},"action":"remove","lines":["u"]},{"start":{"row":49,"column":32},"end":{"row":49,"column":33},"action":"remove","lines":["o"]},{"start":{"row":49,"column":31},"end":{"row":49,"column":32},"action":"remove","lines":["c"]},{"start":{"row":49,"column":30},"end":{"row":49,"column":31},"action":"remove","lines":["c"]},{"start":{"row":49,"column":29},"end":{"row":49,"column":30},"action":"remove","lines":["a"]}],[{"start":{"row":49,"column":28},"end":{"row":49,"column":29},"action":"remove","lines":["/"],"id":1276}],[{"start":{"row":49,"column":28},"end":{"row":49,"column":29},"action":"insert","lines":["a"],"id":1277},{"start":{"row":49,"column":29},"end":{"row":49,"column":30},"action":"insert","lines":["c"]},{"start":{"row":49,"column":30},"end":{"row":49,"column":31},"action":"insert","lines":["c"]},{"start":{"row":49,"column":31},"end":{"row":49,"column":32},"action":"insert","lines":["o"]},{"start":{"row":49,"column":32},"end":{"row":49,"column":33},"action":"insert","lines":["u"]},{"start":{"row":49,"column":33},"end":{"row":49,"column":34},"action":"insert","lines":["n"]},{"start":{"row":49,"column":34},"end":{"row":49,"column":35},"action":"insert","lines":["t"]},{"start":{"row":49,"column":35},"end":{"row":49,"column":36},"action":"insert","lines":["/"]}],[{"start":{"row":49,"column":50},"end":{"row":49,"column":51},"action":"remove","lines":["\""],"id":1278}],[{"start":{"row":40,"column":40},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":1279},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]},{"start":{"row":41,"column":4},"end":{"row":42,"column":0},"action":"insert","lines":["",""]},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"remove","lines":["    "],"id":1280}],[{"start":{"row":42,"column":0},"end":{"row":42,"column":1},"action":"insert","lines":["#"],"id":1281},{"start":{"row":42,"column":1},"end":{"row":42,"column":2},"action":"insert","lines":["#"]}],[{"start":{"row":42,"column":2},"end":{"row":42,"column":4},"action":"insert","lines":["''"],"id":1282}],[{"start":{"row":42,"column":3},"end":{"row":42,"column":4},"action":"insert","lines":["D"],"id":1283}],[{"start":{"row":42,"column":3},"end":{"row":42,"column":4},"action":"remove","lines":["D"],"id":1284},{"start":{"row":42,"column":2},"end":{"row":42,"column":4},"action":"remove","lines":["''"]}],[{"start":{"row":42,"column":2},"end":{"row":42,"column":3},"action":"insert","lines":["D"],"id":1285}],[{"start":{"row":42,"column":2},"end":{"row":42,"column":3},"action":"remove","lines":["D"],"id":1286}],[{"start":{"row":42,"column":2},"end":{"row":42,"column":3},"action":"insert","lines":[" "],"id":1287},{"start":{"row":42,"column":3},"end":{"row":42,"column":4},"action":"insert","lines":["D"]},{"start":{"row":42,"column":4},"end":{"row":42,"column":5},"action":"insert","lines":["y"]},{"start":{"row":42,"column":5},"end":{"row":42,"column":6},"action":"insert","lines":["n"]},{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"insert","lines":["a"]},{"start":{"row":42,"column":7},"end":{"row":42,"column":8},"action":"insert","lines":["m"]},{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"insert","lines":["o"]},{"start":{"row":42,"column":9},"end":{"row":42,"column":10},"action":"insert","lines":["D"]}],[{"start":{"row":42,"column":10},"end":{"row":42,"column":11},"action":"insert","lines":["B"],"id":1288}],[{"start":{"row":42,"column":11},"end":{"row":43,"column":0},"action":"insert","lines":["",""],"id":1289},{"start":{"row":43,"column":0},"end":{"row":43,"column":1},"action":"insert","lines":["a"]},{"start":{"row":43,"column":1},"end":{"row":43,"column":2},"action":"insert","lines":["p"]},{"start":{"row":43,"column":2},"end":{"row":43,"column":3},"action":"insert","lines":["p"]}],[{"start":{"row":43,"column":2},"end":{"row":43,"column":3},"action":"remove","lines":["p"],"id":1290},{"start":{"row":43,"column":1},"end":{"row":43,"column":2},"action":"remove","lines":["p"]},{"start":{"row":43,"column":0},"end":{"row":43,"column":1},"action":"remove","lines":["a"]}],[{"start":{"row":43,"column":0},"end":{"row":43,"column":1},"action":"insert","lines":["@"],"id":1291},{"start":{"row":43,"column":1},"end":{"row":43,"column":2},"action":"insert","lines":["a"]},{"start":{"row":43,"column":2},"end":{"row":43,"column":3},"action":"insert","lines":["p"]},{"start":{"row":43,"column":3},"end":{"row":43,"column":4},"action":"insert","lines":["p"]},{"start":{"row":43,"column":4},"end":{"row":43,"column":5},"action":"insert","lines":["."]}],[{"start":{"row":43,"column":5},"end":{"row":43,"column":6},"action":"insert","lines":["r"],"id":1292},{"start":{"row":43,"column":6},"end":{"row":43,"column":7},"action":"insert","lines":["o"]},{"start":{"row":43,"column":7},"end":{"row":43,"column":8},"action":"insert","lines":["u"]},{"start":{"row":43,"column":8},"end":{"row":43,"column":9},"action":"insert","lines":["t"]},{"start":{"row":43,"column":9},"end":{"row":43,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":43,"column":10},"end":{"row":43,"column":12},"action":"insert","lines":["()"],"id":1293}],[{"start":{"row":43,"column":11},"end":{"row":43,"column":13},"action":"insert","lines":["''"],"id":1294}],[{"start":{"row":43,"column":12},"end":{"row":43,"column":13},"action":"insert","lines":["/"],"id":1295},{"start":{"row":43,"column":13},"end":{"row":43,"column":14},"action":"insert","lines":["g"]},{"start":{"row":43,"column":14},"end":{"row":43,"column":15},"action":"insert","lines":["e"]},{"start":{"row":43,"column":15},"end":{"row":43,"column":16},"action":"insert","lines":["t"]},{"start":{"row":43,"column":16},"end":{"row":43,"column":17},"action":"insert","lines":["-"]},{"start":{"row":43,"column":17},"end":{"row":43,"column":18},"action":"insert","lines":["i"]},{"start":{"row":43,"column":18},"end":{"row":43,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":43,"column":19},"end":{"row":43,"column":20},"action":"insert","lines":["e"],"id":1296},{"start":{"row":43,"column":20},"end":{"row":43,"column":21},"action":"insert","lines":["m"]},{"start":{"row":43,"column":21},"end":{"row":43,"column":22},"action":"insert","lines":["s"]}],[{"start":{"row":43,"column":24},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":1297},{"start":{"row":44,"column":0},"end":{"row":44,"column":1},"action":"insert","lines":["d"]},{"start":{"row":44,"column":1},"end":{"row":44,"column":2},"action":"insert","lines":["e"]},{"start":{"row":44,"column":2},"end":{"row":44,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":44,"column":3},"end":{"row":44,"column":4},"action":"insert","lines":[" "],"id":1298},{"start":{"row":44,"column":4},"end":{"row":44,"column":5},"action":"insert","lines":["g"]},{"start":{"row":44,"column":5},"end":{"row":44,"column":6},"action":"insert","lines":["e"]},{"start":{"row":44,"column":6},"end":{"row":44,"column":7},"action":"insert","lines":["t"]},{"start":{"row":44,"column":7},"end":{"row":44,"column":8},"action":"insert","lines":["_"]},{"start":{"row":44,"column":8},"end":{"row":44,"column":9},"action":"insert","lines":["i"]},{"start":{"row":44,"column":9},"end":{"row":44,"column":10},"action":"insert","lines":["t"]},{"start":{"row":44,"column":10},"end":{"row":44,"column":11},"action":"insert","lines":["e"]},{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"insert","lines":["m"]},{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":44,"column":13},"end":{"row":44,"column":15},"action":"insert","lines":["()"],"id":1299}],[{"start":{"row":44,"column":15},"end":{"row":44,"column":16},"action":"insert","lines":[":"],"id":1300}],[{"start":{"row":44,"column":16},"end":{"row":45,"column":0},"action":"insert","lines":["",""],"id":1301},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]},{"start":{"row":45,"column":4},"end":{"row":45,"column":5},"action":"insert","lines":["r"]},{"start":{"row":45,"column":5},"end":{"row":45,"column":6},"action":"insert","lines":["e"]},{"start":{"row":45,"column":6},"end":{"row":45,"column":7},"action":"insert","lines":["t"]},{"start":{"row":45,"column":7},"end":{"row":45,"column":8},"action":"insert","lines":["u"]},{"start":{"row":45,"column":8},"end":{"row":45,"column":9},"action":"insert","lines":["r"]},{"start":{"row":45,"column":9},"end":{"row":45,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":45,"column":10},"end":{"row":45,"column":11},"action":"insert","lines":[" "],"id":1302},{"start":{"row":45,"column":11},"end":{"row":45,"column":12},"action":"insert","lines":["j"]},{"start":{"row":45,"column":12},"end":{"row":45,"column":13},"action":"insert","lines":["s"]},{"start":{"row":45,"column":13},"end":{"row":45,"column":14},"action":"insert","lines":["o"]},{"start":{"row":45,"column":14},"end":{"row":45,"column":15},"action":"insert","lines":["n"]},{"start":{"row":45,"column":15},"end":{"row":45,"column":16},"action":"insert","lines":["i"]}],[{"start":{"row":45,"column":16},"end":{"row":45,"column":17},"action":"insert","lines":["f"],"id":1303},{"start":{"row":45,"column":17},"end":{"row":45,"column":18},"action":"insert","lines":["y"]}],[{"start":{"row":45,"column":18},"end":{"row":45,"column":20},"action":"insert","lines":["()"],"id":1304}],[{"start":{"row":45,"column":19},"end":{"row":45,"column":20},"action":"insert","lines":["a"],"id":1305},{"start":{"row":45,"column":20},"end":{"row":45,"column":21},"action":"insert","lines":["w"]},{"start":{"row":45,"column":21},"end":{"row":45,"column":22},"action":"insert","lines":["s"]},{"start":{"row":45,"column":22},"end":{"row":45,"column":23},"action":"insert","lines":["_"]},{"start":{"row":45,"column":23},"end":{"row":45,"column":24},"action":"insert","lines":["c"]}],[{"start":{"row":45,"column":24},"end":{"row":45,"column":25},"action":"insert","lines":["o"],"id":1306},{"start":{"row":45,"column":25},"end":{"row":45,"column":26},"action":"insert","lines":["n"]},{"start":{"row":45,"column":26},"end":{"row":45,"column":27},"action":"insert","lines":["t"]},{"start":{"row":45,"column":27},"end":{"row":45,"column":28},"action":"insert","lines":["r"]},{"start":{"row":45,"column":28},"end":{"row":45,"column":29},"action":"insert","lines":["o"]},{"start":{"row":45,"column":29},"end":{"row":45,"column":30},"action":"insert","lines":["l"]},{"start":{"row":45,"column":30},"end":{"row":45,"column":31},"action":"insert","lines":["l"]},{"start":{"row":45,"column":31},"end":{"row":45,"column":32},"action":"insert","lines":["e"]},{"start":{"row":45,"column":32},"end":{"row":45,"column":33},"action":"insert","lines":["r"]},{"start":{"row":45,"column":33},"end":{"row":45,"column":34},"action":"insert","lines":["."]}],[{"start":{"row":45,"column":34},"end":{"row":45,"column":35},"action":"insert","lines":["g"],"id":1307},{"start":{"row":45,"column":35},"end":{"row":45,"column":36},"action":"insert","lines":["e"]},{"start":{"row":45,"column":36},"end":{"row":45,"column":37},"action":"insert","lines":["t"]}],[{"start":{"row":45,"column":34},"end":{"row":45,"column":37},"action":"remove","lines":["get"],"id":1308},{"start":{"row":45,"column":34},"end":{"row":45,"column":43},"action":"insert","lines":["get_items"]}],[{"start":{"row":45,"column":43},"end":{"row":45,"column":45},"action":"insert","lines":["()"],"id":1309}],[{"start":{"row":2,"column":79},"end":{"row":2,"column":80},"action":"insert","lines":[","],"id":1310}],[{"start":{"row":2,"column":80},"end":{"row":2,"column":81},"action":"insert","lines":[" "],"id":1311}],[{"start":{"row":2,"column":81},"end":{"row":2,"column":82},"action":"insert","lines":["j"],"id":1312},{"start":{"row":2,"column":82},"end":{"row":2,"column":83},"action":"insert","lines":["s"]},{"start":{"row":2,"column":83},"end":{"row":2,"column":84},"action":"insert","lines":["o"]},{"start":{"row":2,"column":84},"end":{"row":2,"column":85},"action":"insert","lines":["n"]},{"start":{"row":2,"column":85},"end":{"row":2,"column":86},"action":"insert","lines":["i"]},{"start":{"row":2,"column":86},"end":{"row":2,"column":87},"action":"insert","lines":["f"]},{"start":{"row":2,"column":87},"end":{"row":2,"column":88},"action":"insert","lines":["y"]}],[{"start":{"row":3,"column":39},"end":{"row":3,"column":40},"action":"insert","lines":["y"],"id":1330}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"insert","lines":["f"],"id":1331},{"start":{"row":4,"column":1},"end":{"row":4,"column":2},"action":"insert","lines":["r"]},{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"insert","lines":["o"]},{"start":{"row":4,"column":3},"end":{"row":4,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":[" "],"id":1332},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["a"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["w"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["s"]}],[{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":["_"],"id":1333},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":["c"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":["o"]},{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":["m"]}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"remove","lines":["m"],"id":1334}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":["n"],"id":1335},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["t"]},{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["r"]},{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["o"]},{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["l"]},{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["l"]},{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["e"]},{"start":{"row":4,"column":18},"end":{"row":4,"column":19},"action":"insert","lines":["r"]}],[{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"insert","lines":[" "],"id":1336},{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"insert","lines":["i"]},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"insert","lines":["m"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"insert","lines":["p"]},{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"insert","lines":["o"]},{"start":{"row":4,"column":24},"end":{"row":4,"column":25},"action":"insert","lines":["r"]},{"start":{"row":4,"column":25},"end":{"row":4,"column":26},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"insert","lines":[" "],"id":1337}],[{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"insert","lines":["g"],"id":1338},{"start":{"row":4,"column":28},"end":{"row":4,"column":29},"action":"insert","lines":["e"]},{"start":{"row":4,"column":29},"end":{"row":4,"column":30},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"insert","lines":["_"],"id":1339},{"start":{"row":4,"column":31},"end":{"row":4,"column":32},"action":"insert","lines":["i"]},{"start":{"row":4,"column":32},"end":{"row":4,"column":33},"action":"insert","lines":["t"]},{"start":{"row":4,"column":33},"end":{"row":4,"column":34},"action":"insert","lines":["e"]},{"start":{"row":4,"column":34},"end":{"row":4,"column":35},"action":"insert","lines":["m"]},{"start":{"row":4,"column":35},"end":{"row":4,"column":36},"action":"insert","lines":["s"]},{"start":{"row":4,"column":36},"end":{"row":4,"column":37},"action":"insert","lines":[","]}],[{"start":{"row":4,"column":37},"end":{"row":4,"column":38},"action":"insert","lines":[" "],"id":1340},{"start":{"row":4,"column":38},"end":{"row":4,"column":39},"action":"insert","lines":["g"]},{"start":{"row":4,"column":39},"end":{"row":4,"column":40},"action":"insert","lines":["e"]},{"start":{"row":4,"column":40},"end":{"row":4,"column":41},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":41},"end":{"row":4,"column":42},"action":"insert","lines":[" "],"id":1341},{"start":{"row":4,"column":42},"end":{"row":4,"column":43},"action":"insert","lines":["i"]},{"start":{"row":4,"column":43},"end":{"row":4,"column":44},"action":"insert","lines":["t"]},{"start":{"row":4,"column":44},"end":{"row":4,"column":45},"action":"insert","lines":["e"]},{"start":{"row":4,"column":45},"end":{"row":4,"column":46},"action":"insert","lines":["m"]},{"start":{"row":4,"column":46},"end":{"row":4,"column":47},"action":"insert","lines":[","]}],[{"start":{"row":4,"column":47},"end":{"row":4,"column":48},"action":"insert","lines":[" "],"id":1342}],[{"start":{"row":4,"column":48},"end":{"row":4,"column":49},"action":"insert","lines":["n"],"id":1343},{"start":{"row":4,"column":49},"end":{"row":4,"column":50},"action":"insert","lines":["e"]},{"start":{"row":4,"column":50},"end":{"row":4,"column":51},"action":"insert","lines":["w"]}],[{"start":{"row":4,"column":51},"end":{"row":4,"column":52},"action":"insert","lines":["_"],"id":1344},{"start":{"row":4,"column":52},"end":{"row":4,"column":53},"action":"insert","lines":["i"]},{"start":{"row":4,"column":53},"end":{"row":4,"column":54},"action":"insert","lines":["t"]},{"start":{"row":4,"column":54},"end":{"row":4,"column":55},"action":"insert","lines":["e"]},{"start":{"row":4,"column":55},"end":{"row":4,"column":56},"action":"insert","lines":["m"]}],[{"start":{"row":4,"column":56},"end":{"row":4,"column":57},"action":"insert","lines":[","],"id":1345}],[{"start":{"row":4,"column":57},"end":{"row":4,"column":58},"action":"insert","lines":[" "],"id":1346},{"start":{"row":4,"column":58},"end":{"row":4,"column":59},"action":"insert","lines":["u"]},{"start":{"row":4,"column":59},"end":{"row":4,"column":60},"action":"insert","lines":["p"]},{"start":{"row":4,"column":60},"end":{"row":4,"column":61},"action":"insert","lines":["d"]},{"start":{"row":4,"column":61},"end":{"row":4,"column":62},"action":"insert","lines":["a"]},{"start":{"row":4,"column":62},"end":{"row":4,"column":63},"action":"insert","lines":["t"]},{"start":{"row":4,"column":63},"end":{"row":4,"column":64},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":64},"end":{"row":4,"column":65},"action":"insert","lines":["_"],"id":1347},{"start":{"row":4,"column":65},"end":{"row":4,"column":66},"action":"insert","lines":["i"]},{"start":{"row":4,"column":66},"end":{"row":4,"column":67},"action":"insert","lines":["t"]},{"start":{"row":4,"column":67},"end":{"row":4,"column":68},"action":"insert","lines":["e"]},{"start":{"row":4,"column":68},"end":{"row":4,"column":69},"action":"insert","lines":["m"]},{"start":{"row":4,"column":69},"end":{"row":4,"column":70},"action":"insert","lines":[","]}],[{"start":{"row":4,"column":70},"end":{"row":4,"column":71},"action":"insert","lines":["d"],"id":1348},{"start":{"row":4,"column":71},"end":{"row":4,"column":72},"action":"insert","lines":["e"]},{"start":{"row":4,"column":72},"end":{"row":4,"column":73},"action":"insert","lines":["l"]},{"start":{"row":4,"column":73},"end":{"row":4,"column":74},"action":"insert","lines":["e"]},{"start":{"row":4,"column":74},"end":{"row":4,"column":75},"action":"insert","lines":["t"]},{"start":{"row":4,"column":75},"end":{"row":4,"column":76},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":76},"end":{"row":4,"column":77},"action":"insert","lines":[" "],"id":1349}],[{"start":{"row":4,"column":76},"end":{"row":4,"column":77},"action":"remove","lines":[" "],"id":1350},{"start":{"row":4,"column":76},"end":{"row":4,"column":77},"action":"insert","lines":["_"]},{"start":{"row":4,"column":77},"end":{"row":4,"column":78},"action":"insert","lines":["i"]},{"start":{"row":4,"column":78},"end":{"row":4,"column":79},"action":"insert","lines":["t"]},{"start":{"row":4,"column":79},"end":{"row":4,"column":80},"action":"insert","lines":["e"]},{"start":{"row":4,"column":80},"end":{"row":4,"column":81},"action":"insert","lines":["m"]}],[{"start":{"row":4,"column":70},"end":{"row":4,"column":71},"action":"insert","lines":[" "],"id":1351}],[{"start":{"row":4,"column":41},"end":{"row":4,"column":42},"action":"remove","lines":[" "],"id":1352},{"start":{"row":4,"column":41},"end":{"row":4,"column":42},"action":"insert","lines":["_"]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":2},"action":"insert","lines":["# "],"id":1354}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":2},"action":"insert","lines":["# "],"id":1355}],[{"start":{"row":4,"column":27},"end":{"row":4,"column":82},"action":"remove","lines":["get_items, get_item, new_item, update_item, delete_item"],"id":1356},{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"remove","lines":[" "]}],[{"start":{"row":4,"column":5},"end":{"row":4,"column":19},"action":"remove","lines":["aws_controller"],"id":1357}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":[" "],"id":1358}],[{"start":{"row":4,"column":13},"end":{"row":4,"column":27},"action":"insert","lines":["aws_controller"],"id":1359}],[{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"remove","lines":[" "],"id":1360},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"remove","lines":[" "]},{"start":{"row":4,"column":3},"end":{"row":4,"column":4},"action":"remove","lines":["m"]},{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"remove","lines":["o"]},{"start":{"row":4,"column":1},"end":{"row":4,"column":2},"action":"remove","lines":["r"]},{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"remove","lines":["f"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":4,"column":0},"end":{"row":4,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":true,"wrapToView":true},"firstLineState":0},"timestamp":1639668197586,"hash":"c15a8bf8817753fcb37cd563e83ec7b20f9d2edf"}