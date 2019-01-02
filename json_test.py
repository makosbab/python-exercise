import json

szornyekJSON = '''
    {
      "nev": "Aboleth",
      "meret": "Óriási",
      "tipus": "Rendellenesség",
      "tipus_modosito": "Vízi",
      "tulajdonsagok": 
      [
        {
          "nev" : "Erő",
          "pont" : 26
        },
        {
          "nev" : "Ügy",
          "pont" : 12
        },
        {
          "nev" : "Áll",
          "pont" : 20
        },
        {
          "nev" : "Int",
          "pont" : 15
        },
        {
          "nev" : "Böl",
          "pont" : 17
        },
        {
          "nev" : "Kar",
          "pont" : 17
        }
      ],
      "jartassagok": 
      [
          {
              "nev" : "Koncentráció",
              "pont" : 16
          }
      ],
      "eletero_dobas": 
      {
          "dobas" : "8d8+40",
          "eletpont ": 76
      },
      "kezdemenyezes": 
      {
          "modosito" : 1,
          "eredet": "Ügy"
      },
      "vf": 
      {
          "ertek": 16,
          "modositok" : 
          [
            [-2, "termet"], [1, "Ügy"],  [7, "természetes"]
          ]
      },
      "mentok": [
        {
          "nev": "Szív",
          "ertek" : 7
        },
        {
          "nev": "Gyors",
          "ertek" : 3
        },
        {
          "nev": "Akarat",
          "ertek" : 11
        }
      ],
      "kihivasi_ertek": 7,
      "tamadasok": 
      {
        "szam": 4,
        "nev": "Csáp",
        "bonusz" : 12,
        "forma" : "kh."
        
      },
      "sebzes": 
      {
          "nev" : "Csáp",
          "dobas" : "1d6+9",
          "hatas" : "Átalakítás"
      },
      "oldal_eleres": 
      {
          "szelesseg" : 10,
          "hosszusag" : 20,
          "tavolsag" : 10
      },
      "kulonleges_tamadasok": ["Átalakítás", "pszionika", "rabszolgaság"],
      "kulonleges_kepessegek": 
      [
          "Nyálkafelhő"   
      ],
      "sebesseg": "10 láb, úszva 60 láb",
      "kepessegek": 
      [
        "Éberség", "Harci Alkalmazások", "Vasakarat"        
      ],
      "fejlesztes": 
      [
          {
              "min": 9,
              "max": 16,
              "meret": "Óriási"
          },
          {
            "min": 17,
            "max": 24,
            "meret": "Hatalmas"
          } 
      ]
    }
'''

y = json.loads(szornyekJSON)
print(y["fejlesztes"])