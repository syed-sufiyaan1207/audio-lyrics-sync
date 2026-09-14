import sys
import time
import random
import os
from playsound3 import playsound


# =========================================================
# COLORS
# =========================================================

RESET = "\033[0m"
BOLD = "\033[1m"

COLORS = [
    "\033[91m",
    "\033[95m",
    "\033[96m",
    "\033[93m",
    "\033[94m"
]
lyrics = [
"Hey",
"Havana, ooh na-na (ayy)🌴",
"Half of my heart is in Havana, ooh-na-na (ayy, ayy)💗",
"He took me back to East Atlanta, na-na-na🌆",
"Oh, but my heart is in Havana (ayy)✨",
"There's somethin' 'bout his manners (uh-huh)😏",
"Havana, ooh, na-na (uh)🌺",
"He didn't walk up with that, How you doin'? (uh)💃",
"(When he came in the room)🌙",
"He said there's a lot of girls I can do with (uh)💭",
"(But I can't without you) ☀️",
"I knew him forever in a minute (hey) 🫶",
"(That summer night in June) 💘",
"And papa says he got malo in him (uh) 🥹",
"He got me feelin' like ❤️",
"Ooh-ooh-ooh, I knew it when I met him (ayy) ✈️  ",
"I loved him when I left him💗",
"Got me feelin' like❤️",
"Ooh-ooh-ooh, and then I had to tell him🌺",
"I had to go, oh, na-na-na-na-na (woo)” 🌆",
"Havana, ooh na-na (ayy, ayy)🌴",
"Half of my heart is in Havana, ooh-na-na🌴 (ayy, ayy, uh-huh)",
"He took me back to East Atlanta, na-na-na🌴",
"Oh, but my heart is in Havana (ayy)🌴",
"My heart is in Havana 🌴(ayy)",
"Havana, ooh, na-na.🌴"
]

# =========================================================
# CHARACTER-BY-CHARACTER EFFECT
# =========================================================

def type_line(text, color, start_time, start, end):

    if not text:
        return

    # Wait until the actual lyric starts
    while time.perf_counter() - start_time < start:
        time.sleep(0.002)

    # How much time this particular lyric has
    duration = end - start

    # Number of characters
    characters = len(text)

    if characters == 0:
        return

    # Character-by-character speed calculated
    # from the actual timing of this lyric
    char_delay = duration / characters

    sys.stdout.write(color + BOLD)
    sys.stdout.flush()

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()

        time.sleep(char_delay)

    sys.stdout.write(RESET + "\n")
    sys.stdout.flush()


# =========================================================
# START HAVANA
# ==================================================
# PLAY SONG
# ==================================================

audio_file = input("Enter the path to your MP3 file: ")

if not os.path.isfile(audio_file):
    print()
    print("❌ Audio file not found.")
    print("Please check the file path and try again.")
    sys.exit()

sound = playsound(
    sound=audio_file,
    block=False
)

# Timer starts when the audio is launched
start_time = time.perf_counter()


# =========================================================
# ACTUAL LINE START TIMES
#
# These correspond to the exact line structure of
# the lyrics you pasted.
# =========================================================

LINE_STARTS = [
    1.82,    # Hey
    9.21,    # Havana...
    11.99,   # Half of my heart...
    16.88,   # He took me back...
    21.15,   # Oh, but my heart...
    24.12,   # There's somethin'...
    26.26,   # Havana...
    27.75,   # He didn't...
    30.86,   # When he came...
    32.35,   # He said...
    35.45,   # But I can't...
    36.90,   # I knew...
    40.04,   # That summer...
    41.60,   # And papa...
    44.59,   # He got me...
    45.95,   # Ooh... I knew...
    51.45,   # I loved...
    54.26,   # Got me...
    55.02,   # Ooh... and then...
    60.47,   # I had to go...
    64.07,   # Havana...
    66.87,   # Half...
    71.65,   # He took...
    75.89,   # Oh...
    78.95,   # My heart...
    81.09,   # Havana...
    83.99,   # Just graduated...
    88.26,   # Fresh out...
    91.71,   # Fresh out East Atlanta
    93.03,   # Bump...
    97.10,   # Hey, I was...
    101.42,  # Back it on me...
    104.06,  # Get to...
    105.93,  # She waited...
    107.46,  # Shawty cakin'...
    110.36,  # This is history...
    112.56,  # Point blank...
    114.75,  # If it cost...
    117.20,  # I was gettin'...
    119.16,  # Havana...
    121.93,  # Half...
    126.61,  # He took...
    131.00,  # Oh...
    133.65,  # My heart...
    135.94,  # Havana...
    137.77,  # Ooh na-na...
    140.55,  # Take me...
    141.93,  # Ooh na-na...
    145.00,  # Take me...
    146.39,  # Ooh na-na...
    149.69,  # Take me...
    151.00,  # Ooh na-na...
    154.38,  # Take me...
    158.72,  # Hey, hey
    164.98,  # Ooh-ooh-ooh
    169.32,  # Ooh-ooh-ooh
    172.52,  # Take me back...
    174.33,  # Havana...
    176.58,  # Half...
    181.21,  # He took...
    185.58,  # Oh...
    188.60,  # My heart...
    190.94,  # Havana...
    192.78,  # Uh-huh
    193.29,  # Oh na-na-na
    198.17,  # Oh na-na-na
    200.71,  # Oh na-na-na
    203.98,  # No, no, no...
    207.58,  # Oh na-na-na
    209.13   # Havana...
]


# =========================================================
# SAFETY CHECK
# =========================================================

for i, line in enumerate(lyrics):

    if i >= len(LINE_STARTS):
        break

    start = LINE_STARTS[i]

    if i + 1 < len(LINE_STARTS):
        end = LINE_STARTS[i + 1] - 0.08
    else:
        end = start + 2.0

    color = random.choice(COLORS)

    type_line(
        line,
        color,
        start_time,
        start,
        end
    )

    # =====================================================
    # PLAY CHARACTER-BY-CHARACTER
    # =====================================================




# =========================================================
# END
# =========================================================

sys.stdout.write(RESET + "\n")
sys.stdout.flush()

print("\n❤️ END ❤️")