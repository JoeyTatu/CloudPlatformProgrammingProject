{"filter":false,"title":"dynamodb_setup.py","tooltip":"/flaskapp/dynamodb_setup.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"remove","lines":[":"],"id":20},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["="]}],[{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"remove","lines":[":"],"id":21},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["="]}],[{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"remove","lines":["="],"id":23},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["="]}],[{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"remove","lines":["="],"id":24}],[{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"remove","lines":[" "],"id":28},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":[" "]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"remove","lines":["'"]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["="]}],[{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"remove","lines":["U"],"id":29},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":[" "]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"remove","lines":["s"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["\""]}],[{"start":{"row":8,"column":20},"end":{"row":8,"column":26},"action":"remove","lines":["\"ers',"],"id":30},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["\""]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["U"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["s"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["e"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["r"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["s"]}],[{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["\""],"id":31},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":[","]}],[{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"remove","lines":[" "],"id":32}],[{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":[" "],"id":33}],[{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":[" "],"id":34}],[{"start":{"row":13,"column":14},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":14,"column":0},"end":{"row":14,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":14,"column":41},"end":{"row":14,"column":42},"action":"remove","lines":[" "],"id":36}],[{"start":{"row":14,"column":41},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":15,"column":0},"end":{"row":15,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":17,"column":30},"end":{"row":17,"column":32},"action":"remove","lines":[": "],"id":38},{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"insert","lines":["="]}],[{"start":{"row":21,"column":31},"end":{"row":21,"column":32},"action":"remove","lines":[":"],"id":39},{"start":{"row":21,"column":31},"end":{"row":21,"column":32},"action":"insert","lines":["="]}],[{"start":{"row":10,"column":0},"end":{"row":25,"column":5},"action":"remove","lines":["            { ","                'AttributeName': \"id\",","                \"KeyType\": \"HASH\" },","            { ","                \"AttributeName\": \"email\",","                \"KeyType\": \"RANGE\" }","        ],","        \"AttributeDefinitions\"=[","            { \"AttributeName\": \"id\", \"AttributeType\": \"N\" },","            { \"AttributeName\": \"email\", \"AttributeType\": \"S\" }","        ],","        \"ProvisionedThroughput\"= {","            \"ReadCapacityUnits\": 10,","            \"WriteCapacityUnits\": 10","        }","    )"],"id":40},{"start":{"row":10,"column":0},"end":{"row":25,"column":5},"action":"insert","lines":["            { ","                'AttributeName': 'id',","                'KeyType': 'HASH' },","            { ","                'AttributeName': 'email',","                'KeyType': 'RANGE' }","        ],","        'AttributeDefinitions'=[","            { 'AttributeName': 'id', 'AttributeType': 'N' },","            { 'AttributeName': 'email', 'AttributeType': 'S' }","        ],","        'ProvisionedThroughput'= {","            'ReadCapacityUnits': 10,","            'WriteCapacityUnits': 10","        }","    )"]}],[{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"insert","lines":[" "],"id":41}],[{"start":{"row":21,"column":32},"end":{"row":21,"column":33},"action":"remove","lines":[" "],"id":42}],[{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"remove","lines":["'"],"id":43}],[{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"remove","lines":["'"],"id":44}],[{"start":{"row":21,"column":30},"end":{"row":21,"column":31},"action":"remove","lines":["'"],"id":45}],[{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"remove","lines":["'"],"id":46}],[{"start":{"row":30,"column":25},"end":{"row":30,"column":30},"action":"remove","lines":["movie"],"id":47},{"start":{"row":30,"column":25},"end":{"row":30,"column":26},"action":"insert","lines":["U"]}],[{"start":{"row":30,"column":25},"end":{"row":30,"column":26},"action":"remove","lines":["U"],"id":48}],[{"start":{"row":30,"column":25},"end":{"row":30,"column":26},"action":"insert","lines":["u"],"id":49},{"start":{"row":30,"column":26},"end":{"row":30,"column":27},"action":"insert","lines":["s"]},{"start":{"row":30,"column":27},"end":{"row":30,"column":28},"action":"insert","lines":["e"]},{"start":{"row":30,"column":28},"end":{"row":30,"column":29},"action":"insert","lines":["r"]}],[{"start":{"row":3,"column":11},"end":{"row":3,"column":15},"action":"remove","lines":["movi"],"id":50},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["u"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["s"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["e"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["r"]}],[{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"remove","lines":["e"],"id":51}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["#"],"id":52},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["C"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["r"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["e"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["a"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["e"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["s"]}],[{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":[" "],"id":53},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["t"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["h"]},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":[" "],"id":54},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["t"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["a"]},{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":["b"]},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["l"]},{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":[" "],"id":55},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["f"]},{"start":{"row":0,"column":20},"end":{"row":0,"column":21},"action":"insert","lines":["o"]},{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"insert","lines":["r"]}],[{"start":{"row":0,"column":22},"end":{"row":0,"column":23},"action":"insert","lines":[" "],"id":56},{"start":{"row":0,"column":23},"end":{"row":0,"column":24},"action":"insert","lines":["t"]},{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"insert","lines":["h"]},{"start":{"row":0,"column":25},"end":{"row":0,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":26},"end":{"row":0,"column":27},"action":"insert","lines":[" "],"id":57},{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"insert","lines":["S"]}],[{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"remove","lines":["S"],"id":58}],[{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"insert","lines":["D"],"id":59},{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"insert","lines":["y"]},{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"insert","lines":["n"]},{"start":{"row":0,"column":30},"end":{"row":0,"column":31},"action":"insert","lines":["a"]},{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"insert","lines":["m"]},{"start":{"row":0,"column":32},"end":{"row":0,"column":33},"action":"insert","lines":["o"]},{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"insert","lines":["D"]}],[{"start":{"row":0,"column":34},"end":{"row":0,"column":35},"action":"insert","lines":["B"],"id":60},{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"insert","lines":[","]}],[{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"insert","lines":[" "],"id":61},{"start":{"row":0,"column":37},"end":{"row":0,"column":38},"action":"insert","lines":["o"]},{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"insert","lines":["n"]},{"start":{"row":0,"column":39},"end":{"row":0,"column":40},"action":"insert","lines":["y"]}],[{"start":{"row":0,"column":39},"end":{"row":0,"column":40},"action":"remove","lines":["y"],"id":62}],[{"start":{"row":0,"column":39},"end":{"row":0,"column":40},"action":"insert","lines":[";"],"id":63},{"start":{"row":0,"column":40},"end":{"row":0,"column":41},"action":"insert","lines":["y"]}],[{"start":{"row":0,"column":40},"end":{"row":0,"column":41},"action":"remove","lines":["y"],"id":64},{"start":{"row":0,"column":39},"end":{"row":0,"column":40},"action":"remove","lines":[";"]}],[{"start":{"row":0,"column":39},"end":{"row":0,"column":40},"action":"insert","lines":["l"],"id":65},{"start":{"row":0,"column":40},"end":{"row":0,"column":41},"action":"insert","lines":["y"]}],[{"start":{"row":0,"column":41},"end":{"row":0,"column":42},"action":"insert","lines":[" "],"id":66},{"start":{"row":0,"column":42},"end":{"row":0,"column":43},"action":"insert","lines":["t"]},{"start":{"row":0,"column":43},"end":{"row":0,"column":44},"action":"insert","lines":["h"]},{"start":{"row":0,"column":44},"end":{"row":0,"column":45},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":45},"end":{"row":0,"column":46},"action":"insert","lines":[" "],"id":67}],[{"start":{"row":0,"column":46},"end":{"row":0,"column":47},"action":"insert","lines":["i"],"id":68},{"start":{"row":0,"column":47},"end":{"row":0,"column":48},"action":"insert","lines":["f"]}],[{"start":{"row":0,"column":47},"end":{"row":0,"column":48},"action":"remove","lines":["f"],"id":69}],[{"start":{"row":0,"column":47},"end":{"row":0,"column":48},"action":"insert","lines":["d"],"id":70},{"start":{"row":0,"column":48},"end":{"row":0,"column":49},"action":"insert","lines":["e"]},{"start":{"row":0,"column":49},"end":{"row":0,"column":50},"action":"insert","lines":["f"]}],[{"start":{"row":0,"column":49},"end":{"row":0,"column":50},"action":"remove","lines":["f"],"id":71}],[{"start":{"row":0,"column":49},"end":{"row":0,"column":50},"action":"insert","lines":["n"],"id":72},{"start":{"row":0,"column":50},"end":{"row":0,"column":51},"action":"insert","lines":["y"]}],[{"start":{"row":0,"column":50},"end":{"row":0,"column":51},"action":"remove","lines":["y"],"id":73}],[{"start":{"row":0,"column":50},"end":{"row":0,"column":51},"action":"insert","lines":["t"],"id":74},{"start":{"row":0,"column":51},"end":{"row":0,"column":52},"action":"insert","lines":["i"]},{"start":{"row":0,"column":52},"end":{"row":0,"column":53},"action":"insert","lines":["f"]},{"start":{"row":0,"column":53},"end":{"row":0,"column":54},"action":"insert","lines":["y"]},{"start":{"row":0,"column":54},"end":{"row":0,"column":55},"action":"insert","lines":["i"]},{"start":{"row":0,"column":55},"end":{"row":0,"column":56},"action":"insert","lines":["n"]},{"start":{"row":0,"column":56},"end":{"row":0,"column":57},"action":"insert","lines":["h"]}],[{"start":{"row":0,"column":57},"end":{"row":0,"column":58},"action":"insert","lines":[" "],"id":75}],[{"start":{"row":0,"column":57},"end":{"row":0,"column":58},"action":"remove","lines":[" "],"id":76},{"start":{"row":0,"column":56},"end":{"row":0,"column":57},"action":"remove","lines":["h"]}],[{"start":{"row":0,"column":56},"end":{"row":0,"column":57},"action":"insert","lines":["f"],"id":77}],[{"start":{"row":0,"column":56},"end":{"row":0,"column":57},"action":"remove","lines":["f"],"id":78}],[{"start":{"row":0,"column":56},"end":{"row":0,"column":57},"action":"insert","lines":["g"],"id":79}],[{"start":{"row":0,"column":57},"end":{"row":0,"column":58},"action":"insert","lines":[" "],"id":80},{"start":{"row":0,"column":58},"end":{"row":0,"column":59},"action":"insert","lines":["f"]},{"start":{"row":0,"column":59},"end":{"row":0,"column":60},"action":"insert","lines":["a"]},{"start":{"row":0,"column":60},"end":{"row":0,"column":61},"action":"insert","lines":["c"]},{"start":{"row":0,"column":61},"end":{"row":0,"column":62},"action":"insert","lines":["t"]},{"start":{"row":0,"column":62},"end":{"row":0,"column":63},"action":"insert","lines":["o"]},{"start":{"row":0,"column":63},"end":{"row":0,"column":64},"action":"insert","lines":["r"]},{"start":{"row":0,"column":64},"end":{"row":0,"column":65},"action":"insert","lines":["s"]}],[{"start":{"row":0,"column":65},"end":{"row":0,"column":66},"action":"insert","lines":[" "],"id":81},{"start":{"row":0,"column":66},"end":{"row":0,"column":67},"action":"insert","lines":["a"]},{"start":{"row":0,"column":67},"end":{"row":0,"column":68},"action":"insert","lines":["r"]},{"start":{"row":0,"column":68},"end":{"row":0,"column":69},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":69},"end":{"row":0,"column":70},"action":"insert","lines":[" "],"id":82},{"start":{"row":0,"column":70},"end":{"row":0,"column":71},"action":"insert","lines":["n"]},{"start":{"row":0,"column":71},"end":{"row":0,"column":72},"action":"insert","lines":["e"]},{"start":{"row":0,"column":72},"end":{"row":0,"column":73},"action":"insert","lines":["e"]},{"start":{"row":0,"column":73},"end":{"row":0,"column":74},"action":"insert","lines":["d"]},{"start":{"row":0,"column":74},"end":{"row":0,"column":75},"action":"insert","lines":["e"]},{"start":{"row":0,"column":75},"end":{"row":0,"column":76},"action":"insert","lines":["d"]}],[{"start":{"row":0,"column":76},"end":{"row":0,"column":77},"action":"insert","lines":[" "],"id":83},{"start":{"row":0,"column":77},"end":{"row":0,"column":78},"action":"insert","lines":["d"]},{"start":{"row":0,"column":78},"end":{"row":0,"column":79},"action":"insert","lines":["u"]},{"start":{"row":0,"column":79},"end":{"row":0,"column":80},"action":"insert","lines":["r"]},{"start":{"row":0,"column":80},"end":{"row":0,"column":81},"action":"insert","lines":["i"]},{"start":{"row":0,"column":81},"end":{"row":0,"column":82},"action":"insert","lines":["n"]},{"start":{"row":0,"column":82},"end":{"row":0,"column":83},"action":"insert","lines":["g"]}],[{"start":{"row":0,"column":83},"end":{"row":0,"column":84},"action":"insert","lines":[" "],"id":84},{"start":{"row":0,"column":84},"end":{"row":0,"column":85},"action":"insert","lines":["c"]},{"start":{"row":0,"column":85},"end":{"row":0,"column":86},"action":"insert","lines":["r"]},{"start":{"row":0,"column":86},"end":{"row":0,"column":87},"action":"insert","lines":["e"]},{"start":{"row":0,"column":87},"end":{"row":0,"column":88},"action":"insert","lines":["a"]},{"start":{"row":0,"column":88},"end":{"row":0,"column":89},"action":"insert","lines":["t"]},{"start":{"row":0,"column":89},"end":{"row":0,"column":90},"action":"insert","lines":["i"]},{"start":{"row":0,"column":90},"end":{"row":0,"column":91},"action":"insert","lines":["o"]},{"start":{"row":0,"column":91},"end":{"row":0,"column":92},"action":"insert","lines":["n"]}],[{"start":{"row":0,"column":92},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":85}],[{"start":{"row":0,"column":66},"end":{"row":0,"column":67},"action":"insert","lines":["("],"id":86},{"start":{"row":0,"column":67},"end":{"row":0,"column":68},"action":"insert","lines":["i"]},{"start":{"row":0,"column":68},"end":{"row":0,"column":69},"action":"insert","lines":["d"]},{"start":{"row":0,"column":69},"end":{"row":0,"column":70},"action":"insert","lines":[","]}],[{"start":{"row":0,"column":70},"end":{"row":0,"column":71},"action":"insert","lines":[" "],"id":87},{"start":{"row":0,"column":71},"end":{"row":0,"column":72},"action":"insert","lines":["e"]},{"start":{"row":0,"column":72},"end":{"row":0,"column":73},"action":"insert","lines":["m"]},{"start":{"row":0,"column":73},"end":{"row":0,"column":74},"action":"insert","lines":["a"]},{"start":{"row":0,"column":74},"end":{"row":0,"column":75},"action":"insert","lines":["i"]},{"start":{"row":0,"column":75},"end":{"row":0,"column":76},"action":"insert","lines":["l"]},{"start":{"row":0,"column":76},"end":{"row":0,"column":77},"action":"insert","lines":[","]}],[{"start":{"row":0,"column":77},"end":{"row":0,"column":78},"action":"insert","lines":[" "],"id":88},{"start":{"row":0,"column":78},"end":{"row":0,"column":79},"action":"insert","lines":["n"]},{"start":{"row":0,"column":79},"end":{"row":0,"column":80},"action":"insert","lines":["o"]},{"start":{"row":0,"column":80},"end":{"row":0,"column":81},"action":"insert","lines":["t"]},{"start":{"row":0,"column":81},"end":{"row":0,"column":82},"action":"insert","lines":["h"]}],[{"start":{"row":0,"column":82},"end":{"row":0,"column":83},"action":"insert","lines":[" "],"id":89},{"start":{"row":0,"column":83},"end":{"row":0,"column":84},"action":"insert","lines":["u"]},{"start":{"row":0,"column":84},"end":{"row":0,"column":85},"action":"insert","lines":["n"]},{"start":{"row":0,"column":85},"end":{"row":0,"column":86},"action":"insert","lines":["i"]}],[{"start":{"row":0,"column":85},"end":{"row":0,"column":86},"action":"remove","lines":["i"],"id":90},{"start":{"row":0,"column":84},"end":{"row":0,"column":85},"action":"remove","lines":["n"]},{"start":{"row":0,"column":83},"end":{"row":0,"column":84},"action":"remove","lines":["u"]},{"start":{"row":0,"column":82},"end":{"row":0,"column":83},"action":"remove","lines":[" "]},{"start":{"row":0,"column":81},"end":{"row":0,"column":82},"action":"remove","lines":["h"]},{"start":{"row":0,"column":80},"end":{"row":0,"column":81},"action":"remove","lines":["t"]},{"start":{"row":0,"column":79},"end":{"row":0,"column":80},"action":"remove","lines":["o"]},{"start":{"row":0,"column":78},"end":{"row":0,"column":79},"action":"remove","lines":["n"]}],[{"start":{"row":0,"column":78},"end":{"row":0,"column":79},"action":"insert","lines":["b"],"id":91},{"start":{"row":0,"column":79},"end":{"row":0,"column":80},"action":"insert","lines":["o"]},{"start":{"row":0,"column":80},"end":{"row":0,"column":81},"action":"insert","lines":["t"]},{"start":{"row":0,"column":81},"end":{"row":0,"column":82},"action":"insert","lines":["h"]}],[{"start":{"row":0,"column":82},"end":{"row":0,"column":83},"action":"insert","lines":[" "],"id":92},{"start":{"row":0,"column":83},"end":{"row":0,"column":84},"action":"insert","lines":["u"]},{"start":{"row":0,"column":84},"end":{"row":0,"column":85},"action":"insert","lines":["n"]},{"start":{"row":0,"column":85},"end":{"row":0,"column":86},"action":"insert","lines":["i"]},{"start":{"row":0,"column":86},"end":{"row":0,"column":87},"action":"insert","lines":["q"]},{"start":{"row":0,"column":87},"end":{"row":0,"column":88},"action":"insert","lines":["u"]},{"start":{"row":0,"column":88},"end":{"row":0,"column":89},"action":"insert","lines":["e"]},{"start":{"row":0,"column":89},"end":{"row":0,"column":90},"action":"insert","lines":[")"]}],[{"start":{"row":0,"column":90},"end":{"row":0,"column":91},"action":"insert","lines":[" "],"id":93}],[{"start":{"row":0,"column":76},"end":{"row":0,"column":78},"action":"remove","lines":[", "],"id":94},{"start":{"row":0,"column":76},"end":{"row":0,"column":77},"action":"insert","lines":[" "]},{"start":{"row":0,"column":77},"end":{"row":0,"column":78},"action":"insert","lines":["-"]}],[{"start":{"row":0,"column":78},"end":{"row":0,"column":79},"action":"insert","lines":[" "],"id":95}],[{"start":{"row":19,"column":60},"end":{"row":19,"column":61},"action":"insert","lines":[" "],"id":96},{"start":{"row":19,"column":61},"end":{"row":19,"column":62},"action":"insert","lines":["#"]},{"start":{"row":19,"column":62},"end":{"row":19,"column":63},"action":"insert","lines":["N"]}],[{"start":{"row":19,"column":63},"end":{"row":19,"column":64},"action":"insert","lines":[" "],"id":97},{"start":{"row":19,"column":64},"end":{"row":19,"column":65},"action":"insert","lines":["="]}],[{"start":{"row":19,"column":65},"end":{"row":19,"column":66},"action":"insert","lines":[" "],"id":98}],[{"start":{"row":19,"column":65},"end":{"row":19,"column":66},"action":"remove","lines":[" "],"id":99},{"start":{"row":19,"column":64},"end":{"row":19,"column":65},"action":"remove","lines":["="]}],[{"start":{"row":19,"column":64},"end":{"row":19,"column":65},"action":"insert","lines":["i"],"id":100},{"start":{"row":19,"column":65},"end":{"row":19,"column":66},"action":"insert","lines":["s"]}],[{"start":{"row":19,"column":66},"end":{"row":19,"column":67},"action":"insert","lines":[" "],"id":101},{"start":{"row":19,"column":67},"end":{"row":19,"column":68},"action":"insert","lines":["n"]},{"start":{"row":19,"column":68},"end":{"row":19,"column":69},"action":"insert","lines":["u"]},{"start":{"row":19,"column":69},"end":{"row":19,"column":70},"action":"insert","lines":["m"]},{"start":{"row":19,"column":70},"end":{"row":19,"column":71},"action":"insert","lines":["b"]},{"start":{"row":19,"column":71},"end":{"row":19,"column":72},"action":"insert","lines":["e"]},{"start":{"row":19,"column":72},"end":{"row":19,"column":73},"action":"insert","lines":["r"]}],[{"start":{"row":20,"column":62},"end":{"row":20,"column":63},"action":"insert","lines":["#"],"id":102},{"start":{"row":20,"column":63},"end":{"row":20,"column":64},"action":"insert","lines":["S"]}],[{"start":{"row":20,"column":64},"end":{"row":20,"column":65},"action":"insert","lines":[" "],"id":103},{"start":{"row":20,"column":65},"end":{"row":20,"column":66},"action":"insert","lines":["S"]}],[{"start":{"row":20,"column":65},"end":{"row":20,"column":66},"action":"remove","lines":["S"],"id":104}],[{"start":{"row":20,"column":65},"end":{"row":20,"column":66},"action":"insert","lines":["i"],"id":105},{"start":{"row":20,"column":66},"end":{"row":20,"column":67},"action":"insert","lines":["s"]}],[{"start":{"row":20,"column":67},"end":{"row":20,"column":68},"action":"insert","lines":[" "],"id":106},{"start":{"row":20,"column":68},"end":{"row":20,"column":69},"action":"insert","lines":["S"]},{"start":{"row":20,"column":69},"end":{"row":20,"column":70},"action":"insert","lines":["t"]},{"start":{"row":20,"column":70},"end":{"row":20,"column":71},"action":"insert","lines":["r"]},{"start":{"row":20,"column":71},"end":{"row":20,"column":72},"action":"insert","lines":["i"]},{"start":{"row":20,"column":72},"end":{"row":20,"column":73},"action":"insert","lines":["n"]},{"start":{"row":20,"column":73},"end":{"row":20,"column":74},"action":"insert","lines":["g"]}],[{"start":{"row":19,"column":61},"end":{"row":19,"column":62},"action":"insert","lines":[" "],"id":107}],[{"start":{"row":20,"column":62},"end":{"row":20,"column":63},"action":"insert","lines":[" "],"id":108}],[{"start":{"row":19,"column":61},"end":{"row":19,"column":62},"action":"remove","lines":[" "],"id":109}],[{"start":{"row":19,"column":62},"end":{"row":19,"column":63},"action":"insert","lines":[" "],"id":110}],[{"start":{"row":20,"column":64},"end":{"row":20,"column":65},"action":"insert","lines":[" "],"id":111}],[{"start":{"row":0,"column":118},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":112},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["~"]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"remove","lines":["~"],"id":113}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["#"],"id":114}],[{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":[" "],"id":115},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["@"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["R"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["e"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["f"]}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":[":"],"id":116}],[{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":[" "],"id":117}],[{"start":{"row":1,"column":8},"end":{"row":1,"column":102},"action":"insert","lines":["https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.01.html"],"id":118}],[{"start":{"row":1,"column":102},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":119}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":[" "],"id":120}],[{"start":{"row":0,"column":36},"end":{"row":0,"column":38},"action":"remove","lines":[", "],"id":121},{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"insert","lines":["."]}],[{"start":{"row":0,"column":37},"end":{"row":0,"column":38},"action":"insert","lines":[" "],"id":122}],[{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"remove","lines":["o"],"id":123}],[{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"insert","lines":["O"],"id":124}]]},"ace":{"folds":[],"scrolltop":14,"scrollleft":0,"selection":{"start":{"row":6,"column":37},"end":{"row":6,"column":37},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":0,"state":"start","mode":"ace/mode/python"}},"timestamp":1639840385437,"hash":"d0034e4d6dffa97a9a36f24ad2d6065ecb310079"}