## Rasperry Pi Vintage Clock

This is the project for my dream project of redoing the internals of an old alarm clock.

### Inspiration
I had a 90s Realistic (RIP Radio Shack) alarm clock growing up, and I want to recreate the feeling I had using it to
listen to the radio at night (Coast to Coast AM!), but in a much more useful, modern fashion.

### Hardware
- 1 Rasperry Pi, SD Card, etc. (I'll be using a 3 B+ until I can get a 4)*
- 1 Sanyo RM 5005 (Or comparable Sanyo unit)*
- 1 I2C LCD (I use a 20x4 screen)
- Exact part list to come as I build...

#### Hardware Notes
I was considering the ESP8266 instead of a Pi as I have one on hand, but the pure software benefits of using a full Linux
machine FAR outweigh the cleverness and speed of shipping MicroPython and throwing together all my own solutions.

Regarding the actual donor alarm clock unit, I have NO idea at the time of writing how compatible the actual clock interfaces are, as they are
very out of date, and most likely proprietary solutions I'll need to manually verify and reverse engineer. In fact, I am
only able to find a service manual online for the big brother, the Sanyo RM 5900, though it is on average 10-15 USD MORE
than the 5005 and was not worth the money for something I might completely break while reverse-engineering...

I plan to eventually move to a Realistic brand clock as my main target, but the Sanyo RM 5005 looks cool, and was available
_very_ cheap at the time of writing.

### Software
This is written almost exclusively in Python as C would be pointlessly complicated for this. I'm skipping a pure
microcontroller for now as I plan on relying on some software solutions on the pi for things like bluetooth, local
music, etc.

I highly recommend using the following development setup:
- Raspberry Pi running Ubuntu 64-bit
  - Ubuntu is a more of a personal preference, feel free to use Raspberry Pi OS 
- PyCharm Professional (JetBrains). Costs money, but is far better than the free tier
  - Remote interpreter setting to SSH into pi for development

If you have the option, remote development FAR outclasses native Pi development. You're still running all of your code
on the Pi, but even the Pi 4 just does _not_ have what it takes yet to run a beefy IDE like PyCharm or VS Code.

### Pics
Coming soon!
