
Do Taller Trees Mean Higher Prices?
explore whether properties on streets with taller trees are more valuable than those on streets with shorter ones. Using Python for analysis and a simple React app to present your findings, you'll showcase your skills in data analysis, machine learning, and front-end development.
Objective
Analyze property values based on tree heights and present your findings in a React app.
Datasets
You’ll be working with two files:
city-trees.json: Contains street names categorized as either short or tall, based on median tree height.
property-data.csv: Contains property sales data, including street names and sale prices in euros.
Task Outline
Data Analysis and Processing
Load and analyze both datasets in Python to explore the relationship between tree height categories and property prices.
Identify any trends or insights regarding property values based on tree height categories.
Machine Learning and Analysis
Feature Engineering: Based on the datasets provided, consider and create any relevant features that could improve the model’s accuracy. Explain your choices and any assumptions made.
Model Selection: Choose a machine learning model appropriate for predicting or classifying the impact of tree height categories on property prices. Justify why you selected this model and discuss any alternatives you considered.
Evaluation: Assess your model’s performance using appropriate metrics. Explain your choice of metrics and any specific results. If the model is not performing as expected, note potential improvements or refinements.
Interpretation: Provide a brief analysis of the model’s predictions, explaining any notable patterns or insights found in property values relative to tree height. Consider visualizations or summary statistics to back up your findings.
Documentation & Presentation
Prepare a README or Jupyter notebook that explains your approach, analysis, and findings.
Separate your code and documentation so that the presentation effectively demonstrates your programming capabilities.
React Application
Create a basic React app using TypeScript to display your findings.
Design a simple UI to present key insights, ensuring the app is well-organized and showcases reusable components.
Stretch Goals (Optional)
Try creating a simple API to serve predictions from your model (run locally with a tool like docker/docker compose)
Enhance the React app with interactive charts or graphs to make the data more engaging.

trees-data.json{
       "tall": {
        "road": {
            "adelaide": {
                "adelaide road": 25
            },
            "beaumont": {
                "beaumont road": 20
            },
            "cabra": {
                "cabra road": 25
            },
            "cambridge": {
                "cambridge road": 20
            },
            "carnlough": {
                "carnlough road": 20
            },
            "clare": {
                "clare road": 25
            },
            "clogher": {
                "clogher road": 20
            },
            "clyde": {
                "clyde road": 20
            },
            "donnybrook": {
                "donnybrook road": 20
            },
            "drumcondra": {
                "drumcondra road": 25
            },
            "glenarriff": {
                "glenarriff road": 20
            },
            "glenbrook": {
                "glenbrook road": 20
            },
            "glendhu": {
                "glendhu road": 20
            },
            "haddington": {
                "haddington road": 25
            },
            "inchicore": {
                "inchicore road": 20
            },
            "infirmary": {
                "infirmary road": 25
            },
            "infirmery": {
                "infirmery road": 20
            },
            "iona": {
                "iona road": 20
            },
            "circular": {
                "north": {
                    "north circular road": 25
                },
                "south": {
                    "south circular road": 20
                }
            },
            "orchard": {
                "orchard road": 25
            }
        },
        "green": {
            "beresford": {
                "beresford green": 20
            },
            "colege": {
                "colege green": 20
            },
            "college": {
                "college green": 20
            },
            "fairways": {
                "fairways green": 25
            }
        },
        "street": {
            "alley": {
                "bull": {
                    "bull alley street": 20
                }
            },
            "cuffe": {
                "cuffe street": 20
            },}}}
    "short": {
        "drive": {
            "abbey": {
                "abbey drive": 0
            },
            "coolrua": {
                "coolrua drive": 10
            },
            "coultry": {
                "coultry drive": 5
            },
            "drumcliffe": {
                "drumcliffe drive": 0
            },
            "park": {
                "grove": {
                    "grove park drive": 10
                }
            },
            "mcauley": {
                "mcauley drive": 10
            },
            "merlyn": {
                "merlyn drive": 5
            },
            "merylin": {
                "merylin drive": 5
            },
            "rathvale": {
                "rathvale drive": 10
            },
            "rathvilly": {
                "rathvilly drive": 10
            },
            "marys": {
                "st": {
                    "st marys drive": 10
                }
            },
            "mobhi": {
                "st": {
                    "st mobhi drive": 10
                }
            },
            "brendens": {
                "st": {
                    "st brendens drive": 0
                }
            },
            "thornville": {
                "thornville drive": 10
            }
        },
        "college": {
            "albert": {
                "albert college": 0
            }
        },
        "road": {
            "byrne": {
                "alfie": {
                    "alfie byrne road": 5
                }
            },
            "saints": {
                "all": {
                    "all saints road": 10
                }
            },

property-data.csv
Date of Sale (dd/mm/yyyy)	Address	Street Name	Price
01/01/2015	APT 274, THE PARKLANDS, NORTHWOOD	the park	€ 79,500.00
05/01/2015	61 CHARLEMONT, GRIFFITH AVE, DUBLIN 9	charlemont	€ 557,000.00
06/01/2015	6A Church Street, Finglas, Dublin 11	church street	€ 160,000.00
06/01/2015	APARTMENT 13 MOUNTGORRY WOOD, MALAHIDE ROAD, SWORDS	malahide road	€ 140,000.00
07/01/2015	15 THE TANNERY, 50 CORK ST, DUBLIN 8	cork street	€ 200,000.00
07/01/2015	53 RINGSEND RD, RINGSEND, DUBLIN 4	ringsend road	€ 6,000.00
07/01/2015	66 BUSHY PARK RD, TERENURE, DUBLIN 6	bushy park	€ 950,000.00
07/01/2015	APT 1, 82 SOUTH CIRCULAR RD, DUBLIN 8	south circular road	€ 147,000.00
09/01/2015	2 GREENVIEW SEABROOK MANOR, STATION RD, PORTMARNOCK	manor street	€ 245,000.00
09/01/2015	263 Orwell Park Glade, Templeogue	orwell park	€ 470,000.00
09/01/2015	33 MCGOVERNS CORNER, CORK ST, DUBLIN 8	cork street	€ 150,000.00
09/01/2015	43 Lower Buckingham Street, Dublin 1	buckingham street	€ 185,000.00