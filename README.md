# Pico Controller

Have you ever seen Twitch sessions of [Tix Le Geek](https://www.twitch.tv/tixlegeek)? His videos feature a lovely animated Tux that he controls [example](https://www.twitch.tv/videos/1238076779) with a game controller.

Basically, the idea is to do "the same" but with [Pico le Croco](https://pico.masdescrocodiles.fr/), my own character, that I enjoy to draw. 

Except this is only the *beginning*, it's not as good as what TixLeGeek does, no game controller, only few gestures etc.

# How to setup

Preliminary steps:

- It's probably a good idea to setup a virtual environment, but do as you wish `python3 -m venv venv`
- `pip3 install -r requirements.txt`

Launching the setup:

1. **Server**. `python3 server.py`. Leave that open.
2. **Controller**. In another shell, `python3 control.py`. This is where we type commands to animate Pico.
3. **OBS Studio**. Setup the sources of whatever you want to show on your stream + for Pico, an additional source "Browser". In the URL: `http://127.0.0.1:5000` (or wherever your server runs). Width x Height: I recommend something like 600 x 1024. 

Controlling Pico:

In the Controller, type the commands on your keyboard. I haven't implemented a gamepad controller or any other type of controller. 

```
$ python3 control.py 
Press w=up a=left d=right g=nasty n=normal t=say q=quit
```

So far, we can *move* the eyes of Pico, his *eyebrows* and have him *say* something.
To have Pico speak, press "t", then enter your message + ENTER:

```
Enter your message and press Enter:
Thanks to @tixlegeek!!!
Sending message: Thanks to @tixlegeek!!!
Back to control mode. Press q to quit.
```

After that, you can enter again commands such as w, a, d etc.

To *remove* what Pico says, have him speak with a *blank* message.

# License

- `static/*.png static/*.xcf`: The images of Pico le Croco are distributed under [License CC-BY-NC-SA](http://creativecommons.org/licenses/by-sa/4.0/)
- The code of this repository is distributed under *MIT License*.
