#!/usr/bin/env python3
"""
PromptChan AI - 查询余额和状态
"""

import argparse
import os
import sys

import requests


def get_base_url():
    return os.environ.get('PROMPTCHAN_BASE_URL', 'https://promptchan.com')


def get_status(api_key):
    """
    查询账户状态
    
    Args:
        api_key: API Key
    
    Returns:
        dict: 包含 gems 等信息的响应
    """
    url = f"{get_base_url()}/api/external/status"
    
    headers = {
        'x-api-key': api_key
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            print("错误：API Key 无效", file=sys.stderr)
        else:
            print(f"错误：HTTP {e.response.status_code}", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"错误：{e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description='PromptChan 账户状态查询')
    parser.add_argument('--api-key', required=True, help='PromptChan API Key')
    parser.add_argument('--json', action='store_true', help='以 JSON 格式输出')
    
    args = parser.parse_args()
    
    print("正在查询账户状态...")
    
    result = get_status(args.api_key)
    
    if args.json:
        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        gems = result.get('gems', 0)
        print(f"剩余 Gems: {gems}")
        print(f"说明：1 Gem = 1 张图片")
        
        if 'subscription' in result:
            sub = result['subscription']
            print(f"订阅状态：{sub.get('plan', 'Free')}")
            if sub.get('renewal_date'):
                print(f"续费日期：{sub['renewal_date']}")


if __name__ == '__main__':
    main()
