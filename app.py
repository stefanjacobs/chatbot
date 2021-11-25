from skills import Skills
from intent import IntentCheck
from vocal_output import VocalOutputThread

import spacy
import colorama



if __name__ == '__main__':

    # startup vocal output
    vocal_output = VocalOutputThread()
    vocal_output.daemon=True
    vocal_output.start()

    # load intent check model
    intentCheck = IntentCheck()

    # load and initialize spacy for entity recognition, use 
    #   https://explosion.ai/demos/displacy
    nlp = spacy.load("en_core_web_lg")

    # load skills
    skills = Skills()

    # speak a greeting from the greeting skill
    message = skills.skills['greeting'].actAndGetResponse()
    vocal_output.say(message)

    while True:

        # get new command
        # TODO: get speech command
        command = input(colorama.Fore.RESET + "DBG> ")

        # interpret command for intent
        intent = intentCheck.getIntentFromString(command)

        # initialize standard set of parameters
        params = {'intentCheck': intentCheck, 'voice': vocal_output, 'skills': skills.skills} 

        try: # find and execute skill
            skill = skills.skills[intent]
            params |= skill.parseEntities(nlp(command))

            response = skill.actAndGetResponse(**params)
            vocal_output.say(response)
        except Exception as e:
            print(e)
            # vocal_output.say("Could not find skill, bye.")
            # break
