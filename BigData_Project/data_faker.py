import random
from datetime import datetime


class DataFaker:
    # Function to generate random customer data
    @staticmethod
    def generate_random_data():
        Crime = random.choice([True, False])
        return {
        "CrimeType": random.choice(["Theft", "Assault", "Burglary", "Vandalism", "Robbery","Theft", "Assault", "Burglary", "Vandalism", "Robbery","Theft",
                                    "Assault", "Burglary", "Vandalism", "Robbery","Theft", "Assault", "Burglary",
                                    "Vandalism", "Robbery","Theft", "Assault", "Burglary", "Vandalism", "Robbery","Theft", "Assault", "Burglary",
                                    "Vandalism", "Robbery","Theft", "Assault", "Burglary", "Vandalism", "Robbery","Theft", "Assault", "Burglary",
                                    "Vandalism", "Robbery","Theft", "Assault", "Burglary", "Vandalism", "Robbery","Theft", "Assault", "Burglary", 
                                    "Vandalism", "Robbery","Theft", "Assault", "Burglary", "Vandalism", "Robbery"]),
        
        
        "Location": random.choice(["CityA", "CityB", "CityC","CityD", "CityE", "CityF",
                                   "CityA", "CityB", "CityC","CityD", "CityE", "CityF",
                                   "CityA", "CityB", "CityC","CityD", "CityE", "CityF",
                                   "CityA", "CityB", "CityC","CityD", "CityE", "CityF",
                                   "CityA", "CityB", "CityC","CityD", "CityE", "CityF",
                                   "CityA", "CityB", "CityC","CityD", "CityE", "CityF"]),
        
        
        "Date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "Time": str(random.randint(0, 23)) + ":" + str(random.randint(0, 59)),
        "ArrestedParty": {
            "Name" : random.choice(["Zalta", "3bdoMota","Haland","John","Peso",
                                    "Zalta", "3bdoMota","Haland","John","Peso",
                                    "Zalta", "3bdoMota","Haland","John","Peso",
                                    "Zalta", "3bdoMota","Haland","John","Peso",
                                    "Zalta", "3bdoMota","Haland","John","Peso",
                                    "Zalta", "3bdoMota","Haland","John","Peso",
                                    "Zalta", "3bdoMota","Haland","John","Peso"]),
            
            
            
            
            "Age": random.randint(18, 60),
            "Gender": random.choice(["Male", "Female"]),
            "Address": random.choice(["123 Main St, CityA", "123 Haram St, CityB", "123 Helwan St, CityC", "123 Matarya St, CityD", "123 Marg St, CityE", "123 Embaba St, CityF",
                                      "123 Main St, CityA", "123 Haram St, CityB", "123 Helwan St, CityC", "123 Matarya St, CityD", "123 Marg St, CityE", "123 Embaba St, CityF",
                                      "123 Main St, CityA", "123 Haram St, CityB", "123 Helwan St, CityC", "123 Matarya St, CityD", "123 Marg St, CityE", "123 Embaba St, CityF",
                                      "123 Main St, CityA", "123 Haram St, CityB", "123 Helwan St, CityC", "123 Matarya St, CityD", "123 Marg St, CityE", "123 Embaba St, CityF",
                                      "123 Main St, CityA", "123 Haram St, CityB", "123 Helwan St, CityC", "123 Matarya St, CityD", "123 Marg St, CityE", "123 Embaba St, CityF",
                                      "123 Main St, CityA", "123 Haram St, CityB", "123 Helwan St, CityC", "123 Matarya St, CityD", "123 Marg St, CityE", "123 Embaba St, CityF",
                                      "123 Main St, CityA", "123 Haram St, CityB", "123 Helwan St, CityC", "123 Matarya St, CityD", "123 Marg St, CityE", "123 Embaba St, CityF",
                                      "123 Main St, CityA", "123 Haram St, CityB", "123 Helwan St, CityC", "123 Matarya St, CityD", "123 Marg St, CityE", "123 Embaba St, CityF",
                                      ]),
            
            
            "Charges": random.choice(["robbery", "assault", "burglary", "fraud", "vandalism", "drug offense",
                                      "robbery", "assault", "burglary", "fraud", "vandalism", "drug offense","robbery", "assault", "burglary", "fraud", "vandalism", "drug offense"
                                      ,"robbery", "assault", "burglary", "fraud", "vandalism", "drug offense"
                                      ,"robbery", "assault", "burglary", "fraud", "vandalism", "drug offense"
                                      ,"robbery", "assault", "burglary", "fraud", "vandalism", "drug offense",
                                      "robbery", "assault", "burglary", "fraud", "vandalism", "drug offense",
                                      "robbery", "assault", "burglary", "fraud", "vandalism", "drug offense",
                                      "robbery", "assault", "burglary", "fraud", "vandalism", "drug offense"]),
            
            
    
            "ArrestLocation": random.choice(["CityA", "CityB", "CityC","CityD", "CityE", "CityF",
                                             "CityA", "CityB", "CityC","CityD", "CityE", "CityF",
                                             "CityA", "CityB", "CityC","CityD", "CityE", "CityF",
                                             "CityA", "CityB", "CityC","CityD", "CityE", "CityF",
                                             "CityA", "CityB", "CityC","CityD", "CityE", "CityF",
                                             "CityA", "CityB", "CityC","CityD", "CityE", "CityF",
                                             "CityA", "CityB", "CityC","CityD", "CityE", "CityF",
                                             "CityA", "CityB", "CityC","CityD", "CityE", "CityF"])
        },
        "VictimInfo": {
            "VictimName" : random.choice(["Yosof", "Ali","AbdallaElshamy","Omar","Hiqa",
                                          "Yosof", "Ali","AbdallaElshamy","Omar","Hiqa",
                                          "Yosof", "Ali","AbdallaElshamy","Omar","Hiqa",
                                          "Yosof", "Ali","AbdallaElshamy","Omar","Hiqa",
                                          "Yosof", "Ali","AbdallaElshamy","Omar","Hiqa",
                                          "Yosof", "Ali","AbdallaElshamy","Omar","Hiqa",
                                          "Yosof", "Ali","AbdallaElshamy","Omar","Hiqa",
                                          "Yosof", "Ali","AbdallaElshamy","Omar","Hiqa",
                                          "Yosof", "Ali","AbdallaElshamy","Omar","Hiqa",
                                          "Yosof", "Ali","AbdallaElshamy","Omar","Hiqa",
                                          "Yosof", "Ali","AbdallaElshamy","Omar","Hiqa"]),
            
            
            
            
            "VictimAge": random.randint(18, 60),
            "VictimGender": random.choice(["Male", "Female"]),
            "VictimAddress":  random.choice(["123 Main St, CityA", "123 Haram St, CityB", "123 Helwan St, CityC", "123 Matarya St, CityD", "123 Marg St, CityE", "123 Embaba St, CityF",
                                      "123 Main St, CityA", "123 Haram St, CityB", "123 Helwan St, CityC", "123 Matarya St, CityD", "123 Marg St, CityE", "123 Embaba St, CityF",
                                      "123 Main St, CityA", "123 Haram St, CityB", "123 Helwan St, CityC", "123 Matarya St, CityD", "123 Marg St, CityE", "123 Embaba St, CityF",
                                      "123 Main St, CityA", "123 Haram St, CityB", "123 Helwan St, CityC", "123 Matarya St, CityD", "123 Marg St, CityE", "123 Embaba St, CityF",
                                      "123 Main St, CityA", "123 Haram St, CityB", "123 Helwan St, CityC", "123 Matarya St, CityD", "123 Marg St, CityE", "123 Embaba St, CityF",
                                      "123 Main St, CityA", "123 Haram St, CityB", "123 Helwan St, CityC", "123 Matarya St, CityD", "123 Marg St, CityE", "123 Embaba St, CityF",
                                      "123 Main St, CityA", "123 Haram St, CityB", "123 Helwan St, CityC", "123 Matarya St, CityD", "123 Marg St, CityE", "123 Embaba St, CityF",
                                      "123 Main St, CityA", "123 Haram St, CityB", "123 Helwan St, CityC", "123 Matarya St, CityD", "123 Marg St, CityE", "123 Embaba St, CityF",
                                      ]),
            "InjuryType": random.choice(["Physical", "Emotional"]),
            "ImpactOnVictim": random.choice(["Minor", "Moderate", "Severe","Minor", "Moderate", "Severe",
                                             "Minor", "Moderate", "Severe","Minor", "Moderate", "Severe",
                                             "Minor", "Moderate", "Severe","Minor", "Moderate", "Severe"
                                             ,"Minor", "Moderate", "Severe","Minor", "Moderate", "Severe",
                                             "Minor", "Moderate", "Severe","Minor", "Moderate", "Severe",
                                             "Minor", "Moderate", "Severe","Minor", "Moderate", "Severe"])
        },
        "OtherFactors": {
            "WeatherConditions": random.choice(["Clear", "Rainy", "Snowy","Clear", "Rainy", "Snowy"
                                                "Clear", "Rainy", "Snowy","Clear", "Rainy", "Snowy"
                                                "Clear", "Rainy", "Snowy","Clear", "Rainy", "Snowy"
                                                ,"Clear", "Rainy", "Snowy","Clear", "Rainy", "Snowy",
                                                "Clear", "Rainy", "Snowy","Clear", "Rainy", "Snowy",
                                                ]),
            
            
            "Witnesses": random.choice([True, False]),
            "EvidenceCollected": random.choice([True, False]),
            "PoliceResponseTime": round(random.uniform(5.0, 30.0), 2)
        }
    }



        
        
        
        
        
        
        
        
    