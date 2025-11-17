import re
import unicodedata
content = """\nComing Soon\nUpcoming 7 days\n\nCall of Duty: Black Ops 7\nNov 14, 2025\n\nSweetie Candy Maze: Yellow Lemon\nNov 14, 2025\n\nCaemdale\nNov 14, 2025\n\nCode Violet\nNov 14, 2025\n\nSnail Mail\nNov 14, 2025\n\nLittle Nightmares III: Klonoa Costumes Set\nNov 14, 2025\n\nDark Atlas: Infernum\nNov 14, 2025\nNo image\nDragon Ball: Sparking! Zero - Season Pass Bonus\nNov 14, 2025\nNo image\nSpy Guy American Dream\nNov 14, 2025\nNo image\nDragon Ball: Sparking! Zero - Ultimate Edition Bonus\nNov 14, 2025\n\nDynasthir\nNov 14, 2025\n\nCarCam\nNov 14, 2025\n\nDice of Kalma\nNov 14, 2025\n\nStarbrew Station\nNov 14, 2025\n\nBuilt by Force\nNov 14, 2025\n\nSisyphus Is a Bug\nNov 14, 2025\n\nFraud Camp: Survival Escape\nNov 14, 2025\n\nReady or Not: VRO Mod\nNov 14, 2025\n\nMage of Tempest Castle\nNov 14, 2025\nNo image\nLittle Nightmares III: Nomes Costumes Set\nNov 14, 2025\n\nInazuma Eleven: Victory Road\nNov 14, 2025\n\nBeyond R: Rule Ripper\nNov 14, 2025\n\nClawpunk\nNov 14, 2025\n\nCarefully Stamped\nNov 15, 2025\n\nThe Saint Wife’s Newlywed Trials\nNov 15, 2025\n\nFracctal TCG\nNov 15, 2025\n\nEscape from Tarkov\nNov 15, 2025\n\nBlade Tempest\nNov 16, 2025\n\nMagic Kingdom\nNov 16, 2025\n\nSolvimus\nNov 16, 2025\n\nTry 2 Sleep\nNov 17, 2025\n\nThe Berlin Apartment\nNov 17, 2025\n\nPieces of the Past\nNov 17, 2025\n\nForestrike\nNov 17, 2025\n\nClaire a la Mode\nNov 17, 2025\n\nBony Odyssey\nNov 17, 2025\n\nUmami\nNov 17, 2025\n\nLeaf Blower Co.\nNov 17, 2025\n\nSolo Leveling: Arise Overdrive\nNov 17, 2025\n\nResident Evil: Survival Unit\nNov 17, 2025\n\nStay Alive for Me\nNov 17, 2025\n\nPro Basketball Manager 2026\nNov 17, 2025\n\nDoomriderz\nNov 17, 2025\n\nInterstellar Espionage Inc.\nNov 17, 2025\n\nRaidbound\nNov 17, 2025\n\nThe Planet Crafter: Toxicity\nNov 17, 2025\n\nApproaching Infinity: Shipyards\nNov 17, 2025\n\nEvolution: From the Little Light\nNov 18, 2025\n\nMagic Forge Tycoon\nNov 18, 2025\n\nOutside Parties\nNov 18, 2025\n\nKeep Gambling\nNov 18, 2025\n\nTomb Raider: Anniversary\nNov 18, 2025\n\nThe Lord of the Rings: Return to Moria - Durin's Folk Expansion\nNov 18, 2025\n\nMyths are 100% True\nNov 18, 2025\n\nSpongeBob SquarePants: Titans of the Tide\nNov 18, 2025\n\nDesert Race Adventures\nNov 18, 2025\n\nCube Mind\nNov 18, 2025\n\nAssassin’s Creed Mirage: Valley of Memory\nNov 18, 2025\n\nBeak the Hunter\nNov 18, 2025\nNo image\nSpongeBob SquarePants: Titans of the Tide - Tidal Season Pass\nNov 18, 2025\nNo image\nPixel Cross Stitch: Color by Number - Autumn Pack 3\nNov 18, 2025\nNo image\nSpongeBob SquarePants: Titans of the Tide - Plankton's Portal Challenge DLC\nNov 18, 2025\n\nCosmic Tails\nNov 18, 2025\n\nPowwow Bound: A Menominee Homecoming\nNov 18, 2025\nNo image\nSpongeBob SquarePants: Titans of the Tide - Natural Costume Pack\nNov 18, 2025\n\nKingdoms of the Dump\nNov 18, 2025\n\nLost Curse\nNov 18, 2025\n\nVirago World\nNov 18, 2025\n\nDispersio 3\nNov 18, 2025\n\nBirdcage\nNov 18, 2025\n\nDeadpool VR\nNov 18, 2025\n\nSektori\nNov 18, 2025\n\nMorsels\nNov 18, 2025\n\nBirdcage\nNov 18, 2025\n\nBrush Burial: Gutter World\nNov 19, 2025\n\nGoat Simulator 3: Baadlands: Furry Road\nNov 19, 2025\n\nThe Existence Theory of the No.13 High School\nNov 19, 2025\n\nDemonschool\nNov 19, 2025\nNo image\nSonic Racing: CrossWorlds - SpongeBob SquarePants Pack\nNov 19, 2025\n\nDuskpunk\nNov 19, 2025\n\nDisney Dreamlight Valley: Wishblossom Ranch\nNov 19, 2025\n\nPenelope Pendrick and the Art of Deceit\nNov 19, 2025\n\nMara\nNov 19, 2025\n\nChessemble\nNov 19, 2025\n\nKirby Air Riders\nNov 20, 2025\n\nTentacle Tango\nNov 20, 2025\n\nNeon Inferno\nNov 20, 2025\n\nR-Type Delta: HD Boosted\nNov 20, 2025\n\nOutlaws + Handful of Missions: Remastered\nNov 20, 2025\n\nVade Retro Satana\nNov 20, 2025\n\nSamurai Academy: Paws of Fury\nNov 20, 2025\n\nCapoeira Origins\nNov 20, 2025\n\nRoboquest VR\nNov 20, 2025\nNo image\nA Fool's Errand\nNov 20, 2025\n\nKriophobia\nNov 20, 2025\nNo image\nCricket 26\n\nHome\n\nDifficult Game About Letters\n\nSaborus\n\nSun Halo\n\nFlashpoint Campaigns: Cold War\n\nAs I Began to Dream\n\nNo image\n\n\n\n\n\n\n\n\n\n\n\n\n\nYour Move\n\nRetrace the Light\n\nGran Theft Lure\n\nDictator Simulator: Gradnar\nUpcoming 14 days\n\nDead Wells: The Devil Fragment\n\nDictator Simulator: Gradnar\n\nSuper Reaktor\n\nTerrifier: The ARTcade Game\n\n\n\n\n\n\n\nCaptain Wayne: Vacation Desperation\n\n\n\n\n\n\n\n\n\n\n\n\nNo image\nNo image\nNo image\n\nI Will Never Fall for My Tsundere Classmate, so I Will Just Date a Background Character Instead!\n\n\n\nNo image\n\n\nBuilt by Force\n\nCarCam\n\nStarbrew Station\n\nSisyphus Is a Bug\n\nCaemdale\n\nReady or Not: VRO Mod\n\nBeyond R: Rule Ripper\n\nMage of Tempest Castle\n\nCode Violet\n\nClawpunk\n\nInazuma Eleven: Victory Road\n\nFraud Camp: Survival Escape\n\nDice of Kalma\n\nDark Atlas: Infernum\n\nSnail Mail\n\nDynasthir\n\nCall of Duty: Black Ops 7\nNo image\nDragon Ball: Sparking! Zero - Season Pass Bonus"""


lines = content.split("\n")

def is_data_format(date_str):
    pattern = r'^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}, \d{4}$'
    # 使用 fullmatch 检查整个字符串是否完全匹配
    return bool(re.fullmatch(pattern, date_str))

def create_url(s):
    # 空格 : ！ +替换成 -
    # ’ . 去掉
    normalized = unicodedata.normalize('NFKD', s)
    without_accents = ''.join([c for c in normalized if not unicodedata.combining(c)])
    # 2. 转为小写
    lower_case = without_accents.lower()
    kebab_cases = lower_case.split(" ")
    kebab_cases = [re.sub(r'[:!+.\'’]', '', kebab_case) for kebab_case in kebab_cases if kebab_case != " " and kebab_case != "-" and kebab_case != "+" ]
    return "-".join(kebab_cases)

result = []


for i in range(len(lines)):
    if is_data_format(lines[i]):
        game_url = f"https://www.igdb.com/games/{create_url(lines[i-1])}"
        result.append(dict(name=lines[i-1],date=lines[i], url=game_url))




for r in result:
    print(r)



