# Procurement roles — HK residential

Align schedule column **採購方式** and **設計師陪同選購** with who buys, who approves samples, and who owns delivery risk.

## Role matrix

| 採購方式 | Who buys | Sample path | Typical categories |
|----------|----------|-------------|--------------------|
| 承造商提供樣版目錄 | Contractor (承造商) | Contractor submits catalogue / physical samples for designer approval, then orders | Joinery hardware, skirting systems, paint systems, metal trims, many doors |
| 選樣後由承造商採購 | Owner/designer selects at showroom; contractor procures | 待選 brand/model → showroom lock → contractor buys to approved code | Tiles, stone tops, sanitaryware, specialty floors, feature paints |
| 業主自購 | Owner (客方) | Owner confirms brand/model/size; contractor installs if in scope | Appliances, loose furniture, some fixtures per HKRG owner-supply list |

## 設計師陪同選購

| Flag | When |
|------|------|
| 是 | Finish/colour/model still 待選; showroom decision affects design continuity |
| 否 | Spec is locked enough for contractor catalogue sample or no aesthetic selection |

## HKRG / tender alignment

- Owner-supply items (瓷磚、燈具、地板、潔具、門鎖、電器等 when excluded from quote) → list on **業主電器選擇** / **業主自購傢俬** and flag delivery dates early (often at 清拆 for tiles/windows/AC).
- Route quote completeness and §6-style owner-supply gaps to `interior-tendering-qa` + HKRG standard quotation refs.
- Contract supply disputes: do not invent clause numbers — cite project contract / HKRG adaptation.

## Decision rules

1. Empty brand/model on a showroom category → set **待選** + 陪同選購 = 是.
2. Never leave owner-supply appliances without size confirmation before joinery/MEP freeze.
3. Long-lead indent items: state programme risk; prefer ex-stock alternates via `interior-value-engineering` when needed.
