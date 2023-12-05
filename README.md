# Cooldown Timers for Everquest
## Overview
This application provides a visual cooldown timers, triggered by customizable keyboard input. Nothing about it is specific to EverQuest, but it was created with EverQuest in mind.

## Download

- [Download the latest version](https://github.com/frostedpears/eq_cooldown/releases/download/v1.0/eq_cooldown_1.0.zip)
- Unzip eq_cooldown_1.0.zip
- Customize skills.yaml
- Run eq_cooldown.exe

## Features

![main window](/docs/main_window.png)

eq_cooldown runs in the background.

When the **input key** is pressed, the progress bar resets to 0, and fills based on the cooldown set in *skills.yaml*. If you've set an **output key**, that keypress will be sent to the active window.

In the image above, pressing the '2' key will reset the progress bars for 'sense' and 'tracking', as well as sending the keys '5' and '6' to the active window.

Pressing the **reset button** will reset the timer to 0, but won't press the output key.

If an output key is set to the same key as another skills input key, it will not be sent, to prevent an infinite loop.

## Configuration (skills.yaml)
open *skills.yaml* in a text editor to adjust the skills you wish to track. Each entry should be in the following format (indentation is important):

``` yaml
kick:
  cooldown: 8.5
  inkey: 'f21'
  outkey: '4'
```

Line 1: 'kick' will appear on the reset button. Each entry must have a unique name.

'cooldown' is the amount of time, in seconds, of the progress bar.

'inkey' is the activation key. It must be a single key, combinations such as ctrl+2 are not currently supported.

'outkey' is the key which will be sent to the active window. Again, key combinations are not supported.

Add as many timers as you want. Multiple entries can share an input key and/or an output key

To update the configuration after changing *skills.yaml*, close and reopen the application.

#### Example Configuration
```yaml
kick:
  cooldown: 8.5
  inkey: 'f21'
  outkey: '4'
sense:
  cooldown: 2.5
  inkey: '2'
  outkey: '5'
tracking:
  cooldown: 10.5
  inkey: '2'
  outkey: '6'
forage:
  cooldown: 100
  inkey: '7'
```

## Tips
The program was designed for skills, but the timers can be useful for a variety of things. For instance, they make greate spawn timers.

Timers will be activated in order, from top to bottom. When pressing a key, the first item that is ready will be activated, and after a short delay, the next one will activate. In this way, you can manage several timers with a single key. Tap the key quickly to start the first timer. The next time you tap it, the next will start, etc.

Holding the key down will activate the skill as soon as the cooldown is ready. For instance, if you want to use Sense Heading every time it is available, you can hold down the input key, and the output key will be sent every time the timer elapses.

This program only accepts keyboard input, but works great with accesories like controllers or foot pedals. To use a controller, consider a program like [AntiMicroX](https://github.com/AntiMicroX/antimicrox/) which translates gamepad input into keyboard input.

## Running from Source (for advanced users)
- Copy the repository to your local machine.

- Install requirements
``` bash
pip install -r requirements.txt
Customize your skills using the skills.yaml file.
```
- Run the application.

``` bash
python main.py
```
