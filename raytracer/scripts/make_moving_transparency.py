

scene = """{
   "scene": {
             "type": "union",
             "children":
             [
                 {"type": "intersection",
                 "children": [
                  {
                   "type": "hyperboloidone",
                   "center": {"x": -0.8, "y": 7, "z": 0},
                   "material": {"ka": 0.5, "kd": 0.3, "ks": 0.2, "alpha": 3,"transparency": 0.9, "refractionIndex": 1.33, "color": {"r": 255, "b": 100}}
                  },
                  {"type": "sphere",
                   "radius": 4,
                   "height": 3,
                   "material": {"ka": 0.5, "kd": 0.3, "ks": 0.2, "alpha": 3, "transparency": 0.9, "refractionIndex": 1.33, "color": {"r": 255, "g": 100}}
                 }]},
                {"type": "sphere",
                   "radius": 2,
                   "center": {"x": %.2f, "y": 12},
                   "material": {"ka": 0.5, "kd": 0.3, "ks": 0.2, "alpha": 3, "reflectiveness": 0.2, "color": {"r": 255}}
                 } 
             ]
                 
            },
   "camera": {"x": 0, "y": -8, "z": 0},
   "view": {"x": 0, "y": 1, "z": 0},
   "background": {"gray": 128},
   "fov": 90,
   "reflections": 1,
   "lighting": {"type": "phong", "ambient": {"color": 128}, "shadows": true,
                "lights": [{"position": {"x": -50, "y": -700, "z": 30}, "color": {"r": 255, "g": 0, "b": 0}},
                           {"position": {"x": 50, "y": -700, "z": 30}, "color": {"r": 0, "g": 255, "b": 0}},
                           {"position": {"x": 0, "y": -700, "z": -60}, "color": {"r": 0, "g": 0, "b": 255}}]}
}"""


for i in range(100):
   f = open("scene%03d.json"%(i), "w")
   dx = i*1.0/10 - 5.0
   f.write(scene%(dx))
   f.close()