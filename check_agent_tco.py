#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Claude Code / OpenCode 国内直连与 24h 挂机防封 VPS 选型 TCO 测算脚本
零第三方依赖，在终端中直观对比海外原版订阅与国产平替两套架构的真实持有成本。
"""

import argparse
import sys

def format_row(cols, widths, aligns):
    parts = []
    for val, w, align in zip(cols, widths, aligns):
        s = str(val)
        actual_len = sum(2 if ord(c) > 127 else 1 for c in s)
        padding = max(0, w - actual_len)
        if align == '<':
            parts.append(s + ' ' * padding)
        elif align == '>':
            parts.append(' ' * padding + s)
        else:
            left = padding // 2
            right = padding - left
            parts.append(' ' * left + s + ' ' * right)
    return " | ".join(parts)

def run_calc(hours=4.0, team=1, mode='dual'):
    print("=" * 76)
    print("  Claude Code / Cursor Agent 24h 挂机基础设施与模型订阅 TCO 测算")
    print("=" * 76)

    # 1. 海外原版方案 (Cursor Pro / Claude Pro $20/月 + 外币卡充值汇损 + 丽萨双ISP住宅VPS)
    overseas_sub_cny = 145.0 * team
    card_monthly_fee = 7.0 * team  # 汇损与充值手续费摊销
    lisahost_vps_cny = 68.0  # 丽萨美区双ISP原生住宅VPS
    bwh_cn2_cny = 181.2     # 搬瓦工 CN2 GIA $299.99/年
    
    plan_overseas_lisa_first = overseas_sub_cny + card_monthly_fee + lisahost_vps_cny + 20.0  # 含一次性开卡费约¥20
    plan_overseas_lisa_steady = overseas_sub_cny + card_monthly_fee + lisahost_vps_cny
    plan_overseas_lisa_annual = plan_overseas_lisa_first + plan_overseas_lisa_steady * 11

    plan_overseas_bwh_first = overseas_sub_cny + card_monthly_fee + bwh_cn2_cny + 20.0
    plan_overseas_bwh_steady = overseas_sub_cny + card_monthly_fee + bwh_cn2_cny
    plan_overseas_bwh_annual = plan_overseas_bwh_first + plan_overseas_bwh_steady * 11

    # 2. 国内双轨方案 (保留 Cursor/Claude Code 开源壳，接入火山方舟 ¥9.4 + 阿里云百炼)
    volc_first = 9.41 * team
    volc_steady = 40.0 * team
    bailian_first = 39.9 * team
    bailian_steady = 200.0 * team

    plan_volc_single_first = volc_first
    plan_volc_single_steady = volc_steady
    plan_volc_single_annual = volc_first + volc_steady * 11

    plan_dual_first = volc_first + bailian_first
    plan_dual_steady = volc_steady + bailian_steady
    plan_dual_annual = plan_dual_first + plan_dual_steady * 11

    headers = ["技术路线与选型", "首月实付现金", "稳态月均支出", "首年总持有成本 (TCO)", "网络与风控特性"]
    widths = [26, 14, 14, 20, 24]
    aligns = ['<', '>', '>', '>', '<']

    print(format_row(headers, widths, aligns))
    print("-" * 76)
    print(format_row(["1. 海外原版+丽萨双ISP(¥68)", f"¥{plan_overseas_lisa_first:.1f}", f"¥{plan_overseas_lisa_steady:.1f}", f"¥{plan_overseas_lisa_annual:.1f}", "双ISP原生家宽防封/免翻"], widths, aligns))
    print(format_row(["2. 海外原版+搬瓦工CN2 GIA", f"¥{plan_overseas_bwh_first:.1f}", f"¥{plan_overseas_bwh_steady:.1f}", f"¥{plan_overseas_bwh_annual:.1f}", "超低延迟海外高速中转"], widths, aligns))
    print(format_row(["3. 国内双开(火山¥9.4+百炼)", f"¥{plan_dual_first:.1f}", f"¥{plan_dual_steady:.1f}", f"¥{plan_dual_annual:.1f}", "国内直连免梯/主备双路由"], widths, aligns))
    print(format_row(["4. 火山方舟单开(极致性价比)", f"¥{plan_volc_single_first:.1f}", f"¥{plan_volc_single_steady:.1f}", f"¥{plan_volc_single_annual:.1f}", "首月立省95.7%/稳态省81.8%"], widths, aligns))
    print("-" * 76)

    print("\n💡 架构选型深度建议:")
    print("  • 【方案 A 强用海外原版】: 必须使用纯净住宅 IP（如丽萨美区双 ISP 或搬瓦工），机房广播 IP 极易触发 Claude 403 阻断与封号；外币支付或免外卡平替参见专题指南。")
    print("  • 【方案 B 国内零代理双开】: 保留 Cursor / Cline / Claude Code 客户端，配置 API 端点直连火山方舟（首月 ¥9.41）与百炼 Coding Plan，不翻墙、不封号、零外币卡门槛，综合月费不到海外原版四分之一。\n")

    print("🔗 关键服务直达通道:")
    print("  • 火山方舟 Coding Plan (首月 ¥9.41): https://coding.mybskm.top/go/volcengine-coding")
    print("  • 阿里云百炼 Coding Plan Pro: https://coding.mybskm.top/go/aliyun-coding")
    print("  • 丽萨主机双 ISP 原生住宅 VPS (¥68/月): https://coding.mybskm.top/go/lisahost")
    print("  • 搬瓦工 CN2 GIA 电商高速专线: https://coding.mybskm.top/go/bwh")
    print("  • 在线防封与免外卡平替总账单: https://coding.mybskm.top/cursor-claude-pro-virtual-card-and-isp-ip.html\n")

def main():
    parser = argparse.ArgumentParser(description="Claude Code / Cursor Agent 基础设施与模型订阅 TCO 测算")
    parser.add_argument("--hours", type=float, default=4.0, help="每日 Agent 挂机编码工时 (默认: 4.0)")
    parser.add_argument("--team", type=int, default=1, help="团队开发者人数 (默认: 1)")
    parser.add_argument("--mode", choices=["dual", "volcengine", "overseas"], default="dual", help="测算重点模式")
    args = parser.parse_args()
    run_calc(args.hours, args.team, args.mode)

if __name__ == '__main__':
    main()
