# Claude Code / OpenCode 国内直连配置与 24 小时挂机防封 VPS 选型指南（火山方舟 / 百炼双开 + 美区双 ISP 原生住宅 IP 实测）

在本地电脑或服务器上运行 **Claude Code**、**OpenCode**、**Cursor Agent** 或 **Cline** 进行自动化开发时，开发者面临两大最棘手的痛点：
1. **海外原版风控阻断**：使用普通机房 VPS 访问 Anthropic / OpenAI API 时，经常遭遇 Cloudflare Turnstile 验证拦截、403 访问被拒绝 甚至直接封禁账号；外币卡充值更是经常被拒付；
2. **本地合盖断线**：本地笔记本电脑无法 24 小时常驻挂机运行长链 Agent 任务。

本项目提供经过大量实测验证的**双轨解决方案**：既能满足坚持使用海外原版的防封号网络拓扑，又能提供 100% 国内免代理直连的超高性价比平替方案。

---

## ⚡ 双轨架构对比：海外防封专线 vs 国产平替双开

| 评估维度 | 方案 1：海外原版 + 丽萨双 ISP 原生家宽 VPS (防封) | 方案 2：国内直连双开 (火山方舟 ¥9.4 + 百炼) |
| :--- | :--- | :--- |
| **首月实付现金** | **¥240.0** (含 $20 订阅 + 虚拟卡开卡费 + VPS 首月) | **¥49.31** (火山 ¥9.41 + 百炼 ¥39.9) |
| **稳态月均摊销** | **¥220.0 / 月** ($20 汇率折算 + 丽萨 ¥68/月 + 汇损) | **¥40.0 ~ ¥240.0 / 月** (按需搭配) |
| **网络环境依赖** | 需配置原生美区双 ISP 纯净家宽住宅 IP | **100% 国内直连**，无需任何网络代理工具 |
| **支付方式门槛** | 需外币信用卡（或虚拟卡）并解决 KYC 与拒付 | **支付宝 / 微信**，支持国内增值税发票报销 |
| **封号风控概率** | 采用原生 Residential IP，风控等级最低 | **零封号风险**，官方正规合规企业级端点 |

---

## 🛠️ 本地 TCO 算账脚本

直接运行仓库内的零依赖 Python 脚本测算详细账单：

```bash
# 测算单人团队 4 小时工时下的 TCO
python3 check_agent_tco.py --hours 4 --team 1

# 或通过 PyPI 官方包执行
pipx run cn-coding-plan --hours 4 --team 1
```

---

## 🔧 24 小时常驻 Agent 搭建指南

### 路线 A：海外原版 24h 挂机节点 (丽萨双 ISP 或搬瓦工 CN2 GIA)

1. 选购一台 **丽萨主机美区双 ISP 原生住宅 IP VPS**（推荐 1核1G / ¥68/月）；若注重极致低延迟与高速传输，可选择 **搬瓦工 CN2 GIA 电商专线**；
2. 在 VPS 上配置 Node.js 20+ 与 Claude Code 运行环境；
3. 绑定外币卡或通过国内免外卡平替直连，完成 Anthropic Console 绑定并充值；
4. 通过 `systemd` 或 `tmux` 将 Claude Code 守护进程化，实现 24 小时全自动代码重构与挂机监控。

### 路线 B：国内零翻墙双开 (火山方舟 + 阿里云百炼)

1. 领取 **火山方舟 Coding Plan**（首月仅 ¥9.41，支持 DeepSeek-V4.1 / GLM-5.3 / Doubao 等模型）；
2. 备用配置 **阿里云百炼 Coding Plan Pro**，作为高峰期冗余切流；
3. 在本地 Cursor / Cline 或服务器环境变量中直接替换 Base URL：
   ```bash
   export OPENAI_BASE_URL="https://ark.cn-beijing.volces.com/api/v3"
   export OPENAI_API_KEY="your-volcengine-api-key"
   ```

---

## 🔗 官方正品通道与优惠入口

| 平台 / 服务 | 核心特性 | 官方链接 |
| :--- | :--- | :--- |
| **字节火山方舟 Coding Plan** | 首月 ¥9.41 / 免排队抢购 / 4大旗舰模型自由路由 | [火山方舟活动入口](https://coding.mybskm.top/go/volcengine-coding?src=gh_repo_cn_coding_plan) |
| **阿里云百炼 Coding Plan Pro** | 通义千问 Max / Coder / 极低延迟直连 / 官方配额保障 | [阿里云百炼入口](https://coding.mybskm.top/go/aliyun-coding?src=gh_repo_cn_coding_plan) |
| **丽萨主机 LisaHost** | 美区双 ISP 原生家宽纯净住宅 IP / 支付宝付款 / 海外防封首选 | [丽萨主机官网](https://coding.mybskm.top/go/lisahost?src=gh_repo_cn_coding_plan) |
| **搬瓦工 BandwagonHost** | CN2 GIA / 软银高端优化线路 / 海外 API 转发高速中枢 | [搬瓦工高速方案](https://coding.mybskm.top/go/bwh?src=gh_repo_cn_coding_plan) |
| **海外订阅防封与免外卡专题** | 算清海外订阅绑卡、住宅 IP 隐性成本与国内直连平替 | [防封与免外卡总账单](https://coding.mybskm.top/cursor-claude-pro-virtual-card-and-isp-ip.html) |
| **防拒付防封总账单专题** | 算清隐性成本与平替方案，在线交互算账 | [专题详情页](https://coding.mybskm.top/cursor-claude-pro-virtual-card-and-isp-ip.html) |

---

## 四仓互链：网络环境防风控与成本测算

| 仓库 | 用途 |
| --- | --- |
| [awesome-cn-coding-plan](https://github.com/cn-coding-bench/awesome-cn-coding-plan) | 编程订阅对比 |
| [crossborder-multi-shop-bom-calculator](https://github.com/cn-coding-bench/crossborder-multi-shop-bom-calculator) | 多店铺 BOM |
| [claude-code-cn-setup-and-vps-guide](https://github.com/cn-coding-bench/claude-code-cn-setup-and-vps-guide) | 开发环境与 VPS |
| [tiktok-cloudphone-vs-residential-isp-proxy](https://github.com/cn-coding-bench/tiktok-cloudphone-vs-residential-isp-proxy) | 云手机与住宅 IP |


## 📄 开源许可

本项目遵循 [MIT License](LICENSE) 开源协议。数据基于 2026-10-30 快照核验。
