import requests
import random
from flask import Flask, render_template

app = Flask(__name__)


ip = requests.get('https://api.ipify.org').text
api_key = "at_pBkfrZykUUjsyiQvojb8PMutW10gV"


def states():
    all_states = {}
    California = {
        "What is the capital city of Alabama?": {
            "options": ["A) Birmingham", "B) Huntsville", "C) Montgomery", "D) Mobile"],
            "answer": "C) Montgomery"
        },
        "Which river forms the western boundary of Alabama?": {
            "options": ["A) Tennessee River", "B) Mississippi River", "C) Chattahoochee River", "D) Alabama River"],
            "answer": "B) Mississippi River"
        },
        "What is the nickname of Alabama?": {
            "options": ["A) The Sunshine State", "B) The Heart of Dixie", "C) The Yellowhammer State",
                        "D) The Magnolia State"],
            "answer": "C) The Yellowhammer State"
        },
        "Who was the first female African-American astronaut from Alabama?": {
            "options": ["A) Sally Ride", "B) Mae Jemison", "C) Guion Bluford", "D) Ellen Ochoa"],
            "answer": "B) Mae Jemison"
        },
        "Which university is located in Tuscaloosa, Alabama, and is known for its football team?": {
            "options": ["A) Auburn University", "B) University of Alabama", "C) Alabama State University",
                        "D) Troy University"],
            "answer": "B) University of Alabama"
        },
        "Which city in Alabama was the first capital of the Confederate States of America?": {
            "options": ["A) Birmingham", "B) Huntsville", "C) Montgomery", "D) Mobile"],
            "answer": "C) Montgomery"
        },
        "What is the official state bird of Alabama?": {
            "options": ["A) Robin", "B) Eagle", "C) Yellowhammer", "D) Cardinal"],
            "answer": "C) Yellowhammer"
        },
        "Which famous civil rights activist was born in Tuskegee, Alabama, and founded the Tuskegee Institute?": {
            "options": ["A) Martin Luther King Jr.", "B) Rosa Parks", "C) Malcolm X", "D) Booker T. Washington"],
            "answer": "D) Booker T. Washington"
        },
        "What is the highest point in Alabama?": {
            "options": ["A) Cheaha Mountain", "B) Lookout Mountain", "C) Mount Baldy", "D) Red Mountain"],
            "answer": "A) Cheaha Mountain"
        },
        "Which Alabama city was the site of the Montgomery Bus Boycott in 1955?": {
            "options": ["A) Birmingham", "B) Montgomery", "C) Selma", "D) Mobile"],
            "answer": "B) Montgomery"
        }
    }
    Alaska = {
        "What is the capital city of Alaska?": {
            "options": ["A) Anchorage", "B) Fairbanks", "C) Juneau", "D) Sitka"],
            "answer": "C) Juneau"
        },
        "Which U.S. state is the largest in terms of area?": {
            "options": ["A) Texas", "B) California", "C) Alaska", "D) Florida"],
            "answer": "C) Alaska"
        },
        "What is the highest peak in North America, located in Alaska?": {
            "options": ["A) Mount Everest", "B) Mount Kilimanjaro", "C) Denali", "D) Mount Rainier"],
            "answer": "C) Denali"
        },
        "Which Alaskan city is known as the 'gateway to Denali National Park'?": {
            "options": ["A) Anchorage", "B) Fairbanks", "C) Juneau", "D) Talkeetna"],
            "answer": "D) Talkeetna"
        },
        "What is the name of the indigenous people of Alaska?": {
            "options": ["A) Inuit", "B) Apache", "C) Sioux", "D) Cherokee"],
            "answer": "A) Inuit"
        },
        "Which month does the Iditarod Trail Sled Dog Race typically start in Alaska?": {
            "options": ["A) January", "B) February", "C) March", "D) April"],
            "answer": "B) February"
        },
        "What is the state flower of Alaska?": {
            "options": ["A) Forget-me-not", "B) Rose", "C) Lily", "D) Daisy"],
            "answer": "A) Forget-me-not"
        },
        "Which Alaskan city is the northernmost in the United States?": {
            "options": ["A) Barrow", "B) Anchorage", "C) Juneau", "D) Fairbanks"],
            "answer": "A) Barrow"
        },
        "What is the official state nickname of Alaska?": {
            "options": ["A) The Last Frontier", "B) The Golden State", "C) The Equality State", "D) The Beehive State"],
            "answer": "A) The Last Frontier"
        },
        "Which U.S. president famously purchased Alaska from Russia in 1867?": {
            "options": ["A) Abraham Lincoln", "B) Thomas Jefferson", "C) Andrew Johnson", "D) William Seward"],
            "answer": "D) William Seward"
        }
    }
    Washington = {
        "What is the capital city of Washington?": {
            "options": ["A) Seattle", "B) Spokane", "C) Olympia", "D) Tacoma"],
            "answer": "C) Olympia"
        },
        "Which mountain range lies to the west of Washington state?": {
            "options": ["A) Rocky Mountains", "B) Sierra Nevada", "C) Cascade Range", "D) Appalachian Mountains"],
            "answer": "C) Cascade Range"
        },
        "What is the state bird of Washington?": {
            "options": ["A) American Goldfinch", "B) Willow Goldfinch", "C) Northern Mockingbird", "D) American Robin"],
            "answer": "B) Willow Goldfinch"
        },
        "What is Washington's nickname?": {
            "options": ["A) The Evergreen State", "B) The Sunshine State", "C) The Mountain State",
                        "D) The Garden State"],
            "answer": "A) The Evergreen State"
        },
        "Which Washington city is known for its famous Space Needle?": {
            "options": ["A) Seattle", "B) Spokane", "C) Bellevue", "D) Everett"],
            "answer": "A) Seattle"
        },
        "What is the largest national park in Washington?": {
            "options": ["A) Olympic National Park", "B) North Cascades National Park", "C) Mount Rainier National Park",
                        "D) Mount St. Helens National Volcanic Monument"],
            "answer": "A) Olympic National Park"
        },
        "Which Washington city is nicknamed the 'Apple Capital of the World'?": {
            "options": ["A) Wenatchee", "B) Yakima", "C) Walla Walla", "D) Spokane"],
            "answer": "A) Wenatchee"
        },
        "What is the name of the strait that separates Washington from Vancouver Island, Canada?": {
            "options": ["A) Puget Sound", "B) Strait of Georgia", "C) Strait of Juan de Fuca", "D) Rosario Strait"],
            "answer": "C) Strait of Juan de Fuca"
        },
        "Which Washington city is home to the University of Washington?": {
            "options": ["A) Seattle", "B) Spokane", "C) Tacoma", "D) Bellingham"],
            "answer": "A) Seattle"
        },
        "What is the highest peak in Washington?": {
            "options": ["A) Mount Adams", "B) Mount Rainier", "C) Mount Baker", "D) Mount St. Helens"],
            "answer": "B) Mount Rainier"
        }
    }
    all_states["California"] = California
    all_states["Alaska"] = Alaska
    all_states["Washington"] = Washington
    return all_states


def ask_question(question, options):
    print(question)
    for option in options:
        print(option)
    answer = input("Your answer (enter the letter corresponding to your choice): ")
    return answer.upper()


def geolocator(ip):
    try:
        response = requests.get(f"https://geo.ipify.org/api/v2/country,city?apiKey={api_key}&ipAddress={ip}")
        if response.status_code == 200:
            data = response.json()
            location_info = data.get("location", {})
            Region = location_info.get("region")
            return Region
        else:
            print("An Error Occurred")
    except Exception as e:
        print("An error occurred:", e)
        return None


user_location = geolocator(ip)

def main(user_location):

    all_states = states()

    state_questions = all_states[user_location]

    rand_questions = random.sample(list(state_questions.items()), 3)

    for question, data in rand_questions:
        answer = ask_question(question, data["options"])
        if answer == data["answer"][0]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", data["answer"])

@app.route('/')
def index():
    ip = requests.get('https://api.ipify.org').text
    user_location = geolocator(ip)
    all_states = states()
    state_questions = all_states[user_location]
    rand_questions = random.sample(list(state_questions.items()), 3)
    return render_template('index.html', questions=rand_questions)

if __name__ == "__main__":
    app.run(debug=True)



main(user_location)