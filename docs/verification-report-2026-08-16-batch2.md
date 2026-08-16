# 复验报告 批2（2026-08-16）— 5篇

基准日 2026-08-16。所有修改建议附来源URL；无法核实项标注「截至2026-08-16」。

## elevenlabs-review.astro
### ✅ 验证通过
- 免费层 Free $0/10,000字符 ✓（11k credits，TTS 1字符=1 credit）→ elevenlabs.io/pricing
- Creator $22/mo、Pro $99/mo 价格不变 ✓
- Enterprise 自定义 ✓
- 2022年成立 ✓
- Voice Design、Voice Guard、AI Dubbing、声音库、语音转语音功能均存在 ✓
- 年付2个月免费（Pro年付等效$82.50/mo）✓

### 🔧 需要修改
1. 定价表"Starter $5/mo / 30,000"→"Starter $6/mo（月付；年付等效$5/mo）/ 30,000"（elevenlabs.io/pricing）
2. 定价表"Creator 100,000字符"→"Creator $22/mo / 121,000 credits"（elevenlabs.io/pricing）
3. 定价表"Pro 500,000字符"→"Pro $99/mo / 600,000 credits"（elevenlabs.io/pricing）
4. 定价表缺档位：官方现为 Free/Starter/Creator/Pro/Scale $299（1.8M）/Business $990（6M）/Enterprise，补入 Scale 和 Business 两行（elevenlabs.io/pricing）
5. 定价表"Starter 1 Professional（克隆）"→"Starter 仅含 Instant Voice Cloning；Professional Voice Cloning（PVC）自 Creator 起"（elevenlabs.io/pricing）
6. 正文"The platform supports 32 languages"及 FAQ"supports 32 languages grouped into High-Fidelity...tiers"→"旗舰模型 Eleven v3 支持 70+ 语言（2026年2月 GA）；High-Fidelity/Standard 分层已废止"（elevenlabs.io/docs/overview/models）
7. "its latest Turbo v3 model delivers sub-200ms latency"→"低延迟模型为 Flash v2.5（约75ms）；旗舰为 Eleven v3（约1-2s、单次5,000字符上限），Turbo 已弃用"（invideo.io/blog/elevenlabs-ai-voice-models）
8. "Professional Voice Cloning...from as little as 1 minute of reference audio, though 10+ minutes yields..."→"PVC 官方最低要求 30 分钟音频，推荐 2-3 小时以获得最佳效果"（elevenlabs.io/docs/.../professional-voice-cloning）
9. "Instant Voice Cloning 2.0...from just 30 seconds"→"Instant Voice Cloning 官方推荐 1-2 分钟干净音频；'2.0' 命名未见于现行官方文档"（同上官方文档FAQ）
10. 正文"Enterprise custom pricing starts around $500/month"→删除或改为"Scale $299 起、Business $990，Enterprise 按需报价"（elevenlabs.io/pricing）
11. "2026年通过Zapier和Make推出低代码集成"→集成确实存在，但"2026年推出"无法证实，改为"现已提供 Zapier/Make 集成"（elevenlabs.io/agents/integrations/zapier）

### ⚠️ 无法确认
- "Creator 3 Professional / Pro 10 Professional 克隆槽位"数字：官方定价页未公布各档 PVC 数量（仅 Scale=3、Business=10），改为定性描述
- 评分4.6/5为主观评分

## synthesia-review.astro
### ✅ 验证通过
- Starter $29/mo、Creator $89/mo（月付）✓；年付 $18/$64 → synthesia.io/pricing
- "50,000+ businesses"与官方"50,000+ teams"一致 ✓
- Creator 30分钟/月 ✓；Enterprise 无限分钟+自定义头像+SAML/SSO ✓
- 2017年成立、伦敦总部 ✓
- SOC 2 Type II 合规 ✓
- 未使用分钟不结转 ✓

### 🔧 需要修改
1. "serving 50,000 businesses, including half of the Fortune 100"→"serving 50,000+ businesses（官方口径），including 70%+ of the Fortune 100"（firstmark.com/story/synthesia-surpasses-100m-arr...；synthesia.io/pricing）
2. 定价表缺免费层 → 补入"Basic（免费）：10分钟视频/月、9个AI头像、带水印"（synthesia.io/pricing）
3. 定价表"Starter...50+ avatars, 6 languages"→"Starter...125+ AI头像、3个个人头像、160+语言"（"6语言限制"已取消）（synthesia.io/pricing）
4. 定价表"Creator...all avatars"→"Creator...180+ AI头像、5个个人头像、API访问"（API 访问实为 Creator 档起，非 Enterprise 专属）（synthesia.io/pricing）
5. 全文"120+ languages"（共5处）→"160+ languages & voices"（synthesia.io/pricing）
6. "record 10-15 minutes...within approximately 24-48 hours"→"个人头像随 Starter/Creator 档提供；专业 Studio 头像为 $1,000/年付费附加项，处理最长10天"（synthesia.io/pricing）
7. 对比表"HeyGen 40+ languages"→"175+ languages"；"HeyGen $29/mo (10 min)"→"$29/mo（600 credits/月，按积分计费）"（help.heygen.com）
8. 对比表"Elai.io 65+ languages"→"75+ languages"；"Elai.io $29/mo (10 min)"→"约$23/mo（Creator档15分钟/月）"（elai.io/pricing）

### ⚠️ 无法确认
- "2-3分钟视频5-15分钟渲染完成"官方未公布基准
- "本地化成本削减80-90%"具体比例无法独立验证
- 评分4.4/5为主观评分（官方页 G2 4.7/5）

## cursor-vs-windsurf.astro
### ✅ 验证通过
- Cursor Pro $20/mo、Teams $40/user/mo ✓ → cursor.com/pricing
- Windsurf Pro $20/mo、Max $200/mo、Teams $40/user/mo ✓ → devin.ai/blog/windsurf-pricing-plans
- "March 2026 Windsurf调价：Pro $15→$20、积分制改为配额制" ✓ → nocode.mba/articles/windsurf-pricing
- "Windsurf的SWE-1.5自研模型" ✓
- 两者同为VS Code分支 ✓

### 🔧 需要修改
1. 收购表述："As of April 2026, Windsurf was reportedly acquired by Cognition"→"2025年7月14日，Cognition（Devin母公司）正式宣布收购Windsurf（非'据报'，已官方确认；此前2025年5月OpenAI曾洽谈30亿美元收购未果）"（cognition.com/blog/windsurf）
2. 定价表"Cursor Free：2,000 completions/mo, 50 premium requests"→"Hobby免费层：limited Agent requests + limited Tab completions（官方已不再公布具体数字）"（cursor.com/pricing）
3. "Cursor...expanded model support (adding Claude Opus 4, GPT-5)"→"持续跟进最新模型（截至2026年中Anthropic已发布Opus 5、GPT-5.x系列）"，避免写死过时版本号
4. 正文"Windsurf, built by Codeium"补充"现归属 Cognition（Devin）旗下，windsurf.com/pricing 已并入 Devin 定价体系"（windsurf.com/pricing）

### ⚠️ 无法确认
- "Windsurf 40+ built-in plugins"具体数字无法核实
- Cursor 4.7/5、Windsurf 4.4/5为主观评分
- 7项实测结论（Test 1-7）为主观测试

## claude-vs-deepseek.astro
### ✅ 验证通过
- Claude Pro $20/mo ✓（年付$17/mo）
- Claude 200K上下文（消费版）✓
- DeepSeek 免费网页聊天 ✓
- DeepSeek 为 High-Flyer 关联公司、open-weight（MIT许可）✓
- DeepSeek V4 为 MoE 架构 ✓（V4-Pro 1.6T总参/49B激活）

### 🔧 需要修改
1. "DeepSeek V4 provides a 128K token context window"（FAQ+正文表格+Test 4 共3处）→"DeepSeek V4提供1M token上下文（384K最大输出）；128K是上一代V3的参数"（benchlm.ai/deepseek/api-pricing）
2. "DeepSeek's V4 costs roughly $0.28 per million tokens"→"DeepSeek V4 Flash $0.14/百万输入、$0.28/百万输出；V4 Pro $0.435/$0.87（2026-05-31起75%折扣永久化）"（benchlm.ai/deepseek/api-pricing）
3. 定价表"Claude ~$15/M tokens (Opus) · ~$3/M (Sonnet)"及"~$75/M (Opus) · ~$15/M (Sonnet)"→"Claude Opus 5 $5/$25（2026-07-24发布）；Sonnet 5 $2/$10（至2026-08-31推广价）；Fable 5 $10/$50；Haiku 4.5 $1/$5"（benchlm.ai/anthropic/api-pricing）
4. 定价表"DeepSeek ~$0.28/M input · ~$1.10/M output (V4)"→"V4 Flash $0.14/$0.28；V4 Pro $0.435/$0.87"（$1.10是V3时代的输出价）
5. "a 50x difference"（全文4处）→按现行价格重算：输入价差约36x（$5 vs $0.14）、输出约89x（$25 vs $0.28），建议改为"约35-90倍"或按具体档位表述
6. "DeepSeek V4, released in early 2026"→"DeepSeek V4于2026年4月24日发布（V4-Pro与V4-Flash两个变体）"（morphllm.com/deepseek-v4）
7. Test 4叙事"DeepSeek's 128K window...struggled near the tail end of very long inputs"→改为基于1M上下文的描述
8. FAQ"DeepSeek V4 matches or beats Claude on many coding benchmarks"建议补充具体参照（V4-Pro-Max SWE-bench Verified 80.6%，开源模型最高）

### ⚠️ 无法确认
- "模型已被下载数百万次"无官方下载量数据
- 评分4.8/5、4.5/5为主观评分
- Test 1-5实测结论为主观测试

## bolt-vs-lovable.astro
### ✅ 验证通过
- Bolt.new 由 StackBlitz 开发、WebContainers 浏览器运行 ✓
- Lovable（原 GPT Engineer）✓
- Lovable 深度 Supabase 集成 ✓
- Bolt 免费层存在（1M tokens/月、日限300K）✓
- Lovable Business $50/mo ✓

### 🔧 需要修改
1. Bolt定价："$20/mo (Pro)"（正文+定价表2处）→"Pro $25/mo（约10M tokens/月）；Teams $30/人/月；Enterprise 自定义"（nocode.mba/articles/bolt-pricing-2026）
2. 定价表"Bolt Pro $20/mo — unlimited prompts"→"$25/mo — 10M tokens/月（token制，非无限）"（banani.co/blog/bolt-new-pricing）
3. Bolt定价"Business: Custom pricing — team features"→"Teams $30/人/月 — 共享工作区；Enterprise 为自定义"（totalum.app/blog/bolt-new-pricing-2026）
4. Lovable定价："$20/mo (Starter)"（正文+定价表2处）→"$25/mo（Pro档，100 credits/月+每日5 credits；免费层为每日5 credits、每月上限30）"（lovable.dev/pricing）
5. 定价表"Lovable Business $50/mo — unlimited projects, team collaboration, custom domains"→"Business $50/mo — 100 credits + SSO/安全中心等团队功能"（layer3labs.io/guides/lovable-pricing）
6. "In early 2026, Bolt.new shipped WebContainers 2.0"→"2026年Bolt发布Bolt v2：构建性能较2024版提升40%、自愈式调试、支持更大项目；'WebContainers 2.0'这一版本号未见官方确认"（willo.ai/blog/bolt-review）

### ⚠️ 无法确认
- "Bolt渲染落地页<12秒、Lovable约25秒"为编辑部实测
- 评分4.5/5、4.6/5为主观评分
