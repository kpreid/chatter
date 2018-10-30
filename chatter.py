#!/usr/bin/env python

# Copyright 2010, 2014, 2018 Kevin Reid
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import absolute_import, division, print_function

import os
import random
import subprocess
import time

def find_voices():
    voice_list_output = subprocess.check_output(['say', '-v', '?'])
    voices = set(line.strip().split()[0] for line in voice_list_output.strip().split('\n'))
    
    # Blacklist too basically-high-pitched or plain voices
    voices -= {'Moira'}
    
    return list(voices)

    # In the old days, we had a hardcoded list of the builtin voices that were suitable. But the classic wacky voices are gone now. R.I.P.
    #     "Agnes",
    #     "Albert",
    #     "Alex",
    #     "Bahh",
    #     "Boing",
    #     "Bruce",
    #     "Bubbles",
    #     "Deranged",
    #     "Fred",
    #     "Ralph",
    #     "Vicki",
    #     "Whisper",
    #     "Zarvox"

def find_words():
    # TODO: Might want to omit some words / use a different list.
    return [x.rstrip().lower() for x in open("/usr/share/dict/words")]

def chatter(
        voices,
        words,
        commands="[[rate 100]][[volm 0.1]][[pbas - 100]]",
        words_per_word=4,
        words_per_voice=5):
    # For information on the commands, see Apple's Speech Synthesis Programming Guide.
    # https://developer.apple.com/library/mac/documentation/UserExperience/Conceptual/SpeechSynthesisProgrammingGuide/FineTuning/FineTuning.html#//apple_ref/doc/uid/TP40004365-CH5-SW10
    # [[rate 1]] used to work for very slow, but as of macOS 10.13.6 seems to be ignored.

    while True:
        voice = random.choice(voices)
        text = " ".join("".join(random.sample(words, words_per_word)) for _ in xrange(words_per_voice))
        print(voice, "-", text)
        os.spawnlp(os.P_NOWAIT, "say", "say", "-v", voice, commands, text)
        time.sleep(10)
    
def main():
    voices = find_voices()
    words = find_words()
    print('Voices: ', voices)
    chatter(
        voices=voices,
        words=words)

if __name__ == '__main__':
    main()