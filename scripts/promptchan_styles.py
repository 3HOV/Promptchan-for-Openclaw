#!/usr/bin/env python3
"""
PromptChan AI - 查看可用的风格、姿势、滤镜列表
"""

import argparse


# 可用风格
STYLES = [
    'Cinematic', 'Anime', 'Hyperreal', 'Hyperanime', 'K-Pop', 'Fur', 'Furtoon',
    'Render XL+', 'Illustration XL+', 'Anime XL', 'Anime XL+', 'Hardcore XL',
    'Cinematic XL', 'Photo XL+', 'Hyperreal XL+'
]

# 可用滤镜
FILTERS = [
    'Default', 'Cyberpunk', 'VHS', 'Manga', 'Flash', 'Analog', 'Professional',
    'Cinematic', 'Studio', 'Polaroid', 'Vintage'
]

# 常用姿势（部分）
COMMON_POSES = [
    'Default', 'POV Missionary', 'POV Blowjob', 'POV Doggystyle',
    'Cum in Mouth', 'POV Cowgirl', 'Titjob', 'Mating Press',
    'Spread Ass', 'Cumshot', 'Kneeling', 'Sitting', 'Showering',
    'Cuddling', 'Smiling', 'Orgasm Face', 'POV Anal', 'Bukkake'
]

# 完整姿势列表
ALL_POSES = [
    'Default', 'POV Missionary', 'POV Blowjob', 'POV Doggystyle',
    'Cum in Mouth', 'After Sex', 'Handjob', 'Carrying Sex', 'Flashing Boobs',
    'Breast Squeeze', 'Front View Cowgirl', 'ButtJob', 'Side View Blowjob',
    'Stick out Tongue', 'POV Spitroast', 'Just Before Sex',
    'POV Threesome BlowJob', 'Grab Ass', 'Mating Press', 'POV Reverse Cowgirl',
    'Thigh Sex', 'POV Anal', 'Piledrive', 'Vagina Spread', 'Imminent Sex',
    'Female Masturbation', 'Jacko Pose', 'Sideway Ass', 'Titjob', 'Titjob Real',
    'Titjob Anime', 'Spread Ass', 'Bukkake', 'Spooning', 'Amazon Position',
    'On/Off Clothing', 'Shirt Pull', 'Cheek Bulge Blowjob', 'Solo Breast Grab',
    'From Below', 'Resting On Stomach', 'Blowjob Under Desk', 'Penis',
    'Breasts Pressed Against Glass', 'Reverse Deepthroat', 'Orgy', 'Cum on Ass',
    'Cumshot', 'Ass On Glass', 'Multiple Hands', 'Facesitting', 'On Off',
    'Side Blowjob', 'Kneeling', 'POV Breast Grab', 'Surrounded by Penises',
    'Orgasm Face', 'Flashing In Public', 'Mooning', 'Wet Tshirt',
    'Lesbian Oral', 'Lesbian Fingering', 'Lesbian Scissoring',
    'Gay Cowboy Anime', 'Gay Cowboy Real', 'Gay Grabbing', 'BDSM Suspension',
    'BDSM Tied Up', 'BDSM Tape', 'BDSM Ballgag', 'BDSM Leash', 'Downblouse',
    'Sitting', 'Vagina', 'Showering', 'Cum Bath', 'Cuddling', 'Lesbian Cuddling',
    'Gay Cuddling', 'POV Cowgirl', 'Feet', 'Multiple Mooning', 'Giant',
    'Upset', 'Disgusted', 'Scared', 'Winking', 'Angry', 'Smiling', 'Laughing',
    'Ouch', 'Shocked', 'Side Blowjob Real', 'Sucking Nipple', 'Finger Sucking',
    'Showing off Ass', 'Wind Lift/ Nip Slip', 'Reverse Blowjob',
    'Lying Down Feet', 'Footjob', 'Dildo', 'Handbra/Holding Boobs',
    'Milking Machine', 'Panties Off', 'Double Handjob', 'Undressing',
    'Bubble Bath', 'Caught Naked Embarrassed', 'Gloryhole', 'Xray Glasses',
    'Man Grabbing Boobs', 'Glory Wall', 'Wind Lift', 'POV Deepthroat',
    'POV Strangling', 'Licking Dick'
]


def main():
    parser = argparse.ArgumentParser(description='PromptChan 可用选项列表')
    parser.add_argument('--type', '-t', required=True,
                       choices=['styles', 'filters', 'poses', 'all'],
                       help='查看类型')
    parser.add_argument('--json', action='store_true', help='以 JSON 格式输出')
    
    args = parser.parse_args()
    
    if args.type == 'styles' or args.type == 'all':
        print("\n=== 可用风格 (Styles) ===")
        for i, style in enumerate(STYLES, 1):
            print(f"{i:2}. {style}")
    
    if args.type == 'filters' or args.type == 'all':
        print("\n=== 可用滤镜 (Filters) ===")
        for i, f in enumerate(FILTERS, 1):
            print(f"{i:2}. {f}")
    
    if args.type == 'poses' or args.type == 'all':
        print(f"\n=== 可用姿势 (Poses) - 共{len(ALL_POSES)}种 ===")
        print("\n常用姿势:")
        for i, pose in enumerate(COMMON_POSES, 1):
            print(f"{i:2}. {pose}")
        print(f"\n完整列表共 {len(ALL_POSES)} 种姿势，详见 SKILL.md 附录")
    
    print()


if __name__ == '__main__':
    main()
