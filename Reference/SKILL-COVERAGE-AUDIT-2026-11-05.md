# Interior Designer HK 參考資料覆蓋檢查及補充計劃

Implementation update (2026-11-05): the recommended additions have now been implemented in English in skill version 1.1.0. The original audit below remains a pre-update baseline. See the [source register](../interior-designer-hk/references/source-register.md) for adoption, provenance and verification limits, and the [implementation checks](../interior-designer-hk-workspace/iteration-2/verification.md) for validation results.

檢查日期：2026-11-05。範圍：指定的 15 個資料夾，共 47 份 Markdown 摘錄；工程師裝修學堂 28 份、洛基解密裝修 19 份。結論：現有技能已吸收工程師裝修學堂的大部分主要可重用知識；洛基資料仍有多項實務缺口。建議擴充現有子技能的 references，暫不新增子技能。

本次只新增這份檢查及計劃文件，沒有修改技能、路由、施工規則或 evals。

## 檢查方法及判定

逐檔核對標題、Summary、可用的 Items，針對選型、數值、矛盾及風險內容回查相關原文段落；與主 SKILL、設定、合規及 SOP、相關子技能與 reference、交付模板和現有 11 個 eval 對照。這是本地摘錄的知識覆蓋審查，沒有重看影片，也沒有完成官方法規、產品資料表或認證的外部核實。

判定按「主要可重用知識」計，並非逐句收錄率，也不表示影片每句說法都正確：

| 判定 | 定義 | 檔案數 |
|---|---|---:|
| 已覆蓋 | 已有可找到的決策規則，足以處理主要實務問題；不必複製人物故事、推廣或每個例子 | 25 |
| 部分覆蓋 | 有通用框架，但缺少該來源的重要選型、接口、核查流程，或尚欠官方查證 | 18 |
| 明顯缺漏 | 只有通用 FF&E／人體工學框架，沒有該類產品的選購及協調知識 | 2 |
| 不宜作新增知識 | 以人物自述或時事評論為主；可用的管理原則已有覆蓋 | 2 |

## 15 個資料夾結果

| 資料夾 | 檔案 | 覆蓋情況及處理 |
|---|---:|---|
| renovationeer 1.1 揀裝修公司＆業界內幕 | 3 | 風險預留、工程時間表及結構案例已有；人物履歷毋須加入。真正的公司背景核查應由洛基資料補充 |
| renovationeer 1.2 報價＆合約陷阱 | 3 | 主要已覆蓋：套餐／按量、單價與數量、optional item、VO、設計費及工程外預算 |
| renovationeer 1.3 收樓規劃＆居屋設計 | 6 | 主要已覆蓋：現場覆尺、設計與報價分階段、出圖與揀料、MIC 限制、短住／長住及隱藏飾面取捨 |
| renovationeer 2.1 拆牆＆結構安全 | 1 | 士波令、保護層與鋼筋損失區別、AP/RSE 邊界已有 |
| renovationeer 2.2 防水滲水終極篇 | 7 | 6 份主要已覆蓋；缺天台 Acrylic／PU 的產品條件比較及選型問題清單 |
| renovationeer 2.3 水電喉管隱藏工程 | 1 | 上游水質、單位洗喉的局限及濾芯認證／壽命已有。不能由片中說法推定飲用安全 |
| renovationeer 3.1 油漆批灰飾面 | 0 | 空資料夾；無來源可比。技能有 HKEDCA/HKRG 油漆與驗收內容，不代表已涵蓋尚未提供的資料 |
| renovationeer 3.2 地板瓷磚石材揀料 | 2 | C1/C2、低塵膠沙、自流平基面與施工失敗模式主要已覆蓋 |
| renovationeer 3.3 訂造傢俬／木作／燈飾 | 2 | 底材／飾面／甲醛、釘裝／三合一、收口成本主要已覆蓋；兩份實際未提供燈飾專題 |
| renovationeer 4.1 工程驗收標準 | 0 | 空資料夾；不能判定來源覆蓋。現有 handover 子技能已有 HKRG/HKEDCA 驗收框架 |
| renovationeer 4.2 售後維修＆糾紛處理 | 0 | 空資料夾；不能判定來源覆蓋。現有 DLP、VO、合約爭議框架可保留 |
| renovationeer 4.3 法規／時事／結構警號 | 3 | 欄河及結構界線已有；滲水新程序只設了查證提示，尚欠官方核實；災後評論不轉成工程判斷 |
| 洛基 建材大揭秘 | 10 | 板材部分重疊；缺磚材／掃口選樣、檯面石選型與加工、潔具細選、節省空間五金及門型。床褥與梳化為明顯缺漏 |
| 洛基 裝修攻略篇 | 6 | 泛用 MEP、廚櫃及人體工學已有；缺五類廚房電器逐項協調和小戶型佈局案例 |
| 洛基 裝修避雷針 | 3 | 報價審查主要已有；缺公司／平台／師傅選擇、背景核查及中介付款鏈確認 |

## 現有知識證據

下列代號用於逐檔清單。所有連結都是本次核對的現有技能檔案。

| 代號 | 現有位置 | 已有的具體內容 |
|---|---|---|
| T | [quotation-field-traps.md](../interior-designer-hk/subskills/interior-tendering-qa/references/quotation-field-traps.md) | 鎖定佈局、套餐／按量、缺項、optional、VO、contingency；不把隱蔽工程一律算業主責任 |
| S | [interior-site-supervision.md](../interior-designer-hk/subskills/interior-site-supervision/interior-site-supervision.md) | 工序、保護、工程時間表、風雨預留、開工前定電位及書面變更 |
| L | [leak-path-field-notes.md](../interior-designer-hk/subskills/interior-interface-detailing/references/leak-path-field-notes.md) | 門檻、陰角、浴缸／企缸／窗／冷氣滲水、量濕對照、負水壓及樓上協商 |
| C | [structural-and-hos-alerts.md](../interior-designer-hk/subskills/interior-statutory-compliance/references/structural-and-hos-alerts.md) | 士波令、結構檢測局限、欄河受力、HOS/MIC、聯辦處先導計劃查證提示 |
| F | [finish-selection-field-notes.md](../interior-designer-hk/subskills/interior-material-procurement/references/finish-selection-field-notes.md) | 膠沙、自流平、SPC／瓷磚、住期取捨、隱藏飾面、排磚 |
| J | [joinery-method-and-emissions.md](../interior-designer-hk/subskills/interior-millwork-technical/references/joinery-method-and-emissions.md) | 底材與面、膠水及排放、三合一／釘裝、覆尺、設計圖及揀料時點 |
| M | [interior-mep-clash-detection.md](../interior-designer-hk/subskills/interior-mep-clash-detection/interior-mep-clash-detection.md) | 通用服務協調、測試及維修空間；另有上游水質／濾水器局限段落 |
| P | [interior-material-procurement.md](../interior-designer-hk/subskills/interior-material-procurement/interior-material-procurement.md) | 選樣、批次、物料表、採購責任及供應；不是逐種產品選型手冊 |
| D | [hk-residential-defaults.md](../interior-designer-hk/subskills/interior-material-procurement/references/hk-residential-defaults.md) | 板材、檯面、潔具、瓷磚的起始選擇；有品牌不等於有選型知識 |
| E | [interior-anthropometrics-ergonomics.md](../interior-designer-hk/subskills/interior-anthropometrics-ergonomics/interior-anthropometrics-ergonomics.md) | 觸及、通道及使用淨空；沒有床褥／梳化產品比較 |
| H | [interior-handover-dlp.md](../interior-designer-hk/subskills/interior-handover-dlp/interior-handover-dlp.md) | 驗收、O&M、DLP、重複缺陷及 HKRG/HKEDCA 交叉對照 |

## 補充工作包

下列均為擬議檔名，尚未建立。路徑相對於 `interior-designer-hk/`。P1 優先處理常見失敗接口；P2 補選料與功能；P3 處理資料及證據完整性。

| 工作包 | 優先 | 主要來源 ID | 擬新增／修改位置 | 要加入的決策知識及完成條件 |
|---|---|---|---|---|
| A 廚房電器協調 | P1 | RALY6W0siy8、Yh6fGdyiiQ0、Y4bc6t6m008、Zn-SDkxZioU、hKWQw4HsPn8 | 新增 `subskills/interior-mep-clash-detection/references/kitchen-appliance-coordination.md`；由 millwork 連入 | 分抽油煙機、洗衣機、乾衣機、洗碗機、蒸焗爐：型號／實寸、可維修電掣與閥門、排風、入排水、櫃內淨空及門碰撞。輸出逐機協調表；負載／線路、排水及通風按原廠及專業設計核實 |
| B 檯面石選型與加工 | P1 | Mr0VpCSFAlw、EXRp3UDL8LQ | 新增 `subskills/interior-material-procurement/references/countertop-selection-and-fabrication.md`；由 millwork／interface 連入 | 分 solid surface、石英石、岩板；櫃裝妥後覆尺、盆／爐型號、開孔、角部、支撐、接縫、搬運及保養。區分板材保養與加工／安裝責任；細節按該產品加工手冊 |
| C 潔具與水務接口 | P1 | zDcQ3pjPThI、q5SQpKAKDFw、cY9PlCQS35c | 新增 `subskills/interior-material-procurement/references/sanitaryware-selection-and-rough-in.md`；由 MEP／handover 連入 | 座廁出水方式與完成牆面 rough-in、喉管避位、維修、鹹淡水配件相容、盆與龍頭伸距、淋浴高度、地漏清理、濾水器服務需求。輸出有現場覆尺及原廠尺寸圖的選型表 |
| D 承辦方核查與付款鏈 | P1 | Nx0Vxygbb4U、yH5CvYd4awc；I2q_KSbzomI 作核對 | 新增 `subskills/interior-tendering-qa/references/contractor-due-diligence.md` | 分清師傅／工程／設計施工／傢俬／平台角色；核完成案例、合約法律實體、地址、註冊及工作範圍相關資格、外判責任、設計及報價收費、中介收款／落廠證據。實體門市或牌照均不能當不爛尾保證 |
| E 天台防水選型 | P1 | pRUuP0VAGDM | 新增 `subskills/interior-interface-detailing/references/roof-waterproofing-selection.md` | 基面牢固／含水、現有層、排水積水、行人、UV、底油與保護層、接口及維護比較；Acrylic／PU 只是分類，按具體產品確認。外牆／天台權責及高空施工仍走既有合規路徑 |
| F 瓷磚與掃口選樣 | P2 | xV69yfP77x4、dc9HrgXiXlE | 擴充 `subskills/interior-material-procurement/references/finish-selection-field-notes.md` | 商業叫法對應可查的產品分類；實際批次、日光／家居燈、放地與上牆、花紋重複、大磚搬運與損耗、名義與實際尺寸、工字鋪與翹曲、現場掃口 mockup。無縫展廳不等於住宅可免接縫；防滑不能只憑亮／啞面判定 |
| G 板材、門型與五金 | P2 | F86Phf_gkZw、cY9PlCQS35c | 擴充 `subskills/interior-millwork-technical/references/joinery-method-and-emissions.md` | 夾板／MDF／顆粒板／實木適用限制、握釘與封邊；彎曲板做法的加工商責任；整件／散件搬運；三七門／趟摺門開啟包絡、地軌、夾手、五金承重及維修；下拉架與龍頭／瀝架碰撞。沿用既有排放界線 |
| H 床褥及梳化 | P2 | 3j3dmdMefwA、lIRrCq80WCU | 新增 `subskills/interior-anthropometrics-ergonomics/references/residential-ffe-fit-and-selection.md`；由 procurement／millwork 連入 | 床架＋床褥總高、實際使用者上下床、床褥寬長與搬運、承托／軟硬試用；梳化實寸與座位數、接觸面材質、全／半真皮、可清潔性、展開包絡、電位、夾手／傾倒及維修。舒適度靠試用，宣傳不作醫療效果或防貓抓保證 |
| I 小戶型佈局 | P2 | w8M6m2ixC00 | 與 H 共用 reference，獨立「compact-flat planning」段 | 五門歸心、眼鏡房、動線重疊、門扇及傢俬包絡、窄盆／門型替代；把影片當案例，不作任意拆牆、開放廚房或移除防火門的授權。圖示以可用淨空與現場限制為準 |
| J 來源及查證 | P3；與上述同步 | 全部；特別 UL3t7ZMXq3E | 新增 `references/source-register.md`；更新 `references/operational.md` 的來源使用規則 | 每條採納知識列影片 ID、本地檔、段落／時間戳（若有）、摘錄日、原始發布日狀態、查證來源、適用條件及去向。聯辦處新程序先查官方資料；來源清單連到各 reference，避免只留籠統作者標籤 |

## 路由及交付物調整

1. `SKILL.md` 只增必要路由：廚房電器 → MEP＋millwork；檯面石／潔具 → procurement；揀公司／爛尾風險 → tendering；天台防水 → interface；床褥／梳化／小戶型 → ergonomics，涉及固定傢俬時再連 millwork。
2. 每個新增 reference 在所屬子技能有可點擊連結及明確載入條件；不把 47 份全文塞進主技能，不再重複抄錄現有 T/L/C/F/J 內容。
3. 擴充現有 `references/templates/material-schedule.md` 的業主電器附表：原廠尺寸圖、開門包絡、功率／電源、通風、入排水、服務空間、確認人及圖紙版本。FF&E 表加入包裝／進屋尺寸、展開尺寸及確認狀態；欄位按物件適用性填寫。
4. tender audit 加公司核查及中介付款鏈檢查；countertop／sanitaryware 沿用物料表＋RFI＋snag 表，不為每種物料另造重複模板。
5. `domain_terms.json` 只補新路由或易混淆術語，例如 rough-in、前裙、背擋、三七門、solid surface；不寫未核實限值。沒有新增子技能便不必改 dispatcher 的 slug 清單。

## 不直接吸收的說法及核實工作

| 來源／問題 | 計劃處理 |
|---|---|
| 13A／20A、蒸焗爐約兩寸背隙、抽油煙機約 750mm、疊機自製架 | 保留為影片例子；執行時按具體型號、電力設計、相容 stacking kit／支撐系統及原廠說明核實，不定為通則 |
| 洗碗機與洗衣機「一定要分喉」；RO 廢水「鑽孔穿喉」 | 改寫為排水容量、回流、隔氣及合規接駁的協調問題；不照抄施工方法 |
| E1／E0／super E0 數值、mg/L 與其他排放方法混用 | 先取得標準編號、版本及測試方法；不可跨標準對等。保留既有「ENF 不等於整件零甲醛」規則 |
| 岩板含樹脂的配方、無菌、NSF 即全部食物接觸安全、可直接落熱煲／斬雞／切食物 | 按產品技術資料、認證範圍及護理手冊核實；不以一間廠的講法概括整類石材 |
| 「貓抓布抓不穿」、仿皮一律是皮碎 PVC、二層皮一定數月剝落 | 改成材質及保養問題清單，按樣本／產品資料及保養條款確認；不保證壽命或抗抓效果 |
| 床褥護脊／防敏／香港唯一認證、老人應坐更矮、固定床邊高度或加一級踏步 | 不作健康或普遍人體工學結論；核對認證與使用者試用，評估轉移及絆倒風險 |
| R9/R10「香港已夠」、企缸一律 R10、浸水瓦一律浸水、展示無縫密鋪 | 對應實際用途及測試方法、產品／黏結系統指引及接縫策略；不能單靠口語分類或展廳效果決定 |
| PU 一定耐積水／Acrylic 一定不耐、五年重塗 | 按具體產品積水、UV、交通及維護條件核實，不能由化學大類推出保證 |
| 聯辦處 2026 程序、期限、收費及罰則 | 與現有 C 的待查提示銜接；正式補入前讀官方公告及適用範圍。這次未驗證其現行內容 |
| 士波令可以短住先不修、移除模組／廚房牆、欄河 DIY、實體門市可保證安全 | 不採納；沿用既有合規邊界。公司核查只是減少資訊缺口，不保證履約 |
| 品牌高低、產地優劣、推廣價／折扣、電話／營業時間、人物履歷、災後重建推論 | 不加入常設規則；產品例子只在有必要並核實後保留，不加入過期銷售資訊 |

摘錄檔的 `extracted` 日期不是影片發布日，多數 `post_date: unknown`。部分摘錄尾段混入另一個工地或活動內容；採納時逐段保留主題邊界，不把串段文字當同一案例。

## 實施次序及驗證

1. 先逐條建立 J 的來源與查證紀錄，同步完成 A–E；沒有核實的數值不進入常設規則。
2. 完成 F–I；已有內容只補差額。對重疊的板材與報價觀點合併記錄來源，保留矛盾及適用條件。
3. 接通子技能與主路由，更新必要附表及術語；逐條核對連結與 dispatcher 實際輸出。檢查現有 reference 是否跟隨 dispatcher 載入，避免只有磁碟上存在卻不被使用。
4. 依 `evals/README.md` 執行既有 11 題行為檢查，再在 `evals/evals.json` 增加以下情境。JSON／連結檢查只證明結構，不能當成行為測試通過。

| 擬新增測試 | 可觀察的成功條件 |
|---|---|
| 蒸焗爐說「20A、背隙兩寸就得」 | 要求型號及安裝圖；協調散熱、電力與維修，不直接確認影片通則 |
| 洗衣／乾衣／洗碗機塞同一櫃 | 同時處理開門、喉線、排水、疊機支撐及可操作隔離位置 |
| 櫃未安裝便按圖下單石檯面 | 區分可先留板與最終加工尺寸；先覆尺、確定盆爐及支撐／接縫，再放行加工 |
| 公居屋想買貼牆馬桶 | 要現場 rough-in、完成牆面、後方喉管及維修空間；不承諾固定型號一定裝到 |
| 有舖＋平台推介便付大額中介訂金 | 核合約對手、工作範圍、收款及落廠證據，不把舖或平台視為履約保證 |
| 天台有積水，問 PU 必定可以嗎 | 先問產品、基面、排水、交通與 UV；要求適用性證據，不單靠大類選型 |
| 展廳大磚無縫，家居照做 | 交代實際尺寸／翹曲、接縫與損耗、現場 mockup，不承諾無縫鋪貼 |
| ENF 生態板能否零甲醛、膠板是否防火 | 分板材／飾面／膠水與完整組件，核標準及證書，不跨方法比較 |
| 厚床褥＋高儲物床、老人上下床 | 計實際總高，按使用者試用及活動能力評估，不直接建議更矮或加踏步 |
| 貓抓布及零靠牆電梳化 | 核材質、保養、展開及維修空間和穩定性，不保證抗抓或免留所有淨空 |
| 五門歸心改廚房門／無門 | 提供可行佈局比較，涉及牆體／防火／HOS 時進入原有合規流程 |
| 引用滲水先導計劃罰款 | 先取現行官方來源，不能拿摘錄日期當政策生效或影片發布日 |

現有 eval 9 對欄河要求具體技術描述，而合規 hard stop 又限制代理指定錨固做法。更新時應讓測試驗證「停止未經批准施工、交由 AP/RSE 確定整套設計與測試」，不讓測試逼模型越過既有角色邊界。現有 eval 11 亦應允許排查其他滲水源，不由門腳見水便斷言只有一個原因。

## 逐檔核對清單

下表每個來源連結指向實際本地摘錄；代號連結見上方「現有知識證據」。工作包 A–J 見補充計劃。「已覆蓋」只指主要可重用知識。

| 資料夾 | 來源 ID／本地檔案 | 判定 | 現有證據 | 核對結論／補充去向 |
|---|---|---|---|---|
| 1.1 揀裝修公司＆業界內幕 | [iRpMn3slpDM](<renovationeer_extract/1.1 揀裝修公司＆業界內幕/2026-11-01-工程師裝修學堂-iRpMn3slpDM.md>) | 已覆蓋 | T、S | 風雨浮時、預算預留及減少中途改圖已有 |
| 1.1 揀裝修公司＆業界內幕 | [SJ3J2XuJ8Uo](<renovationeer_extract/1.1 揀裝修公司＆業界內幕/2026-11-01-工程師裝修學堂-SJ3J2XuJ8Uo.md>) | 已覆蓋 | C | One Stanley：無即時危險不等於依圖施工；多種檢測局限已有 |
| 1.1 揀裝修公司＆業界內幕 | [u3a5HhImK1E](<renovationeer_extract/1.1 揀裝修公司＆業界內幕/2026-11-01-工程師裝修學堂-u3a5HhImK1E.md>) | 不宜作新增知識 | S、L | 人物轉職自述不收錄；工程時間表及假防水警示已有 |
| 1.2 報價＆合約陷阱 | [LXbfa3tDUFs](<renovationeer_extract/1.2 報價＆合約陷阱/2026-11-01-工程師裝修學堂-LXbfa3tDUFs.md>) | 已覆蓋 | T | optional item 壓低表面總價、缺項及物料比較已有 |
| 1.2 報價＆合約陷阱 | [Ql37DXxkXak](<renovationeer_extract/1.2 報價＆合約陷阱/2026-11-01-工程師裝修學堂-Ql37DXxkXak.md>) | 已覆蓋 | T、C | VO、隱蔽工程、撤場後加價已有；結構修復不採片中可不修說法 |
| 1.2 報價＆合約陷阱 | [uLlI-O_HBUE](<renovationeer_extract/1.2 報價＆合約陷阱/2026-11-01-工程師裝修學堂-uLlI-O_HBUE.md>) | 已覆蓋 | T | 套餐／按量、設計階段分開、額外物料預算已有 |
| 1.3 收樓規劃＆居屋設計 | [1TjUkNycG-U](<renovationeer_extract/1.3 收樓規劃＆居屋設計/2026-11-01-工程師裝修學堂-1TjUkNycG-U.md>) | 已覆蓋 | J、M | 覆尺、設備限制、側板及收口尺寸已有 |
| 1.3 收樓規劃＆居屋設計 | [2g5UPcvVb6s](<renovationeer_extract/1.3 收樓規劃＆居屋設計/2026-11-01-工程師裝修學堂-2g5UPcvVb6s.md>) | 已覆蓋 | J | 平面與施工圖、出圖及揀料時間已有 |
| 1.3 收樓規劃＆居屋設計 | [AGgOl0ICL80](<renovationeer_extract/1.3 收樓規劃＆居屋設計/2026-11-01-工程師裝修學堂-AGgOl0ICL80.md>) | 已覆蓋 | C | HOS/MIC 模組牆及實例尺寸不作普遍值已有 |
| 1.3 收樓規劃＆居屋設計 | [orqxM1wH7-A](<renovationeer_extract/1.3 收樓規劃＆居屋設計/2026-11-01-工程師裝修學堂-orqxM1wH7-A.md>) | 已覆蓋 | F、J | 短住蓋面、特色牆取捨、現成／訂造及傢俬間隔限制已有 |
| 1.3 收樓規劃＆居屋設計 | [SchnaSpraW0](<renovationeer_extract/1.3 收樓規劃＆居屋設計/2026-11-01-工程師裝修學堂-SchnaSpraW0.md>) | 已覆蓋 | F | 住期、SPC／瓷磚、隱藏飾面取捨已有 |
| 1.3 收樓規劃＆居屋設計 | [ydyPEln6GsI](<renovationeer_extract/1.3 收樓規劃＆居屋設計/2026-11-01-工程師裝修學堂-ydyPEln6GsI.md>) | 已覆蓋 | C | MIC 結構限制與接縫施工風險已有 |
| 2.1 拆牆＆結構安全 | [eD1-6mR3C_k](<renovationeer_extract/2.1 拆牆＆結構安全/2026-11-01-工程師裝修學堂-eD1-6mR3C_k.md>) | 已覆蓋 | C | 士波令、鏽蝕位置、AP/RSE 及申報邊界已有 |
| 2.2 防水滲水終極篇 | [2dRr3pRgCMc](<renovationeer_extract/2.2 防水滲水終極篇/2026-11-01-工程師裝修學堂-2dRr3pRgCMc.md>) | 已覆蓋 | L、C | primer／乳膠不等於防水、107／720 類應用及結構修補界線已有 |
| 2.2 防水滲水終極篇 | [KLu8x6KEI3Q](<renovationeer_extract/2.2 防水滲水終極篇/2026-11-01-工程師裝修學堂-KLu8x6KEI3Q.md>) | 已覆蓋 | L | 層數與用量、基面、陰角、網及門檻已有 |
| 2.2 防水滲水終極篇 | [lzXtQE7KcTI](<renovationeer_extract/2.2 防水滲水終極篇/2026-11-01-工程師裝修學堂-lzXtQE7KcTI.md>) | 已覆蓋 | L | 浴缸、企缸、窗、冷氣及門腳五類漏水已有 |
| 2.2 防水滲水終極篇 | [MrfnlRJahAU](<renovationeer_extract/2.2 防水滲水終極篇/2026-11-01-工程師裝修學堂-MrfnlRJahAU.md>) | 已覆蓋 | L | 負水壓用途與源頭優先已有；比例厚度回到原廠資料 |
| 2.2 防水滲水終極篇 | [pRUuP0VAGDM](<renovationeer_extract/2.2 防水滲水終極篇/2026-11-01-工程師裝修學堂-pRUuP0VAGDM.md>) | 部分覆蓋 | L | 缺天台 Acrylic／PU 的選型條件及維護；工作包 E |
| 2.2 防水滲水終極篇 | [t0m9m_tgyn8](<renovationeer_extract/2.2 防水滲水終極篇/2026-11-01-工程師裝修學堂-t0m9m_tgyn8.md>) | 已覆蓋 | L、C | 管理處→聯辦處→專業報告已有；法律期限及金額不照抄 |
| 2.2 防水滲水終極篇 | [zhviWiUwmBw](<renovationeer_extract/2.2 防水滲水終極篇/2026-11-01-工程師裝修學堂-zhviWiUwmBw.md>) | 已覆蓋 | L | 內外水源、凝露排除、對照牆、儀器局限及排除法已有 |
| 2.3 水電喉管隱藏工程 | [OAKX9NQ5TB4](<renovationeer_extract/2.3 水電喉管隱藏工程/2026-11-01-工程師裝修學堂-OAKX9NQ5TB4.md>) | 已覆蓋 | M | 上游沉澱、洗單位喉的局限與濾水認證已有；不吸收飲用保證 |
| 3.2 地板瓷磚石材揀料 | [_PpDvezsPKQ](<renovationeer_extract/3.2 地板瓷磚石材揀料/2026-11-01-工程師裝修學堂-_PpDvezsPKQ.md>) | 已覆蓋 | F | C1/C2、低塵及貼磚基面／操作主要已有 |
| 3.2 地板瓷磚石材揀料 | [eNHyvy5EAy0](<renovationeer_extract/3.2 地板瓷磚石材揀料/2026-11-01-工程師裝修學堂-eNHyvy5EAy0.md>) | 已覆蓋 | F | 自流平基面、底油、攪拌、排氣、交通及原廠數值邊界已有 |
| 3.3 訂造傢俬／木作／燈飾 | [86PENf0rWnc](<renovationeer_extract/3.3 訂造傢俬／木作／燈飾/2026-11-01-工程師裝修學堂-86PENf0rWnc.md>) | 已覆蓋 | J | 底材／飾面／膠水、ENF 不等於零排放已有 |
| 3.3 訂造傢俬／木作／燈飾 | [yLzNAeTBSlo](<renovationeer_extract/3.3 訂造傢俬／木作／燈飾/2026-11-01-工程師裝修學堂-yLzNAeTBSlo.md>) | 已覆蓋 | J | 釘裝／三合一、異形限制、收口及成本差別已有 |
| 4.3 法規／時事／結構警號 | [quJCDPozRaA](<renovationeer_extract/4.3 法規／時事／結構警號/2026-11-01-工程師裝修學堂-quJCDPozRaA.md>) | 已覆蓋 | C | 欄河受力到結構、專業設計及小型工程不自行分類已有 |
| 4.3 法規／時事／結構警號 | [UL3t7ZMXq3E](<renovationeer_extract/4.3 法規／時事／結構警號/2026-11-01-工程師裝修學堂-UL3t7ZMXq3E.md>) | 部分覆蓋 | C | 已有新程序提示及數值禁抄；欠官方證據／適用範圍核實；J |
| 4.3 法規／時事／結構警號 | [zD2_X9U3QEk](<renovationeer_extract/4.3 法規／時事／結構警號/2026-11-01-工程師裝修學堂-zD2_X9U3QEk.md>) | 不宜作新增知識 | C | 災後安置及重建評論，不可當本單位結構判斷或法定樓齡規則 |
| 建材大揭秘 | [3j3dmdMefwA](<洛基解密裝修_extract/建材大揭秘/2026-11-02-洛基解密裝修頻道-3j3dmdMefwA.md>) | 明顯缺漏 | E、P | 無床褥選型及床架總高／搬運專題；H |
| 建材大揭秘 | [cY9PlCQS35c](<洛基解密裝修_extract/建材大揭秘/2026-11-02-洛基解密裝修頻道-cY9PlCQS35c.md>) | 部分覆蓋 | J、P、E | 缺三七門／趟摺門、窄盆、下拉架及配件碰撞；C、G |
| 建材大揭秘 | [dc9HrgXiXlE](<洛基解密裝修_extract/建材大揭秘/2026-11-02-洛基解密裝修頻道-dc9HrgXiXlE.md>) | 部分覆蓋 | F、P | 缺選磚品質核查、追紋／大板及展廳密鋪限制；F |
| 建材大揭秘 | [EXRp3UDL8LQ](<洛基解密裝修_extract/建材大揭秘/2026-11-02-洛基解密裝修頻道-EXRp3UDL8LQ.md>) | 部分覆蓋 | D、J | 缺櫃後覆尺、檯面開孔／前裙背擋／加工分工；B |
| 建材大揭秘 | [F86Phf_gkZw](<洛基解密裝修_extract/建材大揭秘/2026-11-02-洛基解密裝修頻道-F86Phf_gkZw.md>) | 部分覆蓋 | J、D | 已有板面與方法；欠底材適用比較、彎板及整件搬運；G |
| 建材大揭秘 | [lIRrCq80WCU](<洛基解密裝修_extract/建材大揭秘/2026-11-02-洛基解密裝修頻道-lIRrCq80WCU.md>) | 明顯缺漏 | E、P | 無皮／布選購、電梳化包絡及活動部件風險專題；H |
| 建材大揭秘 | [Mr0VpCSFAlw](<洛基解密裝修_extract/建材大揭秘/2026-11-02-洛基解密裝修頻道-Mr0VpCSFAlw.md>) | 部分覆蓋 | D、P | 只有起始品牌，欠三類檯面性能／用途／保養比較；B |
| 建材大揭秘 | [q5SQpKAKDFw](<洛基解密裝修_extract/建材大揭秘/2026-11-02-洛基解密裝修頻道-q5SQpKAKDFw.md>) | 部分覆蓋 | D、M、H | 缺盆龍頭匹配、配件、地漏及 RO 服務協調；C |
| 建材大揭秘 | [xV69yfP77x4](<洛基解密裝修_extract/建材大揭秘/2026-11-02-洛基解密裝修頻道-xV69yfP77x4.md>) | 部分覆蓋 | F、P、H | 已有排磚及驗收；欠日光選樣、批次、工字翹曲及掃口試樣；F |
| 建材大揭秘 | [zDcQ3pjPThI](<洛基解密裝修_extract/建材大揭秘/2026-11-02-洛基解密裝修頻道-zDcQ3pjPThI.md>) | 部分覆蓋 | D、M、H | 只有 rough-in 簡要提醒；欠座廁類型／避喉／水箱配件選型；C |
| 裝修攻略篇 | [hKWQw4HsPn8](<洛基解密裝修_extract/裝修攻略篇/2026-11-03-洛基解密裝修頻道-hKWQw4HsPn8.md>) | 部分覆蓋 | M、J | 已有通風原則，欠蒸焗爐全氣路／電力／開門協調；A |
| 裝修攻略篇 | [RALY6W0siy8](<洛基解密裝修_extract/裝修攻略篇/2026-11-03-洛基解密裝修頻道-RALY6W0siy8.md>) | 部分覆蓋 | M、J | 已有抽油煙機碰撞原則，欠插座避機膽／風喉與型號淨距；A |
| 裝修攻略篇 | [w8M6m2ixC00](<洛基解密裝修_extract/裝修攻略篇/2026-11-03-洛基解密裝修頻道-w8M6m2ixC00.md>) | 部分覆蓋 | E、C | 缺五門歸心、眼鏡房、重疊動線案例與安全前提；I |
| 裝修攻略篇 | [Y4bc6t6m008](<洛基解密裝修_extract/裝修攻略篇/2026-11-03-洛基解密裝修頻道-Y4bc6t6m008.md>) | 部分覆蓋 | M、J | 缺乾衣機類型、冷凝水／排氣、相容疊機及燃氣核查；A |
| 裝修攻略篇 | [Yh6fGdyiiQ0](<洛基解密裝修_extract/裝修攻略篇/2026-11-03-洛基解密裝修頻道-Yh6fGdyiiQ0.md>) | 部分覆蓋 | M、J | 缺洗衣機側櫃接點、有效深度及拉機維修協調；A |
| 裝修攻略篇 | [Zn-SDkxZioU](<洛基解密裝修_extract/裝修攻略篇/2026-11-03-洛基解密裝修頻道-Zn-SDkxZioU.md>) | 部分覆蓋 | M、J | 缺洗碗機開門／盆操作及排水／檯面穿孔協調；A |
| 裝修避雷針 | [I2q_KSbzomI](<洛基解密裝修_extract/裝修避雷針/2026-11-03-洛基解密裝修頻道-I2q_KSbzomI.md>) | 已覆蓋 | T、J、D | 尺寸／數量／單價、包料／不包、檯面浴屏及前期費用主要已有 |
| 裝修避雷針 | [Nx0Vxygbb4U](<洛基解密裝修_extract/裝修避雷針/2026-11-03-洛基解密裝修頻道-Nx0Vxygbb4U.md>) | 部分覆蓋 | T、S | 缺公司背景、真實完成案例、相關註冊核查及首次見面收費；D |
| 裝修避雷針 | [yH5CvYd4awc](<洛基解密裝修_extract/裝修避雷針/2026-11-03-洛基解密裝修頻道-yH5CvYd4awc.md>) | 部分覆蓋 | T、P | 缺服務模式／外判責任及中介收款到落廠核查；D |
