# Item code map — HK residential material schedule

Use prefixes on 物料規格表 rows so codes match drawing tags. Serials are project-local (`FL-01`, `WT-A`, `DR-FD`).

| Prefix | Category (物料類別) | Typical items |
|--------|---------------------|---------------|
| DH | 五金 / door hardware | Door ironmongery sets (non-FD certified) |
| HW | 五金 / joinery & metal hardware | Soft-close hinges, runners, curtain tracks, custom metal frames |
| FL | 地板 | SPC, timber, ceramic floor tiles |
| SK | 地板配件 | Skirting / 腳線 |
| CL | 天花 | Alu strip / gypsum false ceiling, light coves |
| CB | 木器基板／飾面板 | Plywood carcass, HPL / veneer faces (`CB-PLY`, `CB-HPL`) |
| CT | 枱面石材 | Worktop / vanity stone (quartz, solid surface) |
| AC | 機電包封 | AC enclosure / pipe boxing with access |
| PT | 油漆 | Emulsion, feature / art finishes |
| SW | 潔具／龍頭 | WC, basin, bath, mixers, shower, kitchen sink |
| LG | 燈具 | Track, cove LED, downlights |
| WD | 牆身飾面 | Feature timber wall / grille |
| GL | 玻璃 | Cabinet glass, shower screen |
| WT | 瓷磚 (牆) | Wall tiles (general + feature) |
| TH | 石材門檻 | Threshold strips |
| WS | 窗臺石 | Window sills |
| MT | 金屬配件／收口 | Aluminium trims, unified metal colour |
| AD | 鋪貼輔材 | Tile adhesive, anti-mould grout |
| DR | 門 | Internal doors, bath door, **FD fire doors** (`DR-FD`) |
| WP | 防水物料 | Wet-area waterproofing system |
| EL | 電掣面板 | BS faceplates / switches / sockets (when fixed-spec on schedule) |

## Coding rules

1. One unique code per schedule line; reuse codes on drawings and BOQ notes.
2. Fire-rated door sets keep a distinct code (e.g. `DR-FD`) and chain to `interior-fire-life-safety`.
3. Same-series wet tiles share brand/batch notes across `FL` + `WT` lines to reduce shade variation.
4. New prefixes allowed if documented in 填表說明 for that project.
