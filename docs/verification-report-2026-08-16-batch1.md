# 复验报告 批1（2026-08-16）— 6篇评测

基准日 2026-08-16。所有修改建议附来源URL；无法核实项标注「截至2026-08-16」。

## cursor-review.astro
### ✅ 验证通过
- Pro $20/mo ✓（https://cursor.com/pricing）
- Hobby 免费层存在、无需信用卡 ✓（https://cursor.com/pricing）
- Teams $40/user/mo 价格 ✓，但计划名已从 Business 改为 Teams
- GitHub Copilot $10/mo individual、$19/mo business ✓
- Windsurf Pro $20/mo ✓（2026年3月改价后）
- VS Code 分支、全量扩展生态 ✓
- 新档位 Pro+ $60/mo、Ultra $200/mo 存在（文章未提，可补充）

### 🔧 需要修改
1. 定价表「Hobby: 2,000 completions/mo, 50 premium AI requests」→「Hobby：有限的 Agent 请求与 Tab 补全（官方未公布具体数字）」（cursor.com/pricing）
2. 定价表「Pro: 500 premium AI requests/mo」→「Pro：无限 Tab 补全 + 每月 $20 模型用量额度，超出按需计费」（cursor.com/pricing）
3. 定价表「Business $40/user/mo」→「Teams $40/user/mo（含集中计费、隐私模式、SSO）」（cursor.com/pricing）
4. 「using Claude Opus 4, GPT-5, or Cursor's large model」→「Claude Opus 4.8（2026年6月4日）、GPT-5.6（2026年7月9日上线 Cursor）或 Cursor 与 xAI 合作训练的 Grok 4.5（2026年7月8日）」
5. FAQ 中「500 premium AI requests per month」同第2条处理
6. 建议补充：2026年7月 xAI 已收购/深度绑定 Cursor（latent.space/p/ainews-spacexai-launches-grok-45）

### ⚠️ 无法确认
- 「2,000 completions/mo」「50 premium requests」官方不公布免费层配额（截至2026-08-16）
- 「tab completion 30-40% faster」无公开基准
- 「burst onto the scene in 2024」Cursor 实际2023年发布

## claude-review.astro
### ✅ 验证通过
- 200K context window（Free/Pro/Max）✓（anthropic.com/pricing）
- Pro $20/mo ✓（anthropic.com/pricing）
- Enterprise 定制 ✓
- 免费层存在 ✓

### 🔧 需要修改
1. 「Claude Opus 4 (旗舰), Claude 3.5 Sonnet, Claude 3.5 Haiku」→「2026年8月官方最新模型为 Opus 5、Sonnet 5、Fable 5、Haiku 4.5；Opus 4.8/Sonnet 4.6 等为上一代」（anthropic.com/pricing）
2. 定价表「Team $30/user/mo」→「Team Standard $25/席/月（年付$20）、Team Premium $125/席/月（年付$100）；另有个人档 Max 5x $100/mo、Max 20x $200/mo」
3. 免费层「Limited messages with Claude 3.5 Haiku」→「免费层使用轻量模型（当前轻量级为 Haiku 4.5）」（anthropic.com/pricing）
4. 正文/FAQ 所有「Opus 4 访问」→「Opus 5（Pro/Max 可用）」
5. 对比表「Gemini 2.0」→「Gemini 3.1 Pro（Gemini 3 于2025年11月18日发布）」，「$19.99/mo Google One AI Premium」计划名改为 Google AI Pro（价格不变）
6. 正文「Opus 4 commands a premium」→「Opus 5 $5/$25 每百万 tokens（输入/输出）、Sonnet 5 $2/$10（首发价）、Haiku 4.5 $1/$5」

### ⚠️ 无法确认
- 免费层具体模型型号（官方未明示）
- 「盲测62%编辑偏好 Claude」为本站自测数据

## chatgpt-review.astro
### ✅ 验证通过
- Plus $20/mo ✓（openai.com/chatgpt/pricing/）
- Pro 档存在 ✓（现为 $100 与 $200 两档）
- Advanced Voice Mode、GPT Store、联网搜索、代码执行 ✓

### 🔧 需要修改
1. 「GPT-5 (旗舰)」→「旗舰为 GPT-5.6 Sol（2026年7月9日上线 ChatGPT）；另有 Luna（免费/Go 默认，2026年8月6日起）、Terra（Work/Codex）」
2. 「GPT-4o (fast/efficient)、GPT-4o mini (free tier)」→「GPT-4o 系列已退出当前产品线；免费层现为 GPT-5.6 Luna + GPT-5 Thinking Mini」
3. 免费层「GPT-4o access with reasonable rate limits」→「免费层：GPT-5.6 Luna 无限文本对话，上传/语音/深度研究受限」
4. 「128K token context window」→「GPT-5.6 推理上下文：Go/Plus 256K、Pro 400K（GPT Instant 54K/128K）」
5. **「DALL-E 4」全部出现处（约7处）→「GPT Image 2（2026年4月21日发布，消费品牌名 ChatGPT Images 2.0）；DALL-E 4 不存在，DALL-E 2/3 已于2026年5月12日从 API 移除」**
6. 「Pro plan at $200/month for unlimited access」→「Pro 现有两档：$100/月（5倍用量）与 $200/月（20倍用量）」
7. 「Team plan at $30/user/month (annual)」→「Team 已于2026年4月2日更名 Business：$20/席/月（年付）或 $25（月付）」
8. 对比表「Claude Opus 4」→「Claude Opus 5」；「Gemini 2.0」→「Gemini 3.1 Pro」；「128K vs 200K」→「GPT-5.6 推理上下文最高400K，Claude 200K，Gemini AI Pro 1M」
9. FAQ「What's new」中 GPT-5 描述整体更新为 GPT-5.6

## midjourney-review.astro
### ✅ 验证通过
- 定价四档全部正确：Basic $10/mo（3.3h）、Standard $30/mo（15h+无限Relax）、Pro $60/mo（30h+Stealth）、Mega $120/mo（60h），年付8折
- 无免费层、无免费试用 ✓
- sref（V7引入）与 cref 功能存在 ✓

### 🔧 需要修改
1. 「V7, released in early 2026」→「V7 于 2025年4月4日发布（alpha）」（techcrunch.com/2025/04/04/midjourney-releases-v7）
2. 「Midjourney V7 是当前模型/当前默认」→「2026年8月默认模型为 V8.1（2026年6月11日起为默认），最新为 V8.2（2026年7月24日）；V8 于2026年3月17日发布 alpha」
3. 「operates exclusively through Discord」及「No native web app or desktop client」「Discord-only interface」全部 →「Midjourney 现提供完整 Web 应用（midjourney.com），Discord 仍是可选入口」
4. FAQ「Does Midjourney have a web interface? No…」→ 整条重写为「有，Web 应用已成熟，Discord 非必需」
5. 「Stable Diffusion 4」对比列 →「Stable Diffusion 4 不存在（截至2026-07-20，Stability 官方无发布记录）；最新开源为 SD 3.5（2024年10月）」
6. 「DALL-E 4」对比列 →「GPT Image 2（DALL-E 4 不存在）」
7. 对比表标题「Midjourney V7」→「Midjourney V8.1」
8. 正文「with the release of V7 in early 2026」→「V7（2025年4月）之后，V8.1 已于2026年6月成为默认模型」

### ⚠️ 无法确认
- 「V7 比 V6 快约30%」无官方量化来源，建议弱化措辞或删数字
- 「sref 生成50张图全部保持视觉一致性」为本站测试数据

## bolt-review.astro
### ✅ 验证通过
- 由 StackBlitz 开发 ✓
- 浏览器内运行（WebContainers）、Supabase 集成、Clerk 认证、一键部署 ✓
- 免费层存在 ✓

### 🔧 需要修改
1. 定价全表：→「2026年已从 prompts 计费改为 token 计费：Free 100万 tokens/月（每日30万上限）；Pro $25/月（1000万 tokens，无每日上限，可结转）；Teams $30/席/月（1000万 tokens 共享工作区）；Enterprise 定制」（nocode.mba/articles/bolt-pricing-2026）
2. FAQ「Free (100 prompts/month)、Pro $20/mo (500 prompts)、Teams $50/mo (2,000 prompts)」同上更新
3. 「Pro at $20/month is reasonably priced」「Teams at $50/month for up to 5 users」→ 更新为 $25 / $30/席
4. 「Enterprise pricing with self-hosted options starts around $200/month」→ 删除价格猜测，改为「Enterprise 定制（官方未公开起价）」（bolt.new）
5. 表格下注释「Prompts count all generations…」→ 改为 token 消耗说明
6. 品牌名「Bolt.new」→ 官方现称「Bolt」（域名 bolt.new 不变）

### ⚠️ 无法确认
- 「Next.js 15」具体支持版本，建议删版本号
- 「全栈应用60-90秒生成」为本站测试数据

## runway-review.astro（重点，过时最严重）
### ✅ 验证通过
- Gen-3 Alpha 于2024年6月17日发布（作为历史事实正确）
- 浏览器运行、无需本地 GPU ✓
- 内置编辑器功能仍存在 ✓

### 🔧 需要修改
1. **旗舰模型**（全文约17处 Gen-3 Alpha，含 JSON-LD description、FAQ「What is Gen-3 Alpha?」整条、h2 标题「Gen-3 Alpha — Video Quality and Capabilities」、正文多处）→ **旗舰为 Gen-4.5（2025年12月1日发布，Artificial Analysis 文生视频榜第一，Elo 1247）；Gen-4 于2025年3月31日发布；Gen-3 Alpha 已是两代前的模型**
2. FAQ「What is Gen-3 Alpha?」整条 → 改为「What is Gen-4.5?」：Runway 旗舰模型，支持文生视频/图生视频/视频生视频，原生音频生成（2025年12月宣布）、物理准确运动、References 角色与世界一致性、最高4K输出
3. 定价表 →「Free 125一次性 credits（非5/月）；Standard $12/月（年付）/$15（月付）625 credits；Pro $28/$35，2,250 credits；Unlimited 已更名 Max：$76/$95，9,500 credits + Explore Mode + 1个月额度结转；Enterprise 定制」（runwayml.com/pricing）
4. FAQ 定价条（"5 credits/month, 125 credits, 500 credits"）同上更新
5. 「Text-to-video costs ~1 credit per 5-second clip」→「Gen-4.5 视频 60 credits/5秒（12 credits/秒）；Gen-4 图像 8 credits/张」
6. 「Enterprise: Up to 4K」→「Standard 及以上已含 4K 放大；Enterprise 为定制 credits、SSO、工作区分析」
7. 功能描述「generate 5-10 second clips…quality can degrade past 15 seconds」→「Gen-4.5 按5秒段计费生成，支持原生音频、角色/世界一致性（References）、相机控制」
8. **Sora 对比（FAQ + 正文 + 结论）**：「Sora has the edge on pure visual fidelity」→「Sora 2 已于2026年4月26日停服（API 至2026年9月24日）；当前主要对比对象为 Google Veo 3.1、Kling 3.0、Seedance 2.0（其中 Kling 3.0、Veo 3.1 已入驻 Runway 平台）」（openai.com/index/sora-2）
9. 「Pika is cheaper for text-to-video」→ 保留 Pika 作为替代，但补充 Kling/Veo 对比现状
10. 「Enterprise pricing…typically starts around $200/month」→ 删除价格猜测，改为「定制报价」
11. 正文「In 2026, Runway also added multi-frame generation, extended clip durations, and better camera motion control」→ 重写为 Gen-4.5/Gen-4 的能力时间线（2025-03 Gen-4、2025-12 Gen-4.5、2026-01 Runway 4.5 更新）

### ⚠️ 无法确认
- 「编辑器能处理约80%常见剪辑任务」为主观评估
- Enterprise 起价（官方不公开）
