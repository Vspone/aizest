# 复验报告 批3（2026-08-16）— 5篇

基准日 2026-08-16。所有修改建议附来源URL；无法核实项标注「截至2026-08-16」。

## runway-vs-kling.astro
### ✅ 验证通过
- Runway Free 125 credits、Standard $15/mo（625 credits）、Pro $35/mo（2,250 credits）→ runway.com/pricing
- Kling Standard $10/mo（660 credits）→ eesel/imagine.art/aitoolcurator 交叉确认
- Kling 由快手开发、最长15秒片段（Kling 3.0 官方 API 文档 3–15s）
- Runway 免费层 720p 带水印、Pro 含编辑器访问
- 主观评测结论方向合理，无需改

### 🔧 需要修改
1. "Runway...offers a mature ecosystem with Gen-3 Alpha and Turbo models" → "Gen-4.5（2025年12月发布，Artificial Analysis T2V基准第1名，1247 Elo）和 Gen-4 Turbo"（runway.com/research/introducing-runway-gen-4.5）
2. "Runway's Gen-3 Turbo offers sub-10-second generation times" → "Gen-4 Turbo 为现行高速模型（Gen-3 Alpha Turbo 已于 2026-07-30 从 API 下线）"（releasebot.io/updates/runwayai）
3. "Kling 2.0, released in early 2026" → "Kling 2.0 于 2025 年 4 月发布；Kling 3.0 于 2026 年 2 月发布（3.0 Turbo 于 2026-06-17 上线）"（en.wikipedia.org/wiki/Kling_AI）
4. "Its 30fps output at 1080p delivers cinematic smoothness" → "Kling 3.0 支持原生 4K 60fps（2026-04-23 API 支持原生4K）"（kling.ai/document-api/apiReference/updateNotice）
5. "Pricing: Free (66 credits/mo) · $10/mo (Basic) · $22/mo (Pro) · $56/mo (Max)" → "Free（66 credits/日，24小时过期）· Standard $10/mo（660 credits）· Pro $37/mo（3,000 credits）· Premier $92/mo（8,000）· Ultra $180/mo（26,000）；'Max' 档已取消"（eesel.ai/blog/kling-ai-pricing）
6. "Runway...$95/mo (Unlimited)" → "Unlimited 已调整为 Max $95/mo（年付$76）= 9,500 credits + 1个月credit结转，并非'无限生成'"（runway.com/pricing）
7. 定价表 "Free: 125 credits/mo" → "125 credits（一次性，官方注明 one-time、不过期）"（runway.com/pricing）
8. 定价表 "Kling Pro $22/mo — 660 credits" → "$37/mo — 3,000 credits"；"Max $56/mo — 2,000 credits" → "Premier $92/mo — 8,000 credits / Ultra $180/mo — 26,000 credits"（eesel.ai/blog/kling-ai-pricing）
9. "At $22/month, Kling Pro offers 1080p...up to 15-second clips" → "$37/month（3,000 credits）"（imagine.art/blogs/kling-ai-pricing）
10. "Kling's Max tier at $56/month delivers 2,000 credits against Runway's Unlimited tier at $95/month" → "Kling 最高档 Ultra $180/mo（26,000 credits）对比 Runway Max $95/mo（9,500 credits）"（eesel.ai + runway.com/pricing）
11. "Runway Gen-3 Turbo model, launched in late 2025" → "Gen-3 Alpha Turbo 实际于 2024年8–10月发布；建议改为'Runway Gen-4.5（2025年12月1日发布）'"（provideocoalition.com/runway-gen-3-alpha-turbo-7x-faster...）
12. 表格 "Max Output: 10 seconds (Gen-3), 5 seconds (Turbo)" → "Gen-4.5 最长 10秒（5/8/10可选）；Kling 3.0 最长 15秒"
13. "budget $57/month total (Kling Pro + Runway Standard)" → 按新价：Kling Pro $37 + Runway Standard $15 = $52/month（月付）
14. "Kling 2.0...extended generation length (up to 15 seconds)" → 15秒是 2.5/3.0 才支持，改为 "Kling 3.0 支持最长15秒、多镜头（最多6个分镜）"

### ⚠️ 无法确认
- Runway Gen-4.5 时长上限按"最长约10秒"处理（教程显示5/8/10秒可选）
- Kling 免费层额度历史上变动，多数来源为每日66 credits，建议标注日期

## heygen-vs-synthesia.astro
### ✅ 验证通过
- HeyGen Creator $29/mo（月付，年付$24）、175+语言、免费层带水印 ✓
- HeyGen 有 voice cloning、TalkingPhoto、实时流媒体（LiveAvatar）✓
- Synthesia Creator $89/mo、SOC 2 Type II、240+虚拟人（Enterprise）、160+语言 ✓
- 定性判断方向合理 ✓

### 🔧 需要修改
1. "100+ avatars"（引言、Overview、表格、Test 1）→ 官方2026年为 "700+ avatars"（heygen.com/blog/best-ai-avatar-generators）
2. "Synthesia simply doesn't offer voice cloning as of 2026"（Test 2 整段）→ 错误。Synthesia 官方提供 voice cloning（所有计划可用）。改为 "Synthesia 自2023年起提供声音克隆，但克隆声音仅支持32种语言，广度不及 HeyGen 的175+"（synthesia.io/features/ai-voice-cloning）
3. 表格 "Voice Cloning: Synthesia ⭐⭐ Not available" → "⭐⭐⭐ 可用（全计划，32种语言）"
4. 表格 "Real-Time Streaming: Synthesia ⭐⭐ Not available" → "⭐⭐ Interactive Avatars（2025年推出，交互式视频；非HeyGen式实时对话）"（synthesia.io/features/avatars/interactive-avatars）
5. "Synthesia's 'free demo'...cannot export full-resolution videos" → "Synthesia 现提供 Basic 免费计划（10分钟/月、9个AI虚拟人、带水印）；无水印导出需 Starter 起"（synthesia.io/pricing）
6. "HeyGen's Creator plan ($29/mo) undercuts Synthesia's Starter plan ($30/mo)" → Synthesia Starter 实为 $29/mo（月付，年付$18），与 HeyGen Creator 同价，不存在"undercut"（synthesia.io/pricing）
7. "Both platforms' Business/Creator plans are priced identically at $89/month" → 过时：HeyGen Business 现为 $149/mo + $20/seat（2026年1月起另有 Pro $99）；Synthesia Creator $89/mo（heygen.com/blog/heygen-january-2026-release）
8. 定价表 "HeyGen: $89/mo — 30 min credits... 100+ avatars" → "$149/mo + $20/seat（Business）— 1,500 credits、4K、700+ avatars；新增 Pro $99/mo（2,000 credits）"
9. 定价表 "Synthesia: $30/mo — 10 min, 140+ avatars, 160+ languages" → "$29/mo（年付$18）— 10分钟、125+ avatars；Creator $89（年付$64）— 30分钟、180+ avatars（240+ 仅 Enterprise）"
10. FAQ JSON-LD "HeyGen plans start at $24/month (Creator), $49/month (Business)" → $49 无此档（Pro 为 $99、Business $149）；改为 "$29/mo Creator（年付$24）、$99/mo Pro、$149/mo Business 起"
11. "In early 2026, HeyGen launched real-time AI avatar streaming" → "2025年，HeyGen 将 Interactive Avatar 升级为 LiveAvatar 实时流媒体平台"（help.heygen.com/articles/12758516-introducing-liveavatar）
12. "Synthesia achieved SOC 2 Type II certification in 2025" → 公开公告时间戳为 2023年4月。改为 "Synthesia 于2023年通过 SOC 2 Type II 审计并持续保持（另有 ISO 27001、ISO 42001）"（synthesia.noticeable.news）
13. "HeyGen's avatar library expansion from roughly 80 avatars in early 2025 to 100+ by mid-2026" → "2026年 HeyGen 官方库已扩至 700+ avatars（约 Synthesia 平台总量的3倍，而非'不到一半'）"
14. FAQ "Synthesia supports 140+ languages" → 官方现为 "160+"（synthesia.io/pricing）
15. 表 "Language Support: HeyGen 175+ / Synthesia 160+" ✅ 无需改

### ⚠️ 无法确认
- Synthesia "160+ languages" 个别第三方称140+，以官方定价页"160+"为准

## best-ai-writing-tools-2026.astro
### ✅ 验证通过
- ChatGPT Free / Plus $20/mo ✓
- Grammarly Free / Pro $12/mo（年付）✓
- Jasper 营销文案定位、ChatGPT 全能定位 定性合理 ✓

### 🔧 需要修改
1. "Jasper...Pricing: $39/mo" → "Creator $49/mo（年付$39）；Pro $69/mo（年付$59）"（demandsage.com/jasper-ai-pricing）
2. "Copy.ai...Pricing: Free / $36/mo" → 免费层已不对新用户开放；现行 Chat 计划 $29/mo（年付$24，5席位），产品已转型为 GTM AI 平台（contentpen.ai/blog/copy-ai-pricing）
3. "Writesonic...Pricing: $16/mo" → $16 档早已取消；2026年最低档 Lite $49/mo（年付$39），产品已转型为 AI SEO/GEO 平台（Starter $99/$79、Basic $249/$199）（hyperwriteai.com/blog/writesonic-pricing）
4. FAQ "Writesonic offers the best value for money at $16/mo" → "$49/mo 起（Lite，年付$39）"
5. FAQ "several other tools including Copy.ai and Writesonic have free plans" → Copy.ai 免费层2026年起不再对新用户开放
6. 建议补充：列表缺 Claude（Anthropic，Pro $20/mo，2026年写作/推理主力）与 Google Gemini；Copy.ai/Writesonic 已非传统"写作工具"，建议调整定位描述或替换（suprmind.ai/hub/claude/pricing）

### ⚠️ 无法确认
- 本站自评分数（4.8/4.6/4.5/4.3/4.4）为主观评分，建议标注评测日期

## best-ai-coding-tools-2026.astro
### ✅ 验证通过
- Cursor Free（Hobby）/ Pro $20/mo ✓
- GitHub Copilot Free / Pro $10 / Business $19/user ✓（docs.github.com）
- v0.dev Free / Premium $20/mo ✓（v0.app/docs/pricing）
- Replit Free / Core $25/mo（月付；年付$20）✓
- 各工具定位描述定性准确 ✓

### 🔧 需要修改
1. "Claude Code...Pricing: Pay-per-use / Subscription available" → 精确化："包含于 Claude Pro $20/mo（年付$17）、Max $100/$200 订阅；或 API 按 token 计费（Team Standard 不含 Claude Code）"（morphllm.com/claude-code-pricing）
2. "v0.dev...Pricing: Free / $20/mo" → 官方文档注明 Premium $20 "正在停售、不再向新用户提供"，替代档为 Plus $30/user/mo。改为 "Free / Plus $30/user/mo（Premium $20 停售中）"（v0.app/docs/pricing）
3. "GitHub Copilot...$10/mo individual / $19/mo business" ✅ 数字正确，建议加注："2026-06-01 起 Copilot 全面转为 usage-based AI Credits 计费（订阅价不变，额度按 credits 计量）"（github.blog）
4. 建议补充：Windsurf（Cognition 旗下，2026-03-19 调价后 Pro $20/mo、Max $200/mo）与 OpenAI Codex（含于 ChatGPT Plus $20）（cloudzero.com/blog/windsurf-pricing）

### ⚠️ 无法确认
- Cursor 2025年6月起"订阅价≈每月模型用量额度"模式，实际支出可能超出订阅价（机制说明而非数字错误）

## best-ai-video-generators-2026.astro
### ✅ 验证通过
- Runway Free / Standard $15/mo ✓
- Synthesia $29/mo（Starter 月付）✓
- HeyGen Creator 月付 $29（年付$24）✓
- Pika Free / Standard $10/mo（月付，年付$8）✓
- CapCut 免费版仍存在 ✓

### 🔧 需要修改
1. "Runway Gen-3 Alpha is the most comprehensive AI video platform" → "Runway Gen-4.5（2025年12月发布，AA基准第1）"（runway.com/research/introducing-runway-gen-4.5）
2. FAQ+正文 "Synthesia...over 160 realistic AI presenters across 140+ languages" → 官方为 "240+ AI 虚拟人"、"1,000+ voices"、"160+ languages"（160+ 是语言数而非虚拟人数）（synthesia.io/pricing）
3. 表格 "Synthesia ✅ 160+"（AI Avatars 列）→ "✅ 240+（平台）/125+（Starter）/180+（Creator）"
4. "HeyGen...Pricing: Free / $24/mo" → "Free / $29/mo（月付；$24 为年付折后价）"（heygen.com/blog/best-ai-avatar-generators）
5. "Its AI translation feature preserves your voice and lip movements in 50+ languages" → "175+ languages（官方2026年1月更新为177+种语言和方言）"（heygen.com/blog/heygen-january-2026-release）
6. "CapCut...Pricing: Free" 及 "rivals premium tools" → 2026年 CapCut 为三层：Free / Standard $9.99/mo（移动端去水印）/ Pro $19.99/mo 或 $179.99/yr（4K+完整AI工具）；免费版导出部分模板带水印。改为 "Free（基础剪辑）/ Standard $9.99/mo / Pro $19.99/mo"（gamsgo.com/blog/capcut-pricing）
7. 建议补充：列表缺 Kling 3.0（2026年2月发布）、OpenAI Sora 2、Google Veo 3/3.1——均为2026年最重要视频工具（en.wikipedia.org/wiki/Kling_AI）

### ⚠️ 无法确认
- CapCut 各渠道价格差异较大（官网约$7.99–9.99 vs App Store $13.99–19.99），建议写区间或标注"以官网为准"
