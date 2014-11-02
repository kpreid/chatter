#!/usr/bin/env python

import sys, os, random, time

voices = [
"Agnes",
"Albert",
"Alex",
#"Bad News",
"Bahh",
#"Bells",
"Boing",
"Bruce",
"Bubbles",
#"Cellos",
"Deranged",
"Fred",
#"Good News",
#"Hysterical",
#"Junior",
#"Kathy",
#"Pipe Organ",
#"Princess",
"Ralph",
#"Trinoids",
"Vicki",
#"Victoria",
"Whisper",
"Zarvox"]

#voices = ["Alex"]

words = [x.rstrip().lower() for x in open("/usr/share/dict/words")]

while True:
  voice = random.choice(voices)
  #voice = "Vicki"
  text = " ".join("".join(random.sample(words, 4)) for x in range(1, 5))
  print voice, "-", text
  os.spawnlp(os.P_NOWAIT, "say", "say", "-v", voice, "[[rate 1]]", text)
  time.sleep(10)

# notes:
# Halloween ambient voice generator
#   generate text (source corpus? Markov-chain? quotes? dialogue? Lojban?)
#   insert speech commands (wobble rate, ...)
#   speak in random voice