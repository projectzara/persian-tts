# Basic Text to Speech for Persian Language

As _Project Z.A.R.A_ is going to be a very big A.I. assistant (think about _Marvel level_), I needed a TTS system. On macOS, I didn't have any choice for a good Persian voice. On Linux, speech engines sound so freaking robotic. I decided to make something simple, but effective. So this is the _proof-of-concept_. 

## How does it work? 

In [sounds](sounds) directory, you can find a bunch of `wav` files and a `sounds.csv` file. This is the example input data. This engine doesn't have any A.I. or fancy stuff and works directly with _recorded words_. It can make it so heavy, but it's good for a special purpose assistant. 

The `engine.py` file, simply converts your input to a `wav` file. The `interface` is an interactive interface that helps you hear what you want immediately. 

## Dependencies

1. Install _portaudio_ on your operating system. On Linux it's mostly available from repositories. On macOS, you can simply use `brew`. 
2. `pyaudio`
3. `pydub` 

Other libraries are python defaults, as I wanted to keep it simple. 