# Sir-Bot-A-Lot - A highly customizable chatbot for desktop work

This is chatbot that lets you implement custom python skills in a simple way.

It features:

- **Simple**: It is easy to use and customize. The complex features are locked away and hidden behind a simple interfaces.
- **Customizable**: You can create your own skills and add them to the bot by implementing an abstract class.
- **Intent detection**: When implementing your own skills, you can set up samples that the bot can be trained upon.
- **Trainable**: You can train the bot on your own skills and samples by using `tensorflow` and `keras`.
- **Entity detection**: Entity detection is implemented using `spacy` to add parameters to your skill.
- **Async voice output**: The bot speaks the voice output asynchronously to the user by using `pyttsx3`. (Area for improvement ;-) )




## Installation

This repository uses `poetry` to manage dependencies. So start by installing `poetry` and then run `poetry install`. When finished, you can run `make run` to start the bot.

```text
$ poetry run python3 app.py
Hi!
DBG> What is the current time?
The time is 10:45 o'clock.
DBG> Tell me a joke!
What's the difference between England and a tea bag? The tea bag stays in the cup longer.
DBG> Bye!
Bye!
Shutting down...
```

## License

At the moment I chose the license to be GPLv3. This is because this is a free software project and I want to share it with others. If you want to use this project in a commercial way, please contact me and I will try to find a way to make it commercial.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## References

- [Medium Article: How to build a chatbot using deep learing](https://towardsdatascience.com/how-to-build-your-own-chatbot-using-deep-learning-bb41f970e281)
- [Spacy dependency visualizer](https://explosion.ai/demos/displacy)
- [Jarvis desktop assistant](https://github.com/sukeesh/Jarvis)

## TODOs

- [ ] Show entity detection on a non classified example
- [ ] More skills, e.g.:
  - [ ] Work time tracking
  - [ ] Open mail.
  - [ ] Write new mail.
  - [ ] Open browser with search for entity
  - [ ] ...
- [ ] Is it possible to implement dialogs using this system?
- [ ] Stupid tensorflow warnings should be left out of the output
- [ ] Voice Input - simple.
- [ ] Voice Activation - need to do some research.
- [ ] Help skill intent name is only `hel`. Why is that and how can it be fixed?
- [ ] Voice output is very slow, very very slow. How can that be fixed?
- [ ] Voice output with different intonations (there are at least 30 on my system), configurable?
- [ ] Load skills at runtime, so if you change something in the skill, you do not have to restart the bot.
