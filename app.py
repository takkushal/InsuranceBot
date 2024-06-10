from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    if request.method == 'POST':
        user_message = request.json.get('message')

        print("this is users message:"+user_message)

        bot_response = generate_response(user_message)

        return jsonify({'response': bot_response})

import random

def generate_response(user_message):

    user_message = user_message.lower().strip()

    # FAQs
    questions = ["who can purchase domestic travel assistance & insurance?",
                 "is there an age limit to be covered under domestic travel assistance & insurance?",
                 "can i purchase domestic travel assistance & insurance if i'm travelling for more than 30 days?",
                 "who would be the beneficiary of domestic travel assistance and insurance?",
                 "what are the travel assistance services that i’m entitled to avail?",
                 "what is the claim processing turnaround time?",
                 "what is the time limit for submitting a claim?",
                 "what do i do if i have any questions on claims settlement?",
                 "what do i do if i encounter an accident while being covered?",
                 "can i cancel my overseas or domestic travel assistance & insurance?",
                 "once i purchase overseas / domestic travel assistance & insurance can i change the date of my travel?",
                 "do i have to carry a copy of my certificate of insurance with me when travelling?",
                 "where can i get the full terms and conditions of my travel assistance & insurance?",
                 "what is overseas travel assistance and insurance? why is it required?",
                 "who can purchase overseas travel assistance & insurance?",
                 "is there an age limit to be covered under overseas travel assistance & insurance?",
                 "can i purchase overseas travel assistance & insurance if i'm travelling for more than 180 days?",
                 "in which countries are the overseas travel assistance and insurance recognized and accepted?",
                 "why do you need travel assistance?",
                 "what is travel assistance?",
                 "tell me about travel assistance",
                 "what is asego?",
                 "tell me about asego",
                 "what are the services offered by asego?",
                 "services provided by asego",
                 ""
                 ""





    ]

    answers = ["Any Indian citizen travelling within India can purchase Domestic Travel Assistance & Insurance.",
                "Yes, the passenger must be below the age of 70 years as of the date of travel to purchase from the website.Passengers above the age of 70 can reach out to us directly on P: +91 22 67872 037 E: customercare@asego.in ",
                "No, Domestic Travel Assistance & Insurance covers the passenger/s for a period of 30 days from the date of inception of the policy which is the date of commencement of the journey. In case of a round trip, the coverage will end with the return journey to the originating airport or 30 days whichever is earlier.However, you can choose our Annual Multi-trip plan which will cover you for an entire year on all your domestic trips.",
                "Benefits will be paid to the insured person's nominee or bonafide legal heir in the event of loss of life under accidental death and dismemberment. All other benefits will be payable to the insured person",
                "You can avail the following travel assistance services: 1) Medical & Travel Assistance: 24x7 emergency assistance during travel including telephonic medical assistance 2) Lifestyle assistance: Pre-trip information, weather forecast, roadside assistance, dining referral and entertainment information, etc., during the stay 3) Family protection: 24x7 medical assistance, domestic roadside assistance including vehicle breakdown services and concierge services such as dining reservation assistance, home movers, etc., for families back home.",
                "Claims will be processed within 15 working days after you've submitted all required documentation.",
                "All claims must be filed within 15 days from the expiry of the policy",
                "I m here to help you with your claim settlement. Or you can send a mail to claims@asego.in or Call at +91 22 67872 037",
                "In case of an accident, please contact: Phone: +91 22 67872 037 E-mail: claims@asego.in",
                "Yes, Overseas Travel Assistance & Insurance can be cancelled by simply sending a request email or calling us. You will receive a complete refund on cancellation. Phone : +91 22 67872 037 E-mail : customercare@asego.in",
                "Overseas / Domestic travel assistance & insurance can be endorsed or modified before the travel date by simply sending a request email or calling us. P: +91 22 67872 037 E: customercare@asego.in",
                "We encourage you to carry a copy of your Certificate of Insurance.",
                "The full Terms and Condition of your Travel Assistance & Insurance is available on our website along with the coverage benefits and also on the assistance and insurance document received by you",
                "Overseas Travel Assistance Plan offers travellers, coverage for unforeseen problems and unexpected costs incurred before or during your trip. The Overseas Assistance Plan can reimburse expenses for the pre‐paid, non‐ refundable portions of a trip if there is a requirement to cancel or interrupt the trip for a covered reason Asego offers Global Assistance services with Travel Insurance which is underwritten by reputed global insurers and accepted worldwide. Medical expenses incurred overseas are costlier than similar ones in the local country. Hence it is advisable to protect oneself with travel assistance services. Moreover, Travel Insurance is mandatory when travelling to the following countries: • Austria • Greece • Portugal • Spain • France • Germany • Belgium • Luxemburg • Netherlands • United Kingdom. It is recommended to opt for overseas travel assistance and insurance even while travelling to countries apart from those mentioned above.",
                "Any Indian citizen with a valid Indian passport can purchase overseas Travel Assistance & Insurance. Foreign passport holders can also avail of the service, provided they present a residential permit, OCI, PIO card and Indian Income Proof. Travel Insurance is also offered on the purchase of Asego travel assistance.",
                "Yes, the passenger must be below the age of 70 years as on the date of travel to purchase from the website. However, passengers above the age of 70 can reach out to us directly on P: +91 22 67872 037 |E: customercare@asego.in",
                "No, overseas travel assistance & insurance covers the passenger/s for a period of 180 days from the date of inception of the policy, i.e the date of commencement of the journey. In case of a round trip, the coverage will end with the return journey to the originating airport or 180 days whichever is earlier. However, you can choose our Annual Multi-trip plan which will cover you for an entire year on all your overseas trips",
                "Travel assistance and insurance are recognized and accepted all over the globe. For your assistance, we have an international presence through our TPA partners. Asego also offers special travel assistance & insurance depending on where you are travelling and the kind of activities you would be involved in.",
                "You will need travel assistance for various reasons : a) It protects your travel investments b) You will have access to round the clock emergency assistance c) You will have access to top quality care wherever you go d) Travel assistance with insurance can fit any budget",
                "Travel assistance refers to the provision of support, services, and guidance to travelers to ensure a safe, convenient, and enjoyable journey. It encompasses various aspects of travel, including transportation, accommodation, information, and emergency support. Asego provides global assistance for customer to have a smooth trip. ",
                "Travel assistance refers to the provision of support, services, and guidance to travelers to ensure a safe, convenient, and enjoyable journey. It encompasses various aspects of travel, including transportation, accommodation, information, and emergency support. Asego provides global assistance for customer to have a smooth trip. ",
                "Asego is one of the leading dedicated providers of Travel Assistance & Insurance with a legacy of 23 years in the sector. Asego provides travel assistance services with insurance underwritten by an IRDA authorized insurance company. They have been servicing all these years through reputed brands across various segments such as Travel Agencies, Airlines, Online Travel Agents, Travel Management Companies, Visa Servicing Centres, Student Consultants etc. and are integrated into every aspect of a traveller’s buying journey.",
                "Asego is one of the leading dedicated providers of Travel Assistance & Insurance with a legacy of 23 years in the sector. Asego provides travel assistance services with insurance underwritten by an IRDA authorized insurance company. They have been servicing all these years through reputed brands across various segments such as Travel Agencies, Airlines, Online Travel Agents, Travel Management Companies, Visa Servicing Centres, Student Consultants etc. and are integrated into every aspect of a traveller’s buying journey.",
                "Asego provides travel assistance, overseas travel protection, domestic travel protection, cruise travel protection and annual travel protection ",
                "Asego provides travel assistance, overseas travel protection, domestic travel protection, cruise travel protection and annual travel protection ",
                ""
                ""





   ]

        # Inclusion & Exclusion

    questions_inc_exc = [
                            "emergency medical expenses",
                            "emergency medical evacuation",
                            "personal accident (ad, ptd, ppd) / personal accident (common carrier) - ad, ptd, ppd",
                            "trip delay",
                            "flight delay",
                            "trip cancellation / trip interruption",
                            "missed connection",
                            "bounced hotel booking",
                            "loss of checked in baggage",
                            "delay of checked in baggage"
                        ]
    answers_inc       = ["Inclusions: Covers the emergency treatment expenses incurred by an insured while on trip due to any illness/disease and whose treatment cannot be postponed until insured’s return to India.",
                         "Inclusions: Expenses relating to transportation of an insured from the place of incident to any nearby place or country for better treatment arising out of any covered illness or injury will be paid.",
                         "Inclusions: Insurer will pay the benefit amount shown in the policy in case an insured dies due to any visible violent external means.",
                         "Inclusion: It covers the expenses incurred towards food and accommodation in case the fight is missed due any adverse weather or technical issues of the aircraft.",
                         "Inclusions: The coverage will indemnify the expenses incurred in arranging alternate transportation due to delay of flight after deducting the refunds from airlines. The delay should be caused by inclement weather, riots, strike, industrial actions, or any delay solely by the airlines. ",
                         "Inclusions: Covers the non-refundable expenses incurred by an insured due to cancellation / curtailment of trip. Covers the cost of rejoining the trip.",
                         "Inclusions: Will pay for the cost of new tickets or the difference of cost between the old and new tickets in case the connecting flight is missed due to the incoming prior flight. ",
                         "Inclusions: Will pay for the additional cost of upgrading to a better room in case of over booking of the hotel room. ",
                         "Inclusions: Loss of checked in baggage is covered if the baggage is lost under custody or airline. ",
                         "Inclusions: Covers the expenses incurred in purchasing of emergency items in lieu of delay of baggage out of the Republic of India."
                    ]
    answers_exc   = ["Exclusions: Does not cover expenses incurred due to any pre-existing medical condition or mental disorders etc.",
                     "Exclusions: Any expense related to any pre-existing illness or u-injury will not be covered.",
                     "Exclusions: Death due to natural reason is not covered",
                    "Exclusions: Will not cover the cost of new air tickets or any delay involving delay from insured’s end.",
                    "Exclusions: Any delay already foreseen / anticipated by the insured at the time of booking. ",
                    "Exclusions: Does not cover the consequential losses due to trip cancellation/ curtailment / interruption. ",
                    "Exclusions: Any delay on part of the insured. Any compensation paid by the airline. ",
                    "Exclusions: if the insured fails to reach the hotel and check in on time as stipulated.",
                    "Exclusions: Loss or theft of baggage is not covered.",
                    "Exclusions: Inbound delay of baggage is not covered."
                ]

    #greeting
    greetings = ["good morning good afternoon good evening good night hello hey hi","bye","thank you thanks thankyou "]
    g_response =["How can I help you?","What can I do for you?","How can I help you?","Do You have any questions for me?","Ask me a query..."]
    l_response =["Bye!! You can ask me anytime."]
    t_response =["You 're Welcome! Feel free to Ask Me Anytime 🙂"]

    if user_message in greetings[0]:
        return user_message.capitalize() +"!!! "+ random.choice(g_response)
    elif user_message in greetings[1]:
        return l_response[0]
    elif user_message in greetings[2]:
        return t_response[0]
    elif user_message in questions:
        for i in range(len(questions)):
            if user_message in questions[i]:
                return answers[i]
                break
    elif user_message in questions_inc_exc:
        for i in range(len(questions_inc_exc)):
            if user_message in questions_inc_exc[i]:
                return answers_inc[i]+"\n"+answers_exc[i]
                break
    else:
        responses = [
            "I'm not sure I understand.",
            "Could you please rephrase that?",
            "I'm sorry, I didn't catch that.",
            "Let me think about it for a moment...",
            "Hmm... I'm not sure how to respond to that."
        ]
        return random.choice(responses)





if __name__ == '__main__':
    app.run(debug=True)