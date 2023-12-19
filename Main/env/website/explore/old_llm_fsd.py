import openai
import json

openai.api_key = "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"

function_descriptions = [
    {
        "name": "courses",
        "description": "Gives the transalational(metres) movements and angular(radians) rotations in x,y and z axis.",
        "parameters": {
            "type": "object",
            "properties": {
                "AI": {
                    "type": "object",
                    "properties": {
                        "value":{
                            "type": "string",
                            "description": "Given a set of questions and their respective binary responses (1 for yes and 0 for no), interpret the answers and recommend a suitable course. and focus on additional intrest toward coding and mathematic along with thign related to artificla intelligence"
                        },

                    }
                },
                "CSE": {
                    "type": "object",
                    "properties": {
                        "value":{
                            "type": "string",
                            "description": "Given a set of questions and their respective binary responses (1 for yes and 0 for no), interpret the answers and recommend a suitable course. and focus on intreset towards coding mathematics along woht low level coding and things related to computer"
                        },

                    }
                },
                "EEE":{
                    "type": "object",
                    "properties": {
                        "value":{
                            "type": "string",
                            "description": "Given a set of questions and their respective binary responses (1 for yes and 0 for no), interpret the answers and recommend a suitable course. and focus on low level coding along with hardware coding and related to circuits"
                        },

                    }
                },
                "ECE":{
                    "type": "object",
                    "properties": {
                        "value":{
                            "type": "string",
                            "description": "Given a set of questions and their respective binary responses (1 for yes and 0 for no), interpret the answers and recommend a suitable course. and focus on intrest in low level coding and coomunication technologies"
                        },

                    }
                },
                "ME": {
                    "type": "object",
                    "properties": {
                        "value":{
                            "type": "string",
                            "description": "Given a set of questions and their respective binary responses (1 for yes and 0 for no), interpret the answers and recommend a suitable course. and focus on intreset in material sciences, machine design and manufaturing"
                        },

                    }
                },
                "Civil": {
                    "type": "object",
                    "properties": {
                        "value":{
                            "type": "string",
                            "description": "Given a set of questions and their respective binary responses (1 for yes and 0 for no), interpret the answers and recommend a suitable course. and focus on intrest towatd materials sciences and urban planning and development"
                        },

                    }
                },
            }
        }
    },
]

import json
def ask_function_calling(query):
    messages = [{'role': 'user', 'content': 'Do you like software coding? 1, Do you like probability and statistics? 0, Do you like hardware programming? 0, Do you like circuits and its design? 0, Do you like communications technologies? 0, Do you like material sciences? 0, Do you like manufacturing? 0, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 1, Do you prefer working on software development over hardware? 1, Would you like to explore the field of artificial intelligence and machine learning? 1, Are you interested in signal processing and VLSI systems? 0, Do you like experimenting with IoT devices? 1, Are you interested in geotechnical engineering and soil mechanics? 0, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 0, Would you prefer to work on projects related to web development and cybersecurity? 1'},
                    {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"CSE":"B.Tech Computer Science Engineering"},indent=2,ensure_ascii=False,)}},
                    {'role': 'user', 'content':'Do you like software coding? 1, Do you like probability and statistics? 0, Do you like hardware programming? 1, Do you like circuits and its design? 0, Do you like communications technologies? 1, Do you like material sciences? 0, Do you like manufacturing? 0, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 0, Do you prefer working on software development over hardware? 0, Would you like to explore the field of artificial intelligence and machine learning? 1, Are you interested in signal processing and VLSI systems? 1, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 0, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 0, Would you prefer to work on projects related to web development and cybersecurity? 0'},
                    {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"ECE":"BTech Electronics and Communication Engineering"},indent=2,ensure_ascii=False,)}},
                    {'role': 'user', 'content': 'Do you like software coding? 0, Do you like probability and statistics? 0, Do you like hardware programming? 1, Do you like circuits and its design? 1, Do you like communications technologies? 0, Do you like material sciences? 0, Do you like manufacturing? 0, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 0, Do you prefer working on software development over hardware? 0, Would you like to explore the field of artificial intelligence and machine learning? 0, Are you interested in signal processing and VLSI systems? 0, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 0, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 1, Would you prefer to work on projects related to web development and cybersecurity? 0'},
                    {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"EEE":"B.Tech Electrical and Electronic Engineering."},indent=2,ensure_ascii=False,)}},
                    {'role': 'user', 'content': "Do you like software coding? 1, Do you like probability and statistics? 1, Do you like hardware programming? 0, Do you like circuits and its design? 0, Do you like communications technologies? 0, Do you like material sciences? 0, Do you like manufacturing? 0, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 1, Do you prefer working on software development over hardware? 1, Would you like to explore the field of artificial intelligence and machine learning? 1, Are you interested in signal processing and VLSI systems? 0, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 0, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 0, Would you prefer to work on projects related to web development and cybersecurity? 0"},
                    {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"AI":"B.Tech Artificial Intelligence"},indent=2,ensure_ascii=False,)}},
                    {'role': 'user', 'content': "Do you like software coding? 0, Do you like probability and statistics? 0, Do you like hardware programming? 0, Do you like circuits and its design? 0, Do you like communications technologies? 0, Do you like material sciences? 1, Do you like manufacturing? 1, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 0, Do you prefer working on software development over hardware? 0, Would you like to explore the field of artificial intelligence and machine learning? 1, Are you interested in signal processing and VLSI systems? 0, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 1, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 0, Would you prefer to work on projects related to web development and cybersecurity? 0"},
                    {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"ME":"B.Tech Mechanical Engineering"},indent=2,ensure_ascii=False,)}},
                    {'role': 'user', 'content': 'Do you like software coding? 0, Do you like probability and statistics? 0, Do you like hardware programming? 0, Do you like circuits and its design? 0, Do you like communications technologies? 0, Do you like material sciences? 1, Do you like manufacturing? 0, Do you like urban planning and development? 1, Do you enjoy studying algorithms and data structures? 0, Do you prefer working on software development over hardware? 0, Would you like to explore the field of artificial intelligence and machine learning? 0, Are you interested in signal processing and VLSI systems? 0, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 1, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 0, Would you prefer to work on projects related to web development and cybersecurity? 0'},
                    {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"Civil":"B.Tech Civil Engineering"},indent=2,ensure_ascii=False,)}},

                    {'role': 'user', 'content': 'Do you like software coding? 0, Do you like probability and statistics? 1, Do you like hardware programming? 0, Do you like circuits and its design? 0, Do you like communications technologies? 0, Do you like material sciences? 0, Do you like manufacturing? 0, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 0, Do you prefer working on software development over hardware? 0, Would you like to explore the field of artificial intelligence and machine learning? 1, Are you interested in signal processing and VLSI systems? 0, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 0, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 0, Would you prefer to work on projects related to web development and cybersecurity? 0'},
                    {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"ECE":"BTech Electronics and Communication Engineering"},indent=2,ensure_ascii=False,)}},
                    {'role': 'user', 'content': 'Do you like software coding? 0, Do you like probability and statistics? 0, Do you like hardware programming? 0, Do you like circuits and its design? 0, Do you like communications technologies? 0, Do you like material sciences? 0, Do you like manufacturing? 0, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 0, Do you prefer working on software development over hardware? 0, Would you like to explore the field of artificial intelligence and machine learning? 0, Are you interested in signal processing and VLSI systems? 0, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 1, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 0, Would you prefer to work on projects related to web development and cybersecurity? 0'},
                    {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"EEE":"B.Tech Electrical and Electronic Engineering."},indent=2,ensure_ascii=False,)}},

                    {'role': 'user', 'content': 'Do you like software coding? 0, Do you like probability and statistics? 1, Do you like hardware programming? 0, Do you like circuits and its design? 0, Do you like communications technologies? 0, Do you like material sciences? 0, Do you like manufacturing? 0, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 1, Do you prefer working on software development over hardware? 1, Would you like to explore the field of artificial intelligence and machine learning? 1, Are you interested in signal processing and VLSI systems? 0, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 0, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 0, Would you prefer to work on projects related to web development and cybersecurity? 0'},
                    {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"AI":"B.Tech Artificial Intelligence"},indent=2,ensure_ascii=False,)}},
                    {'role': 'user', 'content': 'Do you like software coding? 0, Do you like probability and statistics? 0, Do you like hardware programming? 0, Do you like circuits and its design? 0, Do you like communications technologies? 0, Do you like material sciences? 0, Do you like manufacturing? 0, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 0, Do you prefer working on software development over hardware? 0, Would you like to explore the field of artificial intelligence and machine learning? 0, Are you interested in signal processing and VLSI systems? 0, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 1, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 0, Would you prefer to work on projects related to web development and cybersecurity? 0'},
                    {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"ME":"B.Tech Mechanical Engineering"},indent=2,ensure_ascii=False,)}},
                    {'role': 'user', 'content':'Do you like software coding? 0, Do you like probability and statistics? 0, Do you like hardware programming? 0, Do you like circuits and its design? 0, Do you like communications technologies? 1, Do you like material sciences? 0, Do you like manufacturing? 0, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 1, Do you prefer working on software development over hardware? 1, Would you like to explore the field of artificial intelligence and machine learning? 1, Are you interested in signal processing and VLSI systems? 0, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 0, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 0, Would you prefer to work on projects related to web development and cybersecurity? 0'},
                    {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"AI":"B.Tech Artificial Intelligence"},indent=2,ensure_ascii=False,)}},

                    {'role': 'user', 'content': 'Do you like software coding? 1, Do you like probability and statistics? 1, Do you like hardware programming? 0, Do you like circuits and its design? 0, Do you like communications technologies? 0, Do you like material sciences? 0, Do you like manufacturing? 0, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 1, Do you prefer working on software development over hardware? 1, Would you like to explore the field of artificial intelligence and machine learning? 1, Are you interested in signal processing and VLSI systems? 0, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 0, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 0, Would you prefer to work on projects related to web development and cybersecurity? 0'},
                    {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"AI":"B.Tech Artificial Intelligence"},indent=2,ensure_ascii=False,)}},
                    {'role': 'user', 'content': 'Do you like software coding? 0, Do you like probability and statistics? 0, Do you like hardware programming? 1, Do you like circuits and its design? 0, Do you like communications technologies? 1, Do you like material sciences? 0, Do you like manufacturing? 0, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 0, Do you prefer working on software development over hardware? 0, Would you like to explore the field of artificial intelligence and machine learning? 1, Are you interested in signal processing and VLSI systems? 1, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 0, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 0, Would you prefer to work on projects related to web development and cybersecurity? 0'},
                    {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"ECE":"BTech Electronics and Communication Engineering"},indent=2,ensure_ascii=False,)}},
                    {'role': 'user', 'content':'Do you like software coding? 1, Do you like probability and statistics? 0, Do you like hardware programming? 1, Do you like circuits and its design? 0, Do you like communications technologies? 0, Do you like material sciences? 0, Do you like manufacturing? 0, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 1, Do you prefer working on software development over hardware? 0, Would you like to explore the field of artificial intelligence and machine learning? 1, Are you interested in signal processing and VLSI systems? 1, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 0, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 0, Would you prefer to work on projects related to web development and cybersecurity? 0'},
                    {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"ECE":"BTech Electronics and Communication Engineering"},indent=2,ensure_ascii=False,)}},


                    {'role': 'user', 'content': 'Do you like software coding? 1, Do you like probability and statistics? 0, Do you like hardware programming? 1, Do you like circuits and its design? 0, Do you like communications technologies? 0, Do you like material sciences? 0, Do you like manufacturing? 0, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 1, Do you prefer working on software development over hardware? 0, Would you like to explore the field of artificial intelligence and machine learning? 0, Are you interested in signal processing and VLSI systems? 1, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 0, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 1, Would you prefer to work on projects related to web development and cybersecurity? 0'},
                    {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"CSE":"B.Tech Computer Science Engineering"},indent=2,ensure_ascii=False,)}},
                    {'role': 'user', 'content': 'Do you like software coding? 1, Do you like probability and statistics? 0, Do you like hardware programming? 0, Do you like circuits and its design? 0, Do you like communications technologies? 0, Do you like material sciences? 0, Do you like manufacturing? 0, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 1, Do you prefer working on software development over hardware? 0, Would you like to explore the field of artificial intelligence and machine learning? 0, Are you interested in signal processing and VLSI systems? 0, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 0, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 1, Would you prefer to work on projects related to web development and cybersecurity? 0'},
                    {'role': 'assistant', 'content': None,'function_call':{"name": function_descriptions[0]["name"], "arguments": json.dumps({"CSE":"B.Tech Computer Science Engineering"},indent=2,ensure_ascii=False,)}},

                    {'role': 'user', 'content': query}]



                    #{'role': 'user', 'content': 'Do you like software coding? 0, Do you like probability and statistics? 0, Do you like hardware programming? 1, Do you like circuits and its design? 0, Do you like communications technologies? 1, Do you like material sciences? 0, Do you like manufacturing? 0, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 0, Do you prefer working on software development over hardware? 0, Would you like to explore the field of artificial intelligence and machine learning? 0, Are you interested in signal processing and VLSI systems? 1, Do you like experimenting with IoT devices? 1, Are you interested in geotechnical engineering and soil mechanics? 0, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 0, Would you prefer to work on projects related to web development and cybersecurity? 0'}]

                    #{'role': 'user', 'content': 'Do you like software coding? 0, Do you like probability and statistics? 0, Do you like hardware programming? 0, Do you like circuits and its design? 0, Do you like communications technologies? 0, Do you like material sciences? 1, Do you like manufacturing? 0, Do you like urban planning and development? 1, Do you enjoy studying algorithms and data structures? 0, Do you prefer working on software development over hardware? 1, Would you like to explore the field of artificial intelligence and machine learning? 0, Are you interested in signal processing and VLSI systems? 0, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 0, Do you enjoy working on mechanical design and CAD? 1, Do you want to explore the realm of power system and transmission? 0, Would you prefer to work on projects related to web development and cybersecurity? 0,'}]
                # {'role': 'user', 'content': 'Do you like software coding? 1, Do you like probability and statistics? 1, Do you like hardware programming? 0, Do you like circuits and its design? 0, Do you like communications technologies? 0, Do you like material sciences? 0, Do you like manufacturing? 0, Do you like urban planning and development? 0, Do you enjoy studying algorithms and data structures? 0, Do you prefer working on software development over hardware? 0, Would you like to explore the field of artificial intelligence and machine learning? 1, Are you interested in signal processing and VLSI systems? 0, Do you like experimenting with IoT devices? 0, Are you interested in geotechnical engineering and soil mechanics? 0, Do you enjoy working on mechanical design and CAD? 0, Do you want to explore the realm of power system and transmission? 0, Would you prefer to work on projects related to web development and cybersecurity? 0'}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=function_descriptions,
        function_call="auto", # this forces calling `function`
    )
    response_message = json.loads((response["choices"][0]["message"]['function_call']['arguments']))
    return ' '.join(response_message.values())

