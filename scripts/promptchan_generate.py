#!/usr/bin/env python3
"""
PromptChan AI 图像生成脚本
"""

import argparse
import base64
import json
import os
import sys
from datetime import datetime
from pathlib import Path

import requests


def get_base_url():
    """获取基础 URL"""
    return os.environ.get('PROMPTCHAN_BASE_URL', 'https://promptchan.com')


def generate_image(api_key, prompt, negative_prompt='', style='Cinematic',
                   poses='Default', filter='Default', detail=0,
                   quality='Ultra', creativity=50, image_size='512x768',
                   seed=-1, restore_faces=False):
    """
    生成图像
    
    Args:
        api_key: API Key
        prompt: 正向提示词
        negative_prompt: 负向提示词
        style: 艺术风格
        poses: 姿势
        filter: 滤镜
        detail: 细节级别 (-2 到 2)
        quality: 质量等级 (Ultra/Extreme/Max)
        creativity: 创意程度 (30/50/70)
        image_size: 图像尺寸
        seed: 随机种子
        restore_faces: 人脸修复
    
    Returns:
        dict: 包含 image 和 gems 的响应
    """
    url = f"{get_base_url()}/api/external/create"
    
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json'
    }
    
    payload = {
        'prompt': prompt,
        'style': style,
        'poses': poses,
        'filter': filter,
        'detail': detail,
        'quality': quality,
        'creativity': creativity,
        'image_size': image_size,
        'seed': seed,
        'restore_faces': restore_faces
    }
    
    if negative_prompt:
        payload['negative_prompt'] = negative_prompt
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        response.raise_for_status()
        result = response.json()
        
        if 'error' in result:
            print(f"错误：{result['error']}", file=sys.stderr)
            sys.exit(1)
        
        return result
    except requests.exceptions.Timeout:
        print("错误：请求超时（120 秒）", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            print("错误：API Key 无效", file=sys.stderr)
        elif e.response.status_code == 402:
            print("错误：Gems 不足，请充值", file=sys.stderr)
        else:
            print(f"错误：HTTP {e.response.status_code}", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"错误：{e}", file=sys.stderr)
        sys.exit(1)


def save_image(image_base64, output_path):
    """
    保存图片
    
    Args:
        image_base64: Base64 编码的图片
        output_path: 输出路径
    """
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    image_data = base64.b64decode(image_base64)
    with open(output_path, 'wb') as f:
        f.write(image_data)
    
    print(f"图片已保存：{output_path}")


def main():
    parser = argparse.ArgumentParser(description='PromptChan AI 图像生成工具')
    parser.add_argument('--prompt', '-p', required=True, help='正向提示词')
    parser.add_argument('--negative-prompt', '-n', default='', help='负向提示词')
    parser.add_argument('--style', '-s', default='Cinematic', 
                       choices=['Cinematic', 'Anime', 'Hyperreal', 'Hyperanime', 
                               'K-Pop', 'Fur', 'Furtoon', 'Render XL+', 
                               'Illustration XL+', 'Anime XL', 'Anime XL+', 
                               'Hardcore XL', 'Cinematic XL', 'Photo XL+', 
                               'Hyperreal XL+'],
                       help='艺术风格')
    parser.add_argument('--poses', default='Default', help='姿势')
    parser.add_argument('--filter', '-f', default='Default',
                       choices=['Default', 'Cyberpunk', 'VHS', 'Manga', 
                               'Flash', 'Analog', 'Professional', 'Cinematic', 
                               'Studio', 'Polaroid', 'Vintage'],
                       help='滤镜')
    parser.add_argument('--detail', type=int, default=0, help='细节级别 (-2 到 2)')
    parser.add_argument('--quality', '-q', default='Ultra',
                       choices=['Ultra', 'Extreme', 'Max'],
                       help='质量等级')
    parser.add_argument('--creativity', '-c', type=int, default=50,
                       choices=[30, 50, 70],
                       help='创意程度')
    parser.add_argument('--image_size', default='512x768',
                       choices=['512x512', '512x768', '768x512'],
                       help='图像尺寸')
    parser.add_argument('--seed', type=int, default=-1, help='随机种子')
    parser.add_argument('--restore_faces', action='store_true', 
                       help='人脸修复（仅写实风格）')
    parser.add_argument('--api-key', required=True, help='PromptChan API Key')
    parser.add_argument('--output', '-o', type=str, help='输出路径')
    
    args = parser.parse_args()
    
    # 默认输出路径
    if not args.output:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        args.output = f"output/promptchan_{timestamp}.png"
    
    print(f"正在生成图片...")
    print(f"提示词：{args.prompt[:80]}{'...' if len(args.prompt) > 80 else ''}")
    print(f"风格：{args.style}")
    print(f"姿势：{args.poses}")
    print(f"滤镜：{args.filter}")
    print(f"质量：{args.quality}")
    print(f"尺寸：{args.image_size}")
    
    result = generate_image(
        api_key=args.api_key,
        prompt=args.prompt,
        negative_prompt=args.negative_prompt,
        style=args.style,
        poses=args.poses,
        filter=args.filter,
        detail=args.detail,
        quality=args.quality,
        creativity=args.creativity,
        image_size=args.image_size,
        seed=args.seed,
        restore_faces=args.restore_faces
    )
    
    save_image(result['image'], args.output)
    
    remaining_gems = result.get('gems', 0)
    print(f"剩余 Gems: {remaining_gems}")
    print("生成完成！")


if __name__ == '__main__':
    main()
