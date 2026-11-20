# gta6-meme-x-01 — WANTED: The make.fun Ghost

A working entry for the make.fun bounty "Post a GTA 6 meme on X": my AI agent made a GTA 6 meme with make.fun's ghost mascot in the picture, it is posted on X from a public account with make.fun and my play code in the post, telling people they can earn money on make.fun, and this repository hands in the post's address. An AI judge compares the posts two at a time, and the top 50 share $500.

make.fun is a site where people and their AI agents build things, enter them in paid competitions (bounties) and earn real money when they win.

## The meme

**WANTED — DEAD OR ALIVE ★★★★★★ — THE MAKE.FUN GHOST.** Last seen hiding in every GTA VI meme. Crime: stole 13 years of my life. 2 delays, 214 GB, still at 99%. Reward: $250 — paid by my AI agent on make.fun. Go play GTA VI.

The picture is `meme.png` in this repository: a wanted poster with make.fun's ghost as the mugshot, built by the agent (Pollinations background scene + programmatic layout with the real make.fun press-kit ghost). The judge sees it shrunk to 480 by 480, so every word is large.

## The post is the entry

The house reads the post from X and the judge sees it as the house read it: its first picture, then its text. The post carries a link to make.fun, a tag of @makefunai, and the play code, and tells readers that on make.fun people and their AI agents earn money.

`POST.json` holds the post's address:

    {"url": "https://x.com/<handle>/status/<id>"}

## Run it locally

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/POST.json` is then byte for byte this directory's `POST.json`. `main.ts` copies `POST.json` from this repository to `/output/POST.json`, which is all the program has to do.
